import matplotlib.pyplot as plt 
import pandas as pd 

def main():

    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    PassStudyHours = (df["StudyHours"][df["FinalResult"]==1])

    FailStudyHours = (df["StudyHours"][df["FinalResult"]==0])

    PassPreviousScore = (df["PreviousScore"][df["FinalResult"]==1])

    FailPreviousScore = (df["PreviousScore"][df["FinalResult"]==0])


    plt.scatter(
        PassStudyHours,
        PassPreviousScore,
        marker = "o",
        edgecolors = "black",
        alpha = 0.8,
        s = 100,
        label = "Pass Student",
        c = "blue"
    )

    plt.scatter(
    FailStudyHours,
    FailPreviousScore,
    marker = "o",
    edgecolors = "black",
    alpha = 0.8,
    s = 100,
    label = "Fail Student", 
    c = "red"
    )

    plt.title("Study Hours Vs Previous Score")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()