import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.model_selection import train_test_split


def Classifier(DataPath):

######################################################
# Step 1 : Load the data from csv file
######################################################

    Border = "-"*40

    print(Border)
    print("Step 1 : Load the data from csv file")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from dataset are : ")
    print(df.head())
    print(Border)

######################################################
# Step 2 : Clean the Data 
######################################################

    print(Border)
    print("Step 2 : Clean the Data ")
    print(Border)

    df.dropna(inplace=True)

    print("Shape of dataset : ",df.shape)
    print("Number of rows : ",df.shape[0])
    print("Number of columns : ",df.shape[1])
    print(Border)

######################################################
# Step 3 : Separate independent and dependent variables
######################################################

    print(Border)
    print("Step 3 : Separate independent and dependent variables")
    print(Border)

    X = df.drop(columns = "FinalResult")
    Y = df["FinalResult"]

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

######################################################
# Step 4 : Separate training and testing dataset
######################################################

    print(Border)
    print("Step 4 : Separate training and testing dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

######################################################
# Step 5 : Model training 
######################################################

    print(Border)
    print("Step 5 : Model training")
    print(Border)

    max_depth  = [1,3,None]

    for value in max_depth:

        print(Border)
        print(f"For max_depth = {value}")
        print(Border)

        model = DecisionTreeClassifier(max_depth=value,random_state=42)

        model = model.fit(X_train,Y_train)

        print("X_train shape : ",X_train.shape)
        print("X_test shape : ",X_test.shape)

        print("Y_train shape : ",Y_train.shape)
        print("Y_test shape : ",Y_test.shape)

######################################################
# Step 6 : Prediction
######################################################
        print(Border)
        print("Step 6 : Prediction")
        print(Border)

        Y_test_predict = model.predict(X_test)

        Y_train_predict = model.predict(X_train)

        print(Border)
        print("Expected answer : ",Y_test_predict)
        print("Predicted answer : ",Y_train_predict)

######################################################
# Step 7 : Accuracy Calculation
######################################################

        print(Border)
        print("Step 7 : Accuracy Calculation")
        print(Border)
        

        TestAccuracy = accuracy_score(Y_test,Y_test_predict)
        TrainAccuracy = accuracy_score(Y_train,Y_train_predict)

        print("Tesing Accuracy : ",TestAccuracy*100)
        print("Training Accuracy : ",TrainAccuracy*100)

        print(Border)

######################################################
# Step 8 : Confusion Matrix generation
######################################################

        print(Border)
        print("Step 8 : Confusion Matrix generation")
        print(Border)

        print("Confusion Matrix")
        print(confusion_matrix(Y_test,Y_test_predict))

    NewStudent = pd.DataFrame([[6,85,66,7,7]], 
                       columns = X.columns)

    print(Border)
    print("""Predict of StudyHours = 6,
        Attendance = 85,
        PreviousScore = 66,
        AssignmnetsCompleted = 7,
        SleepHours = 7 : """,model.predict(NewStudent))
    print(Border)

def main():

    Classifier("student_performance_ml.csv")

if __name__ == "__main__":
    main()

