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
#--------------------------------------------------------------------


def LoadData(filename):
    df = pd.read_csv(filename)
    return df

#-------------------------------------------------------------------
#       Funtion Name : main
#       Description : Entry point funstion
#       Input : Name of CSV file 
#       Output : Data Frame
#       Author : Trushitaa Pohnerkar
#       Date : 16-Aug-2026
#--------------------------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()