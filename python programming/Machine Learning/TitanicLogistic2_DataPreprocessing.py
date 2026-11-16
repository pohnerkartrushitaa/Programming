import numpy as np 
import pandas as pd 
import joblib    # To preserve model

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1 : Load the dataset

#-------------------------------------------------------------------
#       Funtion Name : LoadData
#       Description : Load the data
#       Input : Name of CSV file 
#       Output : Data Frame
#       Author : Trushitaa Pohnerkar
#       Date : 16-Aug-2026
#--------------------------------------------------------------------


def LoadData(filename):
    df = pd.read_csv(filename)
    print("Data Loaded Sucesfully")
    print(df)
    return df


#   Step 2 : Data Preprocessing

#-------------------------------------------------------------------
#       Funtion Name : PreprocessData
#       Description : It performance data analysis
#       Input : DataFrame 
#       Output : Updated DataFrame
#       Author : Trushitaa Pohnerkar
#       Date : 16-Aug-2026
#--------------------------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors = "ignore"
    )

    # Handle missing values 
    df["Age"] = df["Age"].fillna(df["Age"].median())  # Replace the missing values of age with median
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())  
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Covert Categorical to numeric data

    df = pd.get_dummies(                   # Encoding
        df,
        columns = ["Embarked"],
        drop_first=True,
        dtype= int
    )

    print(df.head())

    print('Data Preprocessing completed')
    return df

#-------------------------------------------------------------------
#       Funtion Name : main
#       Description : Entry point funstion
#       Input : None 
#       Output : None
#       Author : Trushitaa Pohnerkar
#       Date : 16-Aug-2026
#--------------------------------------------------------------------
def main():
    #   Step 1 
    df = LoadData("MarvellousTitanicDataset.csv")

    #   Step 2 
    df = PreprocessData(df)



if __name__ == "__main__":
    main()