import schedule
import time 
import datetime
import os 
import sys

def Count(DirectoryName):

    Border = "-"*77

    Date = time.strftime("%d-%m-%Y")

    Time = time.strftime("%I-%M-%S %p")

    TotalFiles = 0

    for FolderName , SubFolder , FileName in os.walk(DirectoryName):
        for Fname in FileName:
            TotalFiles = TotalFiles + 1

    FileName = "DirectoryCountLog.txt"

    Path = os.path.join(FolderName,FileName)

    AbsolutePath = os.path.abspath(DirectoryName)

    fobj = open(Path,"a")

    fobj.write(f"Directory Path : {AbsolutePath}\n")

    fobj.write(f"Number of files : {TotalFiles}\n")

    fobj.write(f"Date : {Date}\n")

    fobj.write(f"Time : {Time}\n")

    fobj.write(Border+"\n")

    fobj.close()


def main():

    DirectoryName = sys.argv[1]

    schedule.every(5).minutes.do(Count,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()