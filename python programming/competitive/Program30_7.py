import shutil 
import datetime 
import time 
import schedule
import sys 
import os

def Backup():

    FileName = sys.argv[1]   

    DirectoryName = sys.argv[2]   #BackupFolder

    CurrentTime = time.strftime("%Y-%m-%d_%H-%M-%S")

    CopyFileName = ("Data%s.txt" %CurrentTime)

    Ret = False 

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("No such directory")

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("No such directory")

    Destination = os.path.join(DirectoryName,CopyFileName)

    shutil.copy(FileName,Destination)

    Destination = os.path.join(DirectoryName,"Backup_log.txt")  # (Folder,File)

    bobj = open(Destination,"a")

    bobj.write(f"Back up completed succesfully at : {CurrentTime}")


def main():
    Border = "-"*40
    print(Border)
    print("-------------Backup Process-------------")
    print(Border)

    schedule.every(1).hours.do(Backup)

    while (True):
        schedule.run_pending()
        time.sleep(100)

if __name__ == "__main__":
    main()