import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

def main():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    StudyHours = (df["StudyHours"])

    plt.hist(
        StudyHours,
        edgecolor = "black",
        bins = 5,
        alpha = 0.8,
        rwidth = 0.9

    )

    plt.title("StudyHours Histogram")
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()