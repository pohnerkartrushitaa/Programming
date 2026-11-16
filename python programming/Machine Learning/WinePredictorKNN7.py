import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-" * 40

    ##########################################################
    # Step 1 : Load the Data set from csv file
    ##########################################################

    print(border)
    print("Step 1 : Load the Data set from csv file")
    print(border)

    # Data frame
    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset :")
    print(df.head())
    print(border)

    ##########################################################
    # Step 2 : Clean the Dataset
    ##########################################################

    print(border)
    print("Step 2 : Clean the Dataset")
    print(border)

    df.dropna(inplace=True)

    print("Shape of Dataset :",df.shape)
    print("Total records :",df.shape[0])
    print("Total Columns :",df.shape[1])

    print(border)

    ##########################################################
    # Step 3 : Separate independent and dependent variables 
    ##########################################################

    print(border)
    print("Step 3 : Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)
    
    print(border)
    print("Input Columns :",X.columns.tolist())
    print("Output Columns : Class")
    print(border)

    ##########################################################
    # Step 4 : Split the Dataset for training and testing 
    ##########################################################

    print(border)
    print("Step 4 : Split the Dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Details of training and testing data")

    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)

    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)

    print(border)

    ##########################################################
    # Step 5 : Feature Scaling 
    ##########################################################

    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling done")

    print(border)

    ##########################################################
    # Step 6 : Hyper parameter tuning 
    ##########################################################

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test,Y_pred)        

        accuracy_scores.append(accuracy)


    print("Accuracy report : ")

    for no in accuracy_scores:
        print(no)

    print(border)

    ##########################################################
    # Step 7 : Visualization
    ##########################################################

    print(border)
    print("Graphical Representation")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = "o")
    plt.title("K values vs Accuracy")
    plt.xlabel("K Values")
    plt.ylabel("Accuracy")

    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()