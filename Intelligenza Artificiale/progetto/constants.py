csvFilePath = 'data/CurrentPopulationSurvey.csv'

executeSectorAnalysis = False
executeExplainer = False
executeGlobalSpecificAnalysis = True

maleFemaleAnalysis = False
citizenRaceAnalysis = False
raceAnalysis = False
educAnalysis = False
geoAnalysis = True

# Define the ranges for grouping hourly wage
wage_ranges = [0, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 100000]

# Target e variabili predittive
target = ['hrwage']  # Puoi cambiare con il tuo target
features = ["metro", "age", "potexp",
            "citizen"
    , "sch", "educ99", "schlcoll"
    , "inflate",
            "year"
            # --rimettile dopo    , "Agriculture",  "durables", "nondurables",  "Transport", "Utilities", "Communications", "retailtrade", "wholesaletrade", "finance", "SocArtOther",  "Medical", "Education", "professional", "publicadmin", "sumadj_ind", "manager", "business", "financialop", "computer", "architect", "scientist", "socialworker", "postseceduc", "legaleduc", "artist", "lawyerphysician", "healthcare", "healthsupport", "protective", "foodcare", "building", "sales", "officeadmin", "farmer",   "production", "transport"
    , "sex"
    , "relate", "hdwfcoh", "marst"  # not really the gender but very close to it
    , "race"  # not very usefull
    , "annhrs"
            # --rimettile dopo     ,"farm", "yrimmig", "nativity", "hispan", "uhrswork", "union"   --rimettile dopo
            # --rimettile dopo  , "northeast", "northcentral", "south", "west"
            # , "perconexp"#it is cheating
            ]

# CPSVariable

columnToExtract = 'hrwage'
groupingColumn = 'wage'

hrwage = 'hrwage'
sex = 'sex'
race = 'race'

workSectors = ["Agriculture", "durables", "nondurables", "Transport", "Utilities", "Communications", "retailtrade",
                    "wholesaletrade", "finance", "SocArtOther", "Medical", "Education", "professional", "publicadmin",
                    "sumadj_ind", "manager", "business", "financialop", "computer", "architect", "scientist",
                    "socialworker", "postseceduc", "legaleduc", "artist", "lawyerphysician", "healthcare",
                    "healthsupport", "protective", "foodcare", "building", "sales", "officeadmin", "farmer",
                    "production", "transport"]

# Users messages

messageRandomForest = "\n--- Model Random Forest ---"

messageStartAlberiDecisionali = "\n--- Alberi Decisionali | Avvio esecuzione ---"
messageEndAlberiDecisionali = '\n--- Alberi Decisionali | Fine esecuzione ---'

messageExecuteTreeExplainer = "\n--- Esecuzione Tree Explainer ---"

filteredRowMessageString = '\n--- Numero di righe nel dataset filtrato: '
finalRowMessageString = '\n--- Numero di righe nel dataset finale: '

messageFileReadCorrectly = '\n--- Il file è stato letto correttamente'
messageFileNotReadCorrectly = '\n Il file CSV è vuoto o non è stato letto correttamente.'

messageXTestShape = '\n X_test.shape'
messageLenShapValues = '\n len Shap Values'

nEstimator = 100
randomState = 42

sectorFilter = 'production'

# classwkr: classwkr_lbl
# Class of worker
# (Self-empl=10, Wage/salary, private sector=21, Wage/salary, government=24, Federal govt employee=25, State govt employee=27, Local govt employee=28, Unpaid family worker=29)

classWkr = [10, 21, 24, 25, 27, 28, 29]