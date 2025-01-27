# -*- coding: utf-8 -*-
import methods
from constants import *

# Importazione librerie
import pandas as pd
import methods

print(messageStartAlberiDecisionali)

data = methods.readCSV()

if executeSectorAnalysis:
    # Group the filtered data based on defined column in costants
    data[groupingColumn] = pd.cut(data[columnToExtract], bins=wage_ranges)

    # Count the number of observations in each group
    wage_distribution = data[groupingColumn].value_counts().sort_index()

    methods.plotWageDistribution(wage_distribution)

    # Filtra sotto stipendio trenta
    df = data[data[columnToExtract] <= 30]

    male, female = methods.filterSex(df)

    methods.avg_hrwage_diff_by_sector(male, female)

data = methods.doubleFiter(data)

if executeGlobalSpecificAnalysis:
    if maleFemaleAnalysis:
            methods.maleFemaleAnalysisFunction(data)

    if citizenRaceAnalysis:
            methods.citizenRaceAnalysisFnction(data)

    if raceAnalysis:
        methods.raceAnalysisFunction(data)

    if educAnalysis:
        methods.educAnalysisFunction(data)

if executeExplainer:
    model, xTest = methods.executeRandomForestRegressor(data)
    methods.executeTreeExplainer(model, xTest)

print(messageEndAlberiDecisionali)
