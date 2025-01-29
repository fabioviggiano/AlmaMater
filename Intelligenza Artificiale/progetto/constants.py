## CONSTANTS FILE

# Dataset path
csvFilePath = 'data/CurrentPopulationSurvey.csv'

# -----------------------------------------------

# Analysis Flag

executeSectorAnalysis = True
executeExplainer = True
executeGlobalSpecificAnalysis = True

# All related to 'executeGlobalSpecificAnalysis'
maleFemaleAnalysis = True
executeCitizenAnalysis = True
executeMarstAnalysis = True
executeGeographyAnalysis = True
executeRaceAnalysis = True

# -----------------------------------------------

# Random Trees parameters
nEstimator = 100
randomState = 42

# -----------------------------------------------

# Target e variabili predittive

target = ['hrwage']  # Or 'realhrwage' + feature 'inflate'

features = ["metro", "age", "potexp",
            "citizen"
    , "sch", "educ99", "schlcoll"
    , "inflate",
            "year"
            # --stiamo lavorando solo su production per limitare il tempo macchina    , "Agriculture",  "durables", "nondurables",  "Transport", "Utilities", "Communications", "retailtrade", "wholesaletrade", "finance", "SocArtOther",  "Medical", "Education", "professional", "publicadmin", "sumadj_ind", "manager", "business", "financialop", "computer", "architect", "scientist", "socialworker", "postseceduc", "legaleduc", "artist", "lawyerphysician", "healthcare", "healthsupport", "protective", "foodcare", "building", "sales", "officeadmin", "farmer",   "production", "transport"
    , "sex"
    , "relate", "hdwfcoh", "marst"  # not really the gender but very close to it
    , "race"
    , "annhrs"
            # no very usefull ,"farm", "yrimmig", "nativity", "hispan", "uhrswork", "union"
            # -raggruppate in geography  , "northeast", "northcentral", "south", "west"
    , "geography"
            # , "perconexp"#it is cheating
            ]


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
messageNotExecuteTreeExplainer =   '\n--- Not Executing Tree Explainer ---'

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

# Mappatura numerica -> significato
citizen_mapping = {
    1: "Cittadino",
    2: "Naturalizzato",
    3: "Non cittadino"
}

race_mapping = {
    1: "White non-Hispanic",
    2: "Black non-Hispanic",
    3: "Hispanic",
    4: "Other non-Hispanic"
}

marst_mapping = {
    1: "Married, spouse present",
    2: "Married, spouse absent",
    3: "Separated",
    4: "Divorced",
    5: "Widowed",
    6: "Never married"
}

geography_mapping = {
    1: "Northeast",
    2: "North Central",
    3: "South",
    4: "West",
    5: "Other/Unknown"
}
