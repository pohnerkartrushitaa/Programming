import schedule
import time
import datetime
import os
import sys

def Display(FileName):

    Ret = os.path.exists(FileName)  

    if Ret == False:
        print("File does not exists")
        return

    Size = os.path.getsize(FileName)

    if Size == 0:
        print("File is empty")
        return

    try:

            fobj = open(FileName,"r")

            Data = fobj.read()

            print(Data)

            fobj.close()

    except PermissionError as eobj:
        print("Permission denied")

    except OSError as sobj:
        print("File cannot be opened")


def main():

    ScanFileName = "Hello.txt"

    schedule.every(1).minutes.do(Display,ScanFileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()