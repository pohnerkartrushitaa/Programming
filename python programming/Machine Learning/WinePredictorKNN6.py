import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler 


def MarvellousClassifier(DataPath):
    Border = "-"*30

    print(Border)
    print("Step 1 : Load the data from csv file ")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from dataset : ")
    print(df.head())
    print(Border)

    # Step 2 : Clean the dataset

    print(Border)
    print("Step 2 : Clean the dataset")
    print(Border) 

    df.dropna(inplace= True)


    print("Shape of dataset : ",df.shape)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(Border)

    # Step 3 : Separate Independent and Dependent variables

    print(Border)
    print("Step 3 : Separate Independent and Dependent variables")
    print(Border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : ",X.columns.tolist())
    print("Output colummns : Class")
    print(Border)

    # Step 4 : Split the dataset for training and testing

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train ,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state = 42, stratify = Y)

    print(Border)
    print("Details of training and testing")
    print("Shape of X_train : ",X_train.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_test : ",Y_test.shape)

    # Step 5 : Feature Scaling 

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)


    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)


    # Step 6 : Build the Model

    print(Border)
    print("Step 6 : Build the Model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors = 9)

    print("Classification model is trained")

    # Step 7 : Train the model 

    model = model.fit(X_train_scaled,Y_train)

    print(Border)
    print("Step 7 : Train the model")
    print(Border)

    print("Model training completed")

    print(Border)

    # Step 8 : Test the model

    print(Border)
    print("Step 8 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Model accuracy score : ",accuracy*100)

    


def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()