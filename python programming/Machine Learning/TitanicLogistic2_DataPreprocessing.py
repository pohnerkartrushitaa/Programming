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

if __name__ == "__main__":
    main()