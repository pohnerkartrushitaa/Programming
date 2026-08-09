import pandas as pd


############################
#  Step 1 : Load the dataset
############################

def main():

    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    print("First 5 records : ")   # First 5 records
    print(df.head())


    print("Last 5 records : ")    # Last 5 records 
    print(df.tail())


    print("Total number of rows and columns : ")  # Total number of rows and column
    print(df.shape)

    print("List of column names : ")              # List of columns names
    print(list(df.columns))

    print("Data type of each column : ")          # Data type of each column  
    print(df.dtypes)

if __name__ == "__main__":
    main()