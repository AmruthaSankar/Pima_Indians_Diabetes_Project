  # Pima Indians Diabetes Project


Pima Indians Diabetes Database
------------------------------
### Input dataset
===============

https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

### Dataset details
===============

1: Pregnancies: Number of times pregnant

2: Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test.

3: BloodPressure: Diastolic blood pressure (mm Hg)

4: SkinThickness: Triceps skinfold thickness (mm)

5: Insulin: 2-Hour serum insulin (mu U/ml)

6: BMI: Body mass index (weight in kg/(height in m)²)

7: DiabetesPedigreeFunction: Diabetes pedigree function

8: Age: Age (years)

9: Outcome: Class variable (0 or 1) 268 of 768 are 1, the others are 0

### Steps
1: Importing the required libraries

2: Load the Dataset

3: EDA - Analysing size, shape, nullvalues, unique values, value counts in the dataset and checking correlation of output variable with 
   input variable and also plot the heatmap

4: Feature engineering -
   Missing value treatment,
   Categorical encoding,
   Outlier treatment

5: Train Test split

6: scale down - 
   It is done using standardScalar ,
   x_train scaled using fit-transform and
   x_test scaled using transform and after that we
   create pickle file of scale down using joblib


7: Apply all classification algorithms such as LogisticRegression, DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier, 
   GradientBooostingClassifier

8: check train and test accuracy of each algorithms

9: Hyper Parameter Tuning
   Hyperparameter tuning done in all algorithms to find the best model
   And print train accuracy,test accuracy and best parameter.
   I choose RandomForestClassifier as best model in the basis of accuracy and
   create pickle file of model using joblib.

  


