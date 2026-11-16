import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from  sklearn.metrics import accuracy_score,confusion_matrix

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
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()