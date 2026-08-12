import pandas as pd 
import matplotlib.pyplot as plt

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    AssignmentCompleted  = (df["AssignmentsCompleted"])
    FinalResult  = (df["FinalResult"])

    plt.plot(
        AssignmentCompleted,
        FinalResult,
        alpha = 0.8,
    )
    plt.xlabel("AssignmentCompleted")
    plt.ylabel("FinalResult")
    plt.title("AssignmentCompleted Vs FinalResult")
    plt.show()

if __name__ == "__main__":
    main()