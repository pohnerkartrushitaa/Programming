import pandas as pd 
import matplotlib.pyplot as plt

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    SleepHours  = (df["SleepHours"])
    FinalResult  = (df["FinalResult"])

    plt.plot(
        SleepHours,
        FinalResult,
        alpha = 0.8,
    )
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")
    plt.title("SleepHours Vs FinalResult")
    plt.show()

if __name__ == "__main__":
    main()