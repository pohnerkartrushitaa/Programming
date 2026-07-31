import schedule
import sys
import os
import time
import datetime

def DeleteEmptyFile(DirectoryName):

    Time = time.strftime("%Y-%m-%d_%I-%M-%S %p")

    try:

        for FolderName , Subfolder , FileName in os.walk(DirectoryName):
            for Fname in FileName:

                FilePath = os.path.join(FolderName,Fname)
                Size = os.path.getsize(FilePath)

                if Size == 0:
                    os.remove(FilePath)

                    fobj = open("DeleteFileLog.txt","a")

                    fobj.write(f"Time : {Time}\n")

                    fobj.write(f"Deleted file path : {FilePath}\n")

                    fobj.close()

                else:
                    print("No empty file")

    except PermissionError as pobj:
        print(pobj)
            

def main():

    DirectoryName = sys.argv[1]

    schedule.every(1).hours.do(DeleteEmptyFile,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()