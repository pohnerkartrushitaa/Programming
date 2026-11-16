import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from  sklearn.metrics import accuracy_score,confusion_matrix

# Step 1 : Data Loading

#============================================================
#
#   Fuction Name : Load Data
#   Description  : Load the data from CSV
#   Inupt        : Name of CSV File
#   Output       : Data Frame
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Data Loaded Successfully")
    print(df.head())

    return df

# Step 2 : Data Preprocessing

#============================================================
#
#   Fuction Name : PreprocessData
#   Description  : It performs Exploratory Data Analysis
#   Inupt        : Data Frame
#   Output       : Updated Data Frame
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors = "ignore"
    )

    # Handle Missing Values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode())

    # Convert Categorical to numeric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )


    print(df.head())

    print("Data Preprocessing Completed")

    return df

# Step 3 : Split Data

#============================================================
#
#   Fuction Name : SplitData
#   Description  : It performs Spliting activity
#   Inupt        : Data Frame
#   Output       : 4 Subset for training and testing
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def SplitData(df):
    X = df.drop("Survived", axis=1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        )

    print("Dataset spliting completed successfully")

    return X_train, X_test, Y_train, Y_test

# Step 4 : Model Training

#============================================================
#
#   Fuction Name : TrainModel
#   Description  : It performs model training
#   Inupt        : training features and labels
#   Output       : Trained Model
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train,Y_train)

    print("Model Trained Successfully")

    return model

# Step 5 : Evaluate Model

#============================================================
#
#   Fuction Name : EvaluateModel
#   Description  : It performs model testing
#   Inupt        : model,testing data[features,label]
#   Output       : none
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def EvaluateModel(model, X_test,Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy :",accuracy)

    print(confusion_matrix(Y_test,Y_pred))

# Step 5 : Evaluate Model

#============================================================
#
#   Fuction Name : PreserveModel
#   Description  : It performs model preservation into .pkl file
#   Inupt        : model
#   Output       : none
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved with name :",filename)

#============================================================
#
#   Fuction Name : main
#   Description  : Entry point funcrion
#   Inupt        : None
#   Output       : None
#   Author       : Niranjan Manoj Khatavkar
#   Date         : 16/08/2026
#
#============================================================

def main():
    # Step 1
    df = LoadData("MarvellousTitanicDataset.csv")

    #Step 2 
    df = PreprocessData(df)

    # Step 3
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step 4
    model = TrainModel(X_train, Y_train)

    # Step 5
    EvaluateModel(model, X_test,Y_test)

    # Step 6
    PreserveModel(model,"MarvellousTitanic.pkl")

if __name__ == "__main__":
    main()