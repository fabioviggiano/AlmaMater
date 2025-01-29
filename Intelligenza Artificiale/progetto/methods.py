import os

import pandas as pd
import shap
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

import constants
from constants import *

def readCSV():
    data = pd.read_csv(csvFilePath)
    if data.shape[0] > 0 and data.shape[1] > 0:
        print(messageFileReadCorrectly)
        return data
    else:
        print(messageFileNotReadCorrectly)
        return None

def executeTreeExplainer(model, xTest):
    print(messageExecuteTreeExplainer)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(xTest)

    print(messageXTestShape + (xTest.shape))
    print(messageLenShapValues + (len(shap_values)))

    # Grafico riepilogativo globale
    shap.summary_plot(shap_values, xTest, feature_names=features)

    # Grafico dell'impatto del genere (sex)
    shap.dependence_plot("sex", shap_values, xTest, feature_names=features)

    # Grafico dell'impatto della razza (race)
    shap.dependence_plot("race", shap_values, xTest, feature_names=features)

    # this part is not tested yet
    shap.force_plot(explainer.expected_value, shap_values[42], xTest.iloc[42])
    return model

# Funzione per analisi SHAP globale e specifica
def shap_analysis(sub_data, target, features, model_desc):
    # Verifica che il subset non sia vuoto
    if sub_data.empty:
        print(f"Il subset '{model_desc}' è vuoto. Salto l'analisi.")
        return

    # Divisione dati
    X_sub = sub_data[features]
    y_sub = sub_data[target]

    # train_test_split - Funzione per dividere il dataset in set di training e test

    X_train_sub, X_test_sub, y_train_sub, y_test_sub = train_test_split(
        X_sub, y_sub, test_size=0.2, random_state=42
    )

    # Addestramento modello
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_sub, y_train_sub)

    # Creazione Explainer SHAP
    explainer = shap.TreeExplainer(model, X_train_sub)
    shap_values = explainer(X_test_sub)

    # Valutazione modello
    y_pred = model.predict(X_test_sub)
    print(f"Modello per {model_desc}:")
    print(f"R²: {r2_score(y_test_sub, y_pred):.4f}")
    print(f"MAE: {mean_absolute_error(y_test_sub, y_pred):.4f}")

    # Analisi globale con titolo personalizzato
    print(f"Analisi globale per {model_desc}")
    shap.summary_plot(shap_values, X_test_sub, feature_names=features, show=False)
    plt.title(f"SHAP Summary Plot - {model_desc}")
    plt.show()

    # Analisi di dipendenza per "race" e "citizen" con titolo personalizzato
    print(f"Analisi di dipendenza per 'race' e 'citizen' - {model_desc}")
    shap.dependence_plot("race", shap_values.values, X_test_sub, feature_names=features, show=False)
    plt.title(f"SHAP Dependence Plot (Race) - {model_desc}")
    plt.show()

    shap.dependence_plot("citizen", shap_values.values, X_test_sub, feature_names=features, show=False)
    plt.title(f"SHAP Dependence Plot (Citizen) - {model_desc}")
    plt.show()

def filterSex(df):
    male = df[df[sex] == 1]
    female = df[df[sex] == 2]
    return male, female

def avgHrwageDiffBySector(data):
    male, female = filterSex(data)
    # Calcola differenza media di `hrwage` per ogni settore
    differenze = {}
    for workSector in workSectors:
        maleMean = male[male[workSector] == 1][hrwage].mean()
        femaleMean = female[female[workSector] == 1][hrwage].mean()
        differenze[workSector] = abs(maleMean - femaleMean)
    # Ordina i settori per differenza decrescente
    orderlyDifferences = dict(sorted(differenze.items(), key=lambda item: item[1], reverse=True))
    # Mostra il settore con la maggiore differenza
    print("Settore con maggiore differenza:", max(orderlyDifferences, key=orderlyDifferences.get))
    print("Differenze per settore:", orderlyDifferences)

def maleFemaleAnalysisFunction(data):  # Divisione per genere
        male_data = data[data[sex] == 1]
        female_data = data[data[sex] == 2]

        # Analisi per maschi
        shapAnalysis(male_data, target, features, "Maschi")

        # Analisi per femmine
        shapAnalysis(female_data, target, features, "Femmine")

def citizenRaceAnalysisFnction(data):
        cittadini = data['citizen'].unique()

        # Analisi per ogni gruppo razziale
        for cittadino in cittadini:
            citizenData = data[data['citizen'] == cittadino]
            shapAnalysis(citizenData, target, features, f'Cittadinanza {cittadino}')

def raceAnalysisFunction(data):    # Valori distinti di race
    races = data[constants.race].unique()

    # Analisi per ogni gruppo razziale
    for race in races:
        race_data = data[data[race] == race]
        shapAnalysis(race_data, target, features, f"Razza:{race}")

def educAnalysisFunction(data):
    # Valori distinti di education
    educations = data['educ99'].unique()
    for edu in educations:
        edu_data = data[data['educ99'] == edu]
        shapAnalysis(edu_data, target, features, f"Education:{edu_data}")

def determineGeography(row):
    if row['northeast'] == 1:
        return 1
    elif row['northcentral'] == 1:
        return 2
    elif row['south'] == 1:
        return 3
    elif row['west'] == 1:
        return 4
    else:
        return 5

def shapDependencePlot(shap_values, X_test):
    # Grafico dell'impatto del genere (sex)
    shap.dependence_plot("sex", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'marst'])

    # Grafico dell'impatto della razza (race)
    shap.dependence_plot("race", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'sex'])

    shap.dependence_plot("geography", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'sex'])

    shap.dependence_plot("age", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'sex'])

    shap.dependence_plot("sch", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'sex'])

    shap.dependence_plot("marst", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'sex'])

    shap.dependence_plot("citizen", shap_values, X_test, feature_names=constants.features, color=shap_values[:, 'sex'])

# Funzione per analisi SHAP globale e specifica
def shapAnalysis(sub_data, target, features, model_desc):
    # Verifica che il subset non sia vuoto
    if sub_data.empty:
        print(f"Il subset '{model_desc}' è vuoto. Salto l'analisi.")
        return

    # Divisione dati
    X_sub = sub_data[features]
    y_sub = sub_data[target]

    X_train_sub, X_test_sub, y_train_sub, y_test_sub = train_test_split(
        X_sub, y_sub, test_size=0.2, random_state=42
    )

    # Addestramento modello
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_sub, y_train_sub)

    # Creazione Explainer SHAP
    explainer = shap.TreeExplainer(model, X_train_sub)
    shap_values = explainer(X_test_sub)

    # Valutazione modello
    y_pred = model.predict(X_test_sub)
    print(f"Modello per {model_desc}:")
    print(f"R²: {r2_score(y_test_sub, y_pred):.4f}")
    print(f"MAE: {mean_absolute_error(y_test_sub, y_pred):.4f}")

    # Analisi globale con titolo personalizzato
    print(f"Analisi globale per {model_desc}")
    shap.summary_plot(shap_values, X_test_sub, feature_names=features, show=False)
    plt.title(f"SHAP Summary Plot - {model_desc}")
    plt.show()

    # Analisi di dipendenza per "race" e "citizen" con titolo personalizzato
    print(f"Analisi di dipendenza per 'race' e 'citizen' - {model_desc}")
    shap.dependence_plot("race", shap_values.values, X_test_sub, feature_names=features, color=shap_values[:, 'sex'],
                         show=False)
    plt.title(f"SHAP Dependence Plot (Race) - {model_desc}")
    plt.show()

    shap.dependence_plot("citizen", shap_values.values, X_test_sub, feature_names=features, color=shap_values[:, 'sex'],
                         show=False)
    plt.title(f"SHAP Dependence Plot (Citizen) - {model_desc}")
    plt.show()

    shap.dependence_plot("sex", shap_values.values, X_test_sub, feature_names=features, color=shap_values[:, 'race'],
                         show=False)
    plt.title(f"SHAP Dependence Plot (sex) - {model_desc}")
    plt.show()

    shap.dependence_plot("geography", shap_values.values, X_test_sub, feature_names=features,
                         color=shap_values[:, 'sex'], show=False)
    plt.title(f"SHAP Dependence Plot (geography) - {model_desc}")
    plt.show()

    shap.dependence_plot("age", shap_values.values, X_test_sub, feature_names=features, color=shap_values[:, 'sex'],
                         show=False)
    plt.title(f"SHAP Dependence Plot (age) - {model_desc}")
    plt.show()

    shap.dependence_plot("sch", shap_values.values, X_test_sub, feature_names=features, color=shap_values[:, 'sex'],
                         show=False)
    plt.title(f"SHAP Dependence Plot (sch) - {model_desc}")
    plt.show()

    shap.dependence_plot("marst", shap_values.values, X_test_sub, feature_names=features, color=shap_values[:, 'sex'],
                         show=False)
    plt.title(f"SHAP Dependence Plot (marst) - {model_desc}")
    plt.show()

def threeFilters(data):
    data = data[(data[constants.firstDatasetFilter] >= 7) & (data[constants.firstDatasetFilter] <= 50)]

    print(f"First filter: '{len(data)}'")

    # Filter by not null value for nativity
    data = data[data[constants.secondDatasetFilter].notna()]
    print(f"Second filter: '{len(data)}'")

    # Filter by hours worked per week
    data = data[data[constants.thirdDatasetFilter] <= 48]
    print(f"Third filter: '{len(data)}'")

    # Ottieni la dimensione del dataset filtrato
    lenFilteredDataset = len(data)

    print(f"Numero di righe nel dataset filtrato: '{lenFilteredDataset}'")

    return data

# Funzioni per il plot

def plotWageDistribution(data):
    # Count the number of observations in each group
    wage_distribution = data[groupingColumn].value_counts().sort_index()
    # Plot the distribution
    plt.figure(figsize=(10, 6))
    wage_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
    #TODO Aggiornare etichette plot in base alle variabili
    plt.title(f'{columnToExtract} Distribution')
    plt.xlabel(f'{columnToExtract} Range')
    plt.ylabel('Number of Observations')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(8, 6))
    plt.boxplot(data[columnToExtract])
    plt.title(f'{columnToExtract} Wage')
    plt.ylabel(f'{columnToExtract}')
    plt.show()

def executeFunctionMaleFemaleAnalysis(data):
    # Divisione per genere
    male, female = filterSex(data)

    # Analisi per maschi
    shapAnalysis(male, target, constants.features, "Maschi")

    # Analisi per femmine
    shapAnalysis(female, target, constants.features, "Femmine")

def executeFunctionCitizenAnalysis(data):
    # Valori distinti di cittadinanza
    citizenUniqueData = data['citizen'].unique()

    # Analisi per ogni gruppo cittadinanza
    for citizen in citizenUniqueData:
        citizenData = data[data['citizen'] == citizen]

        # Ottenere il nome dal dizionario, se non presente usa il numero originale
        citizenName = constants.citizen_mapping.get(citizen, f"Codice {citizen}")

        shapAnalysis(citizenData, target, constants.features, f"Cittadinanza: {citizenName}")

def executeFunctionRaceAnalysis(data):
    races = data['race'].unique()

    for race in races:
        race_data = data[data['race'] == race]
        race_name = constants.race_mapping.get(race, f"Codice {race}")
        shapAnalysis(race_data, target, constants.features, f"Etnia: {race_name}")

def executeFunctionGeographyAnalysis(data):
    states = data['geography'].unique()

    for state in states:
        geographyData = data[data['geography'] == state]
        state_name = constants.geography_mapping.get(state, f"Codice {state}")
        shapAnalysis(geographyData, target, constants.features, f"Zona: {state_name}")

def executeFunctionMarstAnalysis(data):
    mrst = data['marst'].unique()

    for mrt in mrst:
        mrst_data = data[data['marst'] == mrt]
        marital_status = constants.marst_mapping.get(mrt, f"Codice {mrt}")
        shapAnalysis(mrst_data, target, constants.features, f"Stato civile: {marital_status}")
