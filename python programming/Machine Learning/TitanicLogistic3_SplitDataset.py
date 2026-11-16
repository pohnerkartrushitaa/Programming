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

#   sTEP 3 : Split Data
#-------------------------------------------------------------------
#       Funtion Name : SplitData
#       Description : It performs Splitting activity
#       Input : DataFrame 
#       Output : 4 subset for training and testing
#       Author : Trushitaa Pohnerkar
#       Date : 16-Aug-2026
#--------------------------------------------------------------------

def SplitData(df):

    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Dataset splitting completed sucesfully")

    return X_train,X_test,Y_train,Y_test


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

    #   Step 3
    X_train,X_test,Y_train,Y_test = SplitData(df)



if __name__ == "__main__":
    main()