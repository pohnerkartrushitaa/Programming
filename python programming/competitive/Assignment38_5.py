import numpy as np 
import pandas as pd 

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    Result = (df["FinalResult"])

    Pass = 0
    Fail = 0 

    for no in Result:
        if no == 1:
            Pass = Pass + 1
        else:
            Fail = Fail + 1

    print("Total Passed : ",Pass)
    print("Total failed : ",Fail)



    AvgStudyhours = (df["StudyHours"].mean())

    print("Average study hours : ",AvgStudyhours)

    PassStudyHours = (df["StudyHours"][df["FinalResult"]==1].mean())

    print("Average Study Hours of passed student : ",PassStudyHours)

    FailStudyHours = (df["StudyHours"][df["FinalResult"]==0].mean())

    print("Average Study Hours of failed student : ",FailStudyHours)

    if (PassStudyHours > FailStudyHours):
        print("Higher StudyHours are associated with a higher chance of passing.")
    else:
        print("Higher StudyHours are not associated with a higher chance of passing.")

    # Attendance

    AvgAttendance = (df["Attendance"].mean())

    print("Average Attendance : ",AvgAttendance)

    PassAttendance = (df["Attendance"][df["FinalResult"]==1].mean())

    print("Average Attendance of pass student : ",PassAttendance)

    FailAttendance = (df["Attendance"][df["FinalResult"]==0].mean())

    print("Average Attendance of failed student : ",FailAttendance)

    if (PassAttendance > FailAttendance):
        print("Higher Attendance is associated with a higher chance of passing.")
    else:
        print("Higher Attendance is not associated with a higher chance of passing.")


if __name__ == "__main__":
    main()