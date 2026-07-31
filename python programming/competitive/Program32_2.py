import schedule
import time
import datetime
import sys 
import os


def Monitor(FileName):

    Border = "-"*75

    Date = time.strftime("%d-%m-%Y")

    Time = time.strftime("%H-%M-%S")

    Sizeoffile = os.path.getsize(FileName)

    LogFile = "FileSizeLog.txt"

    fobj = open(LogFile,"a")

    fobj.write(f"File size in bytes : {Sizeoffile} bytes\n")

    fobj.write(f"Date : {Date} \n")

    fobj.write(f"Time : {Time} \n")

    fobj.write(Border+"\n")

    fobj.close()

def main():

    MonitorFileName = sys.argv[1]

    Ret = False

    Ret = os.path.exists(MonitorFileName)

    if Ret == False:
        print("Path not exists")

    Ret = os.path.isfile(MonitorFileName)

    if Ret == False:
        print("Directory not found")


    schedule.every(30).seconds.do(Monitor,MonitorFileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()