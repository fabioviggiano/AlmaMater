# Import libraries
import pandas as pd
import numpy as np
import shap
# import os
from matplotlib import pyplot as plt
from pandas.core.arrays.categorical import contains
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

# Other modules
import constants


# Dataset and filtering

def readCSV():
    try:
        data = pd.read_csv(constants.csvFilePath)
        if data.shape[0] > 0 and data.shape[1] > 0:
            print(constants.messageFileReadCorrectly)
            return data
        else:
            print(constants.messageFileNotReadCorrectly)
            return None
    except FileNotFoundError:
        print(constants.messageFileNotFound + {constants.csvFilePath})
        return None
    except Exception as e:
        print(f": {e}")
        return None


def doubleFiter(data):
    min_wage = 5
    max_wage = 50
    max_hours = 48
    production_filter = 1
    i=1

    data = data[
        (data[constants.firstDatasetFilter] >= min_wage) & (data[constants.firstDatasetFilter] <= max_wage)]
    print(f"{constants.messageFilter}{i} {constants.firstDatasetFilter}: {constants.messageDataDimension} {len(data)}")
    i = i+1

    data = data[data[constants.secondDatasetFilter].notna()]
    print(f"{constants.messageFilter}{i} {constants.secondDatasetFilter}: {constants.messageDataDimension} {len(data)}")
    i = i + 1

    data = data[data[constants.thirdDatasetFilter] <= max_hours]
    print(f"{constants.messageFilter}{i} {constants.thirdDatasetFilter}: {constants.messageDataDimension} {len(data)}")

    data = data[data[constants.production] == production_filter]

    print(f"\n--- Production filter: {len(data)}")

    print(constants.messageFinalRow + str(len(data)))

    return data


def insertFeature(data):
    # Adjust some feature before execution start

    # Grouping characteristic by geographical location
    data[constants.geography] = np.dot(data[constants.location], constants.location_weights)

    # Thanks to secondDatasetFilter, constants.union has no null values
    work_sector_mapping = {
        constants.workSectors[0]: 1,
        constants.workSectors[1]: 1,
        constants.workSectors[2]: 2,
        constants.workSectors[3]: 2,
        constants.workSectors[4]: 2,
        constants.workSectors[5]: 3,
        constants.workSectors[6]: 3,
        constants.workSectors[7]: 3,
        constants.workSectors[8]: 3,
        constants.workSectors[9]: 4,
        constants.workSectors[10]: 4,
        constants.workSectors[11]: 4,
        constants.workSectors[12]: 5,
        constants.workSectors[13]: 6,
        constants.workSectors[14]: 6,
        constants.workSectors[15]: 6,
        constants.workSectors[16]: 7,
        constants.workSectors[17]: 7,
        constants.workSectors[18]: 7,
        constants.workSectors[19]: 8,
        constants.workSectors[20]: 8,
        constants.workSectors[21]: 9,
        constants.workSectors[22]: 9,
        constants.workSectors[23]: 9,
        constants.workSectors[24]: 9,
        constants.workSectors[25]: 9,
        constants.workSectors[26]: 9,
        constants.workSectors[27]: 9,
        constants.workSectors[28]: 10,
        constants.workSectors[29]: 10,
        constants.workSectors[30]: 11,
        constants.workSectors[31]: 11,
        constants.workSectors[32]: 11,
        constants.workSectors[33]: 12,
        constants.workSectors[34]: 12,
        constants.workSectors[35]: 13,
        constants.workSectors[36]: 14,
    }

    data[constants.labor] = 0
    for sector, value in work_sector_mapping.items():
        data[constants.labor] += data[sector] * value

    # Grouping characteristic for full/part-time work
    data[constants.work_type] = data[constants.uhrswork].apply(lambda x: 1 if x <= 25 else 2)

    return data


# Returns df samples divided by genre
def filterSex(df):
    male = df[df[constants.sex] == 1]
    female = df[df[constants.sex] == 2]

    return male, female

# -----------------------------------------------

# Work sector analysis

def plotWageDistribution(data):
    data[constants.wage_group] = pd.cut(data[constants.columnToExtract], bins=constants.groupingColumn)
    wage_distribution = data[constants.wage_group].value_counts().sort_index()

    # Plot the distribution
    plt.figure(figsize=(10, 6))
    wage_distribution.plot(kind='bar', color='skyblue', edgecolor='black')

    plt.xlabel(f'{constants.columnToExtract} Range')
    plt.ylabel('Number of Observations')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.boxplot(data[constants.columnToExtract])
    plt.title(f'{constants.columnToExtract} Wage')
    plt.ylabel(f'{constants.columnToExtract}')
    plt.show()


def avgHrwageDiffBySector(male, female):
    # Average difference in 'hrwage' for each sector
    differences = {}

    for work_sector in constants.workSectors:
        male_mean = male[male[work_sector] == 1][constants.hrwage].mean()
        female_mean = female[female[work_sector] == 1][constants.hrwage].mean()
        differences[work_sector] = abs(male_mean - female_mean)

    # Sorting by decreasing difference
    orderly_differences = dict(sorted(differences.items(), key=lambda item: item[1], reverse=True))
    # (e.g., pairs ('Construction', 4.0) in dictionary 'differences', item[1] = 4.0)

    max_difference_sector = max(orderly_differences, key=orderly_differences.get)

    print(f'Sector with the largest difference: {max_difference_sector}')

    print(f'Differences by sector: {orderly_differences}')


# -----------------------------------------------

# Functions analysis - Random Tree
def select_model(X_train, y_train, model_desc):
    param = {
        'n_estimators': [100, 200, 500, 1000],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 5],
        'max_features': ['sqrt', 'log2', None]
    }

    grid_search = GridSearchCV(RandomForestRegressor(random_state=constants.randomState), param, cv=3, scoring='r2',
                               n_jobs=-1, error_score='raise')
    grid_search.fit(X_train, y_train)
    model = grid_search.best_estimator_
    print(f'Best parameters from Grid Search for {model_desc}: ', grid_search.best_params_)
    return model

    # random_search = RandomizedSearchCV(RandomForestRegressor(random_state=constants.random_state), param_distributions=param, n_iter=50, cv=3, scoring='r2', n_jobs=-1, random_state=constants.random_state)
    # random_search.fit(X_train, y_train)
    # model = random_search.best_estimator_
    # print('Best parameters from Random Search: ', random_search.best_params_, error_score='raise')

    # return model


def evaluate_model(model, X_test, y_test, model_desc):
    # Model Evaluation
    y_pred = model.predict(X_test)

    print(f'{model_desc} model: ')
    print(f'R²: {r2_score(y_test, y_pred):.4f}')
    print(f'MAE: {mean_absolute_error(y_test, y_pred):.4f}')
    print(f'MSE: {mean_squared_error(y_test, y_pred):.4f}')
    print(f'RMSE: {mean_squared_error(y_test, y_pred, squared=False):.4f}')


def executeRandomForestRegressor(data, features, model_desc):
    if data.empty:
        print(constants.messageDatasetEmpty)
        return None

    print(constants.messageDatasetIsNotEmpty)
    X = data[features]
    y = data[constants.target].squeeze()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=constants.randomState)

    model = select_model(X_train, y_train, model_desc)

    evaluate_model(model, X_test, y_test, model_desc)

    return X_train, X_test, model


def executeTreeExplainer(X_train, X_test, model, features, model_desc):
    print(constants.messageExecuteTreeExplainer)

    explainer = shap.TreeExplainer(model, X_train)
    shap_values = explainer(X_test)

    print(constants.messageXTestShape + str(X_test.shape))
    print(constants.messageLenShapValues + str(len(shap_values)))

    # Global summary graph
    shap.summary_plot(shap_values, X_test, feature_names=features, show=False)
    plt.title(f'SHAP Summary Plot - {model_desc}')
    plt.show()

    # Genre impact
    shap.dependence_plot(constants.sex, shap_values, X_test, feature_names=features)
    plt.title(f'SHAP Dependence Plot (Sex) - {model_desc}')
    plt.show()

    # Race impact
    shap.dependence_plot(constants.race, shap_values, X_test, feature_names=features, show=False)
    plt.title(f'SHAP Dependence Plot (Race) - {model_desc}')
    plt.show()

    # Citizenship impact
    shap.dependence_plot(constants.citizen, shap_values, X_test, feature_names=features, show=False)
    plt.title(f'SHAP Dependence Plot (Citizen) - {model_desc}')
    plt.show()

    # this part is not tested yet
    # shap.force_plot(explainer.expected_value, shap_values[42], X_test.iloc[42])


def shapAnalysis(data, model_desc):
    extended_features = constants.featuresColumns.copy()

    match model_desc:
        case desc if 'Male' in desc or 'Female' in desc:
            extended_features.extend(constants.features_plus_sex)
        case desc if 'Race' in desc:
            extended_features.extend(constants.features_plus_race)
        case desc if 'Education' in desc:
            extended_features.extend(constants.features_plus_education)
        case desc if 'Global' in desc:
            extended_features.extend(constants.features_plus_global)
        # case desc if 'Citizenship in desc'
        case _:
            print(f"No column extention for model_desc: {model_desc}")

    executeRandomForestRegressor(data, extended_features, model_desc)

# -----------------------------------------------

# Analysis

def maleFemaleAnalysisFunction(data):
    male_data = data[data[constants.sex] == 1]
    female_data = data[data[constants.sex] == 2]

    shapAnalysis(male_data, 'Male')
    shapAnalysis(female_data, 'Female')


'''
def citizenRaceAnalysisFunction(data):
        citizens = data[constants.citizenship].unique()

        for citizen in citizens:
            citizen_data = data[data[constants.citizenship] == citizen]
            shapAnalysis(citizen_data, f'Citizenship {citizen}')
'''


def raceAnalysisFunction(data):
    races = data[constants.race].unique()

    for race in races:
        race_data = data[data[constants.race] == race]
        shapAnalysis(race_data, f"Race:{race}")


def educAnalysisFunction(data):
    educations = data[constants.schooledu].unique()

    for education in educations:
        education_data = data[data[constants.schooledu] == education]
        shapAnalysis(education_data, f'Education:{education}')


# All dataset
def globalAnalysisFunction(data):
    shapAnalysis(data, f'Global analysis')
