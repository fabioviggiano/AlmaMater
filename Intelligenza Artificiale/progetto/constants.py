## CONSTANTS FILE

# Dataset path
csvFilePath = 'data/CurrentPopulationSurvey.csv'

# -----------------------------------------------

# Analysis Flag
executeExplainer = False

executeSectorAnalysis = False # Related to 'workSectors'
executeGlobalSpecificAnalysis = True

# All related to 'executeGlobalSpecificAnalysis'
maleFemaleAnalysis = True
#citizenRaceAnalysis = False
raceAnalysis = False
educAnalysis = False
geoAnalysis = False

# -----------------------------------------------

# Random Trees parameters
nEstimator = 100
randomState = 42

# -----------------------------------------------

# CPSVariable

target = ['hrwage']  # Or 'realhrwage' + feature 'inflate'
# Ranges for grouping hourly wage
wageRanges = [0, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 100000]

featuresColumns = [
    'year',
    'age',
    'marst',
    'classwkr',
    'nativity',
    'union',
    'potexp',
    # Artificial features
    'geography',
    'labor',
    'work_type'
]

groupingColumn = wageRanges
columnToExtract = 'hrwage'

firstDatasetFilter = 'hrwage' # Necessary because is target feature (sample with measured 'hrwage')
secondDatasetFilter = 'nativity'
thirdDatasetFilter = 'uhrswork'

features_plus_sex = ['race', 'sch']
features_plus_race = ['sex', 'sch']
features_plus_education = ['sex', 'race']
features_plus_global = ['sex', 'race', 'sch']

hrwage = 'hrwage'
sex = 'sex'
race = 'race'
citizen = 'citizen'
schooledu = 'sch'
union = 'union'
uhrswork = 'uhrswork'
classwkr = 'classwkr'
geography = 'geography'
location = ['northeast', 'northcentral', 'south', 'west']
labor = 'labor'
work_type = 'work_type'
wage_group = 'wage_group'
schooledu = 'sch'
production = 'production'

location_weights=[1, 2, 3, 4]

workSectors = [
    # Agricultural and livestock sector
    'Agriculture',
    'farmer',
    # Medical and healthcare sector
    'Medical',
    'healthcare',
    'healthsupport',
    # educational and social sector
    'Education',
    'postseceduc',
    'legaleduc',
    'socialworker',
    # artistic and creative sector
    'architect',
    'artist',
    'SocArtOther',
    # legal and juridical sector
    'lawyerphysician',
    # professional and managerial sector
    'manager',
    'business',
    'professional',
    # commercial and sales sector
    'wholesaletrade',
    'sales',
    'retailtrade',
    # technology and IT sector
    'computer',
    'scientist',
    # industry and production sector
    'durables',
    'nondurables',
    'Transport',
    'production',
    'transport',
    'building',
    'constructextractinstall',
    # public and administrative sector
    'publicadmin',
    'protective',
    # service sector
    'hotelsrestaurants',
    'foodcare',
    'officeadmin',
    # financial and banking sector
    'finance',
    'financialop',
    # communications sector
    'Communications',
    # energy sector and infrastructure
    'Utilities'
]

# -----------------------------------------------

# Users messages
messageRandomForest =           '\n--- Model Random Forest ---'

messageStartInDecisionTree =      '\n--- InDecision Trees | Starting execution ---'
messageEndInDecisionTree =        '\n--- InDecision Trees | Execution finished ---'

messageExecuteTreeExplainer =   '\n--- Executing Tree Explainer ---'

filteredRowMessageString =      '\n--- Number of rows in the filtered dataset: '
messageFinalRow = '\n--- Number of rows in the final dataset: '

messageFileReadCorrectly =      '\n--- The file has been read correctly'
messageFileNotReadCorrectly =   '\n--- Error: The CSV file is empty or was not read correctly'
messageFileNotFound =           '\n--- Error: CSV file not found at:  '
messageFileErrorWhileReading =  '\n--- An error occurred while reading the CSV file'

messageDatasetEmpty =           '\n--- The dataset is empty ---'
messageDatasetIsNotEmpty =      '\n--- The dataset for the current analysis is not empty ---'

messageXTestShape =             '\n--- X_test.shape: '
messageLenShapValues =          '\n--- Len Shap values: '

messageFilter = '\n--- Filter #'
messageDataDimension = ' - Data length: '

messageExecuteSectorAnalysis =      '\n--- SectorAnalysis'
messageNotExecuteSectorAnalysis =      '\n--- Sector Analysis not executed'

messageExecuteGlobalSpecificAnalysis =      '\n--- GlobalSpecificAnalysis'
messageNotExecuteGlobalSpecificAnalysis =      '\n--- Global Specific Analysis not executed'

# -----------------------------------------------
