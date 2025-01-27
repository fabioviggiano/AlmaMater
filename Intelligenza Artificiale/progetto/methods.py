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

def executeRandomForestRegressor(data):
    global xTest, model
    # split train / test - Target e variabili predittive
    X = data[features]
    y = data[target].squeeze()  # Puoi cambiare con il tuo target modificando la costante target
    # X_train_scaled = scaler.fit_transform(X)
    # X_test_scaled = scaler.transform(y)
    X_train, xTest, y_train, yTest = train_test_split(X, y, test_size=0.2, random_state=42)
    # Model Random Forest
    model = RandomForestRegressor(nEstimator, random_state=42)
    model.fit(X_train, y_train)
    # Model Evaluation
    y_pred = model.predict(xTest)
    print(f'R²: {r2_score(yTest, y_pred):.4f}')
    print(f'MAE: {mean_absolute_error(yTest, y_pred):.4f}')
    return model, xTest

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

def avg_hrwage_diff_by_sector(male, female):
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

def education_level_to_string(code):
    match code:
        case 1:
            return "No school"
        case 4:
            return "1st-4th grade"
        case 5:
            return "5th-8th grade"
        case 6:
            return "9th grade"
        case 7:
            return "10th grade"
        case 8:
            return "11th grade"
        case 9:
            return "12th grade"
        case 10:
            return "High school"
        case 11:
            return "Some college"
        case 13:
            return "Associate's degree"
        case 15:
            return "Bachelor's degree"
        case 16:
            return "Master's degree"
        case 17:
            return "Professional degree"
        case 18:
            return "Doctorate degree"
        case _:
            return "Unknown education level"

def doubleFiter(data):
    # va filtrato in questo modo?
    data = data[data[hrwage] <= 30]
    # maybe: if hrwage >30 then hrwage = 30.

    # Ottieni la dimensione del dataset filtrato
    lenRowFirstFiltering = len(data)

    print(f"Primo filtro: '{lenRowFirstFiltering}'")

    # Filtra il dataset per il settore 'production'
    data = data[data[sectorFilter] == 1]

    # Ottieni la dimensione del dataset filtrato
    lenRow = len(data)

    print(f"Secondo filtro: '{lenRow}'")

    print(finalRowMessageString + str(lenRow))

    return data

def maleFemaleAnalysisFunction(data):  # Divisione per genere
        male_data = data[data[sex] == 1]
        female_data = data[data[sex] == 2]

        # Analisi per maschi
        shap_analysis(male_data, target, features, "Maschi")

        # Analisi per femmine
        shap_analysis(female_data, target, features, "Femmine")

def citizenRaceAnalysisFnction(data):
        cittadini = data['citizen'].unique()

        # Analisi per ogni gruppo razziale
        for cittadino in cittadini:
            citizenData = data[data['citizen'] == cittadino]
            shap_analysis(citizenData, target, features, f'Cittadinanza {cittadino}')

def raceAnalysisFunction(data):    # Valori distinti di race
    races = data[constants.race].unique()

    # Analisi per ogni gruppo razziale
    for race in races:
        race_data = data[data[race] == race]
        shap_analysis(race_data, target, features, f"Razza:{race}")

def educAnalysisFunction(data):
    # Valori distinti di education
    educations = data['educ99'].unique()
    for edu in educations:
        edu_data = data[data['educ99'] == edu]
        shap_analysis(edu_data, target, features, f"Education:{edu_data}")