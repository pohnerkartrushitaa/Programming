import sys
import os
import schedule
import datetime
import time

def ScanDirectory(DirectoryName):

    CurrentTime = time.ctime()

    TotalSubFolder = 0

    TotalFile = 0

    print("Directory Scanned : ",DirectoryName)

    for FolderName , SubFolder , FileName in os.walk(DirectoryName):
        for Subf in SubFolder:
            TotalSubFolder = TotalSubFolder + 1
            for Fname in FolderName: 
                TotalFile = TotalFile + 1

    print("Total Files : ",TotalFile)

    print("Total SubFolder : ",TotalSubFolder)

    print("Scan time : %s" %CurrentTime)


def main():

    DirectoryName = sys.argv[1]

    schedule.every(2).seconds.do(ScanDirectory,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()