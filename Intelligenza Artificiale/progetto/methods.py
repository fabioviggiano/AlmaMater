# Importazione librerie
import pandas as pd

import methods
import constants
from constants import *

print(constants.messageStartInDecisionTree)

data = methods.readCSV()

if constants.executeSectorAnalysis:
    print(messageExecuteSectorAnalysis)

    # Group the filtered data based on defined column in costants
    data[constants.workSectors] = pd.cut(data[columnToExtract], bins=wageRanges)

    # Count the number of observations in each group
    wage_distribution = data[constants.workSectors].value_counts().sort_index()

    methods.plotWageDistribution(wage_distribution)

    # Filter by hourly wage
    df = data[(data[constants.firstDatasetFilter] >= 5) & (data[constants.firstDatasetFilter] <= 50)]

    male, female = methods.filterSex(df)

    methods.avgHrwageDiffBySector(male, female)
else:
    print(messageNotExecuteSectorAnalysis)

if constants.executeGlobalSpecificAnalysis:
    print(messageExecuteGlobalSpecificAnalysis)

    data = methods.doubleFiter(data)
    data = methods.insertFeature(data)

    if constants.maleFemaleAnalysis:
            methods.maleFemaleAnalysisFunction(data)

    #if constants.citizen_race_analysis:
    #        methods.citizenRaceAnalysisFunction(data)

    if constants.raceAnalysis:
        methods.raceAnalysisFunction(data)

    if constants.educAnalysis:
        methods.educAnalysisFunction(data)

    if constants.executeExplainer:
        methods.globalAnalysisFunction(data)
    else:
        print(messageNotExecuteGlobalSpecificAnalysis)

print(constants.messageEndInDecisionTree)
