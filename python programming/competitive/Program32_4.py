import schedule
import time
import shutil
import sys
import os 

def Copy(DirectoryName,CopyDirectoryName):

    Time = time.strftime("%Y-%m-%d_%I-%M-%S %p")

    Ret1 = False 

    Ret1 = os.path.exists(DirectoryName)

    if Ret1 == False:
        print("File not exists")
        return

    if (os.path.isdir(DirectoryName) == False):
        print("No such directory")
        return

    Ret2 = False

    Ret2 = os.path.exists(CopyDirectoryName)

    if Ret2 == False:
        print("Given directory not exist")
        return

    if (os.path.isdir(CopyDirectoryName) == False):
        os.mkdir(CopyDirectoryName)

    for FolderName , SubFolder , FileName in os.walk(DirectoryName):
        for Fname in FileName:
            print(Fname)
            if (Fname.endswith(".txt")):

                try:

                    Path = os.path.join(FolderName,Fname)
                        
                    shutil.copy(Path,CopyDirectoryName)

                    fobj = open("LogFile.txt","a")

                    fobj.write(f"Copied at : {Time} \n")

                    fobj.write(f"Filename {Path}")

                    fobj.close()

                except Exception as eobj:
                    print(eobj)


def main():

    SourceDirectoryName = sys.argv[1]

    CopyDirectoryName = sys.argv[2]

    schedule.every(10).seconds.do(Copy,SourceDirectoryName,CopyDirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()