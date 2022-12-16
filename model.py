import sklearn.preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

###################################################################################
############################ PREP DATA FOR MODELING ###############################
###################################################################################

def get_dumdum(df):
    '''
    Takes in a dataframe and creates dummy variables for each 
    categorical variable.
    '''
    
    cat_col = list(df.select_dtypes(exclude=np.number).columns)
    dummy_df = pd.get_dummies(df[cat_col], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)
    return df

def prep_for_model(train, validate, test, target, drivers):
    '''
    Takes in train, validate, and test data frames, the target variable, 
    and a list of the drivers/features we want to model
    It splits each dataframe into X (all variables but target variable) 
    and y (only target variable) for each data frame
    '''
    train = get_dumdum(train[drivers])
    validate = get_dumdum(validate[drivers])
    test = get_dumdum(test[drivers])
    
    drop_columns = list(train.select_dtypes(exclude=np.number).columns) + [target]

    X_train = train.drop(columns=drop_columns)
    y_train = train[target]

    X_validate = validate.drop(columns=drop_columns)
    y_validate = validate[target]

    X_test = test.drop(columns=drop_columns)
    y_test = test[target]

    return X_train, y_train, X_validate, y_validate, X_test, y_test


###################################################################################
################### MODEL EVALUATION ON TRAIN AND VALIDATE DATA ###################
###################################################################################


def decision_tree_results(X_train, y_train, X_validate, y_validate):
    '''
    Takes in train and validate data and returns decision tree model results
    '''
    # create classifier object
    clf = DecisionTreeClassifier(max_depth=4, random_state=27)

    #fit model on training data
    clf.fit(X_train, y_train)

    #print results
    print("Decision Tree")
    print(f"Train Accuracy: {clf.score(X_train, y_train):.2%}")
    print(f"Validate Accuracy: {clf.score(X_validate, y_validate):.2%}")
    print(f"Difference: {(clf.score(X_train, y_train)-clf.score(X_validate, y_validate)):.2%}")


def random_forest_results(X_train, y_train, X_validate, y_validate):
    '''
    Takes in train and validate data and returns random forest model results
    '''
    # create classifier object
    rf = RandomForestClassifier(max_depth=4, random_state=27)

    #fit model on training data
    rf.fit(X_train, y_train)

    #print results
    print('Random Forest')
    print(f"Train Accuracy: {rf.score(X_train, y_train):.2%}")
    print(f"Validate Accuracy: {rf.score(X_validate, y_validate):.2%}")
    print(f"Difference: {(rf.score(X_train, y_train)-rf.score(X_validate, y_validate)):.2%}")

def knn_results(X_train, y_train, X_validate, y_validate):
    '''
    Takes in train and validate data and returns knn model results
    '''
    # create classifier object
    knn = KNeighborsClassifier()

    #fit model on training data
    knn.fit(X_train, y_train)

    #print results
    print('KNN')
    print(f"Train Accuracy: {knn.score(X_train, y_train):.2%}")
    print(f"Validate Accuracy: {knn.score(X_validate, y_validate):.2%}")
    print(f"Difference: {(knn.score(X_train, y_train)-knn.score(X_validate, y_validate)):.2%}")

def log_results(X_train, y_train, X_validate, y_validate):
    '''
    Takes in train and validate data and returns logistic regression model results
    '''
    # create classifier object
    logit = LogisticRegression(random_state=27)

    #fit model on training data
    logit.fit(X_train, y_train)

    #print results
    print('Logistic Regression')
    print(f"Train Accuracy: {logit.score(X_train, y_train):.2%}")
    print(f"Validate Accuracy: {logit.score(X_validate, y_validate):.2%}")
    print(f"Difference: {(logit.score(X_train, y_train)-logit.score(X_validate, y_validate)):.2%}")

def best_model(X_train, y_train, X_test, y_test):
    '''
    Takes in train and test data and returns random forest model results
    '''
    # create classifier object
    rf = RandomForestClassifier(max_depth=4, random_state=27)

    #fit model on training data
    rf.fit(X_train, y_train)

    #run the best overall model on test data
    print('Best Model: Random Forest')
    print(f"Test Accuracy: {rf.score(X_test, y_test):.2%}")

def best_model_comparison(X_train, y_train, X_validate, y_validate, X_test, y_test):
    '''
    Takes in train, validate and test data and returns random forest model results
    '''
    # create classifier object
    rf = RandomForestClassifier(max_depth=4, random_state=27)

    #fit model on training data
    rf.fit(X_train, y_train)

    #print results
    print('Random Forest')
    print(f"Train Accuracy: {rf.score(X_train, y_train):.2%}")
    print(f"Validate Accuracy: {rf.score(X_validate, y_validate):.2%}")
    print(f"Test Accuracy: {rf.score(X_test, y_test):.2%}")