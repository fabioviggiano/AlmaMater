# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:57:38 2025

@author: cesaredarochapinto
@author: fabioviggiano
@author: francesacmazzetti
"""

# Importazione librerie
import pandas as pd
from PIL.ImageChops import constant
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import shap
import matplotlib.pyplot as plt
import seaborn as sns

import constants
import methods
from constants import executeMarstAnalysis
from methods import filterSex, shapAnalysis

print(constants.messageStartInDecisionTree)

# Load dataset
data = methods.readCSV()

if constants.executeSectorAnalysis:
    print(constants.messageExecuteSectorAnalysis)

    # Group the filtered data based on hourly wage ranges
    data['wage_group'] = pd.cut(data['hrwage'], bins=constants.wageRanges)

    # Count the number of observations in each group
    wage_distribution = data['wage_group'].value_counts().sort_index()

    # Plot the distribution
    plt.figure(figsize=(10, 6))
    wage_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Hourly Wage Distribution (hrwage > 50)')
    plt.xlabel('Hourly Wage Range')
    plt.ylabel('Number of Observations')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.boxplot(data['hrwage'])
    plt.title('Boxplot of Hourly Wage')
    plt.ylabel('Hourly Wage')
    plt.show()

    df = data[data['hrwage'] <= 50]

    # Filtra per sesso
    male, female = filterSex(data)

    # Calcola differenza media di `hrwage` per ogni settore
    differenze = {}
    for settore in ["Agriculture", "durables", "nondurables", "Transport", "Utilities", "Communications", "retailtrade",
                    "wholesaletrade", "finance", "SocArtOther", "Medical", "Education", "professional", "publicadmin",
                    "sumadj_ind", "manager", "business", "financialop", "computer", "architect", "scientist",
                    "socialworker", "postseceduc", "legaleduc", "artist", "lawyerphysician", "healthcare",
                    "healthsupport", "protective", "foodcare", "building", "sales", "officeadmin", "farmer",
                    "production", "transport"]:  # Sostituisci con la lista completa dei settori
        media_maschi = male[male[settore] == 1]['hrwage'].mean()
        media_femmine = female[female[settore] == 1]['hrwage'].mean()
        differenze[settore] = abs(media_maschi - media_femmine)

    # Ordina i settori per differenza decrescente
    differenze_ordinate = dict(sorted(differenze.items(), key=lambda item: item[1], reverse=True))

    # Mostra il settore con la maggiore differenza
    print("\n--- Settore con maggiore differenza:", max(differenze_ordinate, key=differenze_ordinate.get))
    print("\n--- Differenze per settore:", differenze_ordinate)
else:
    print(constants.messageNotExecuteSectorAnalysis)

dataSample = data.sample(n=25000, random_state=constants.randomState)

data = methods.threeFilters(dataSample)

data["geography"] = data.apply(methods.determineGeography, axis=1)

# Target e variabili predittive
target = ['hrwage']  # Puoi cambiare con il tuo target

# split train / test
X = data[constants.features]
y = data[constants.target].squeeze()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(constants.messageRandomForest)

# Model Random Forest
model = RandomForestRegressor(constants.nEstimator, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
print(f'\n--- R²: {r2_score(y_test, y_pred):.4f}')
print(f'\n--- MAE: {mean_absolute_error(y_test, y_pred):.4f}')

if constants.executeExplainer:
    print(constants.messageExecuteTreeExplainer)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    print(constants.messageXTestShape + len(X_test.shape))
    print(constants.messageLenShapValues + len(shap_values))

    # Grafico riepilogativo globale
    shap.summary_plot(shap_values, X_test, feature_names=constants.features)

    # Elabora grafico delle singole feature
    methods.shapDependencePlot(shap_values, X_test)

    # this part is not tested yet
    shap.force_plot(explainer.expected_value, shap_values[42], X_test.iloc[42])
else:
    print(constants.messageNotExecuteTreeExplainer)

# Analisi per sesso
if constants.maleFemaleAnalysis:
    methods.executeFunctionMaleFemaleAnalysis(data)

# Analisi per ogni gruppo cittadinanza
if constants.executeCitizenAnalysis:
    methods.executeFunctionCitizenAnalysis(data)

# Analisi per gruppo etnico
if constants.executeRaceAnalysis:
    methods.executeFunctionRaceAnalysis(data)

# Analisi per gruppo geografico
if constants.executeGeographyAnalysis:
    methods.executeFunctionGeographyAnalysis(data)

# Analisi per stato civile
if constants.executeMarstAnalysis:
    methods.executeFunctionMarstAnalysis(data)

print(constants.messageEndInDecisionTree)
