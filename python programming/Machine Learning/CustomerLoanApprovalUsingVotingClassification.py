#==============================================================
#   Required Python Packages 
#==============================================================

import pandas as pd 

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score , confusion_matrix

from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

#==============================================================
#   Function Name : read_data
#   Description : Loads customer loan approval dataset from a CSV
#                 file into a Pandas DataFrame and displays the
#                 first five records to verify successful loading.
#   Input : CSV file path
#   Output : Loaded Pandas DataFrame
#   Author : Trushitaa Pohnerkar
#   Date : 17-Nov-2026
#==============================================================

def read_data(data):
    df = pd.read_csv(data)

    print("Data loaded successfully")
    print(df.head())
    return df 

#==============================================================
#   Function Name : SplitData
#   Description : Separates independent features and target
#                 labels from the given dataset and divides
#                 the data into training and testing subsets
#                 using the train_test_split() function.
#   Input : Pandas DataFrame containing customer loan data
#   Output : X_train, X_test, Y_train, Y_test
#   Author : Trushitaa Pohnerkar
#   Date : 17-Nov-2026
#==============================================================

def SpliltData(DataFrame):

    X = DataFrame.drop("LoanApproved" , axis = 1)    # Or X = DataFrame.drop(columns=["LoanApproved"])

    Y = DataFrame["LoanApproved"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    print("Data splitting completed successfuly")

    return X_train,X_test,Y_train,Y_test

#==============================================================
#   Function Name : Scale
#   Description : Standardizes the training and testing feature
#                 data using StandardScaler to bring numerical
#                 features onto a common scale and improve
#                 model performance.
#   Input : X_train and X_test (Training and testing datasets)
#   Output : Scaled X_train and X_test datasets
#   Author : Trushitaa Pohnerkar
#   Date : 17-Nov-2026
#==============================================================

def Scale(X_train,X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.fit_transform(X_test)

    print("Feature scaling completed successfully")

    return X_train,X_test

#==============================================================
#   Function Name : TrainModel
#   Description : Initializes and trains individual machine
#                 learning models, including K-Nearest Neighbors,
#                 Decision Tree and Logistic Regression.
#                 Combines the trained estimators using Soft
#                 Voting and Hard Voting classifiers to improve
#                 prediction performance.
#   Input : Scaled training features (X_train) and target labels
#           (Y_train)
#   Output : Trained KNN, Decision Tree, Logistic Regression,
#            Soft Voting and Hard Voting classifier models
#   Author : Trushitaa Pohnerkar
#   Date : 17-Nov-2026
#==============================================================

def TrainModel(X_train,Y_train):
    model_knn = KNeighborsClassifier(n_neighbors=7)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_lr = LogisticRegression(max_iter=1000)

    model_knn.fit(X_train,Y_train)
    model_dt.fit(X_train,Y_train)
    model_lr.fit(X_train,Y_train)

    model1 = VotingClassifier(
        estimators=[
            ("KNN",model_knn),
            ("DT",model_dt),
            ("LR",model_lr)
        ],
        voting = "soft"
    )

    model2 = VotingClassifier(
        estimators=[
            ("KNN",model_knn),
            ("DT",model_dt),
            ("LR",model_lr)
        ],
        voting = "hard"
    )

    model1.fit(X_train,Y_train)
    model2.fit(X_train,Y_train)

    print("All machine learning models trained successfully")

    return model_knn,model_dt,model_lr,model1,model2

#==============================================================
#   Function Name : TestModel
#   Description : Evaluates the performance of trained machine
#                 learning models by generating predictions on
#                 unseen testing data and calculating accuracy
#                 scores for individual classifiers and both
#                 Soft Voting and Hard Voting classifiers.
#   Input : Trained ML models, scaled testing features (X_test)
#           and actual target labels (Y_test)
#   Output : Predicted labels and accuracy scores of all five
#            machine learning models.
#   Author : Trushitaa Pohnerkar
#   Date : 17-Nov-2026
#==============================================================

def TestModel(model_knn,model_dt,model_lr,model1,model2,X_test,Y_test):

    Y_predknn = model_knn.predict(X_test)

    Y_preddt = model_dt.predict(X_test)

    Y_predlr = model_lr.predict(X_test)


    Y_pred1 = model1.predict(X_test)

    Y_pred2 = model2.predict(X_test)


    accuracyknn = accuracy_score(Y_test,Y_predknn)
    accuracydt = accuracy_score(Y_test,Y_preddt)
    accuracylr = accuracy_score(Y_test,Y_predlr)


    accuracy1 = accuracy_score(Y_test,Y_pred1)

    accuracy2 = accuracy_score(Y_test,Y_pred2)


    print("\n========== MODEL ACCURACY REPORT ==========")

    print("KNN Accuracy            :", accuracyknn * 100, "%")
    print("Decision Tree Accuracy  :", accuracydt * 100, "%")
    print("Logistic Regression     :", accuracylr * 100, "%")
    print("Soft Voting Accuracy    :", accuracy1 * 100, "%")
    print("Hard Voting Accuracy    :", accuracy2 * 100, "%")

    print("==========================================")
#==============================================================
#   Function Name : main
#   Description : Acts as the entry point of the application
#                 and coordinates the complete machine learning
#                 workflow, including data loading, feature
#                 extraction, data splitting, feature scaling,
#                 model training and performance evaluation.
#   Input : None
#   Output : None (Executes the complete ML pipeline)
#   Author : Trushitaa Pohnerkar
#   Date : 17-Nov-2026
#==============================================================

def main():

    df = read_data("Customer_Loan_Approval.csv")

    X_train,X_test,Y_train,Y_test = SpliltData(df)

    Scaled_Xtrain,Scaled_Xtest = Scale(X_train,X_test)

    model_knn,model_dt,model_lr,model1,model2 = TrainModel(Scaled_Xtrain,Y_train)

    TestModel(model_knn,model_dt,model_lr,model1,model2,Scaled_Xtest,Y_test)


if __name__ == "__main__":
    main()


