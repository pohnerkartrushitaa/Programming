import pandas as pd


############################
#  Step 1 : Load the dataset
############################

def main():

    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    print("Total number of students : ")
    print(len(df.index))                            # Give count of index

    FinalResult = (df["FinalResult"])

    TotalPassedStudents = 0
    TotalFailedStudents = 0

    for Pass in FinalResult:
        if Pass == 1:
            TotalPassedStudents = TotalPassedStudents + 1

    print("Total number of students Passed : ")
    print(TotalPassedStudents)

    for Fail in FinalResult:
        if Fail == 0:
            TotalFailedStudents = TotalFailedStudents + 1

    print("Total number of students Failed : ")
    print(TotalFailedStudents)

if __name__ == "__main__":
    main()