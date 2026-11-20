#==============================================================
#   Required Python Packages 
#==============================================================

import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score

#==============================================================
#   Function Name : read_data
#   Description : Loads Fraudulent Transaction Detection dataset from a CSV
#                 file into a Pandas DataFrame and displays the
#                 first five records to verify successful loading.
#   Input : CSV file path
#   Output : Loaded Pandas DataFrame
#   Author : Trushitaa Pohnerkar
#   Date : 19-Nov-2026
#==============================================================

def read_data(data):
    df = pd.read_csv(data)

    print("Data loaded successfuly")

    print(df.head())

    return df 

def Preprocessdata(df):

    # Handle missing value for features

    df["TransactionAmount"] = df["TransactionAmount"].fillna(df["TransactionAmount"].median())
    df["TransactionHour"] = df["TransactionHour"].fillna(df["TransactionHour"].median())
    df["AccountAgeMonths"] = df["AccountAgeMonths"].fillna(df["AccountAgeMonths"].median())
    df["PreviousTransactions"] = df["PreviousTransactions"].fillna(df["PreviousTransactions"].median())
    df["LocationDifferenceKm"] = df["LocationDifferenceKm"].fillna(df["LocationDifferenceKm"].median())
    df["DeviceType"] = df["DeviceType"].fillna(df["DeviceType"].mode()[0])
    df["FailedLoginAttempts"] = df["FailedLoginAttempts"].fillna(df["FailedLoginAttempts"].median())

    # Handle missing value for labels
    df["Fraud"] = df["Fraud"].fillna(df["Fraud"].mode()[0])  # [0] give the first most frequent value

    print("Data Preprocessing Completed")

    return df

def SplitData(df):

    X = df.drop("Fraud", axis = 1)  # or X = df.drop(columns=["Fraud"])

    Y = df["Fraud"]
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    print("Data splitting completed successfuly")

    return X_train,X_test,Y_train,Y_test

def Scale(X_train,X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return X_train,X_test

def Trainmodel(X_train,Y_train):

    model_dt = DecisionTreeClassifier(random_state=42,max_depth=7)

    model_bc = BaggingClassifier(n_estimators=10,random_state=42)

    model_rfc = RandomForestClassifier(n_estimators=100,random_state=42)

    model_ada = AdaBoostClassifier(n_estimators=100)

    model_vc = VotingClassifier(
        estimators=[
            ("dt",model_dt),
            ("bc",model_bc),
            ("rfc",model_rfc),
            ("ada",model_ada)
        ],
        voting="hard"
    )

    model_dt.fit(X_train,Y_train)
    model_bc.fit(X_train,Y_train)
    model_rfc.fit(X_train,Y_train)
    model_ada.fit(X_train,Y_train)

    model_vc.fit(X_train,Y_train)

    print("Model trained successfuly")

    return model_dt,model_bc,model_rfc,model_ada,model_vc

def EvaluateModel(model_dt,model_bc,model_rfc,model_ada,model_vc,X_test,Y_test):

    Y_preddt = model_dt.predict(X_test)

    Y_predbc = model_bc.predict(X_test)

    Y_predrfc = model_rfc.predict(X_test)

    Y_predada = model_ada.predict(X_test)

    Y_predvc = model_vc.predict(X_test)

    #Accuracy 

    Accuracy_dt = accuracy_score(Y_test,Y_preddt)

    Accuracy_bc = accuracy_score(Y_test,Y_predbc)

    Accuracy_rfc = accuracy_score(Y_test,Y_predrfc)

    Accuracy_ada = accuracy_score(Y_test,Y_predada)

    Accuracy_vc = accuracy_score(Y_test,Y_predvc)  

    # Confusion Matrix

    confusionmatrix_dt = confusion_matrix(Y_test,Y_preddt)

    confusionmatrix_bc = confusion_matrix(Y_test,Y_predbc)

    confusionmatrix_rfc = confusion_matrix(Y_test,Y_predrfc)

    confusionmatrix_ada = confusion_matrix(Y_test,Y_predada)

    confusionmatrix_vc = confusion_matrix(Y_test,Y_predvc)

    # Precision score 

    Precisionscore_dt = precision_score(Y_test,Y_preddt)

    Precisionscore_bc = precision_score(Y_test,Y_predbc)

    Precisionscore_rfc = precision_score(Y_test,Y_predrfc)

    Precisionscore_ada = precision_score(Y_test,Y_predada)

    Precisionscore_vc = precision_score(Y_test,Y_predvc)

    # recall_score

    recallscore_dt = recall_score(Y_test,Y_preddt)

    recallscore_bc = recall_score(Y_test,Y_predbc)

    recallscore_rfc = recall_score(Y_test,Y_predrfc)

    recallscore_ada = recall_score(Y_test,Y_predada)

    recallscore_vc = recall_score(Y_test,Y_predvc)

    # F1_score 

    F1score_dt = f1_score(Y_test,Y_preddt)

    F1score_bc = f1_score(Y_test,Y_predbc)

    F1score_rfc = f1_score(Y_test,Y_predrfc)

    F1score_ada = f1_score(Y_test,Y_predada)

    F1score_vc = f1_score(Y_test,Y_predvc)


    # Decsion tree

    print("="*40)
    print("Decision Tree Classifier")
    print("="*40)
    print("Accuracy of Decision tree classifier : ",Accuracy_dt*100,"%")
    print("Confusion matrix of Decision tree classifier : ",confusionmatrix_dt)
    print("Precision score of Decision tree classifier : ",Precisionscore_dt)
    print("Recall Score of Decision tree classifier : ",recallscore_dt)
    print("F1 score of Decision tree classifier : ",F1score_dt)

    print("="*40)
    print("Bagging Classifier")
    print("="*40)
    print("Accuracy of Bagging Classifier : ",Accuracy_bc*100,"%")
    print("Confusion matrix of Bagging Classifier : ",confusionmatrix_bc)
    print("Precision score of Bagging Classifier : ",Precisionscore_bc)
    print("Recall Score of Bagging Classifier : ",recallscore_bc)
    print("F1 score of Bagging Classifier : ",F1score_bc)


    print("="*40)
    print("Random Forest Classifier")
    print("="*40)
    print("Accuracy of Random Forest Classifier : ",Accuracy_rfc*100,"%")
    print("Confusion matrix of Random Forest Classifier : ",confusionmatrix_rfc)
    print("Precision score of Random Forest Classifier : ",Precisionscore_rfc)
    print("Recall Score of Random Forest Classifier : ",recallscore_rfc)
    print("F1 score of Random Forest Classifier : ",F1score_rfc)


    print("="*40)
    print("AdaBoostClassifier")
    print("="*40)
    print("Accuracy of AdaBoostClassifier : ",Accuracy_ada*100,"%")
    print("Confusion matrix of AdaBoostClassifier : ",confusionmatrix_ada)
    print("Precision score of AdaBoostClassifier : ",Precisionscore_ada)
    print("Recall Score of AdaBoostClassifier : ",recallscore_ada)
    print("F1 score of AdaBoostClassifier : ",F1score_ada)

    print("="*40)
    print("Voting Classifier")
    print("="*40)
    print("Accuracy of Voting Classifier : ",Accuracy_vc*100,"%")
    print("Confusion matrix of Voting Classifier : ",confusionmatrix_vc)
    print("Precision score of Voting Classifier : ",Precisionscore_vc)
    print("Recall Score of Voting Classifier : ",recallscore_vc)
    print("F1 score of Voting Classifier : ",F1score_vc)


def main():

    data = "Fraudulent_Transaction_Detection.csv"

    df = read_data(data)

    cleandata = Preprocessdata(df)

    X_train,X_test,Y_train,Y_test = SplitData(cleandata)

    X_train,X_test = Scale(X_train,X_test)

    model_dt,model_bc,model_rfc,model_ada,model_vc = Trainmodel(X_train,Y_train)

    EvaluateModel(model_dt,model_bc,model_rfc,model_ada,model_vc,X_test,Y_test)



if __name__ == "__main__":
    main()


