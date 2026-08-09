import pandas as pd
import numpy as np 

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    AverageStudyHours = (df["StudyHours"].mean())

    print("Average Study Hours: ",AverageStudyHours)

    AverageAttendance = (df["Attendance"].mean())

    print("Average Attendance : ",AverageAttendance)

    MaxPrevScore = (df["PreviousScore"].max())

    print("Maximum PreviousScore : ",MaxPrevScore)

    MinSleepHours = (df["SleepHours"].min())

    print("Minimum SleepHours : ",MinSleepHours)

if __name__ == "__main__":
    main()