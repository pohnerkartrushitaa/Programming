# Python ProcessSurvillence.py 2 MarvellousLog
# Python ProcessSurvillence.py Timeinterval FolderName 

# len(sys.argv) --> 3

# Python ProcessSurvillence.py --h

import psutil
import sys
import os 
import datetime
import time
import schedule

def PlatformSurvillance(FolderName):

    Border = "-"*60

    Ret = False

    Ret = os.path.exists(FolderName)
    
    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if (Ret == False):
            print("Unable to proceed as foldername is existing but its not directory")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for log file gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----Marvellous Platform Survillence System----")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------System Report--------\n")

    fobj.write("Number of active CPU cores : %s \n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n "%psutil.cpu_percent())
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("---------End of log file ------------")

    fobj.close()


def main():
    Border = "-"*60
    print(Border)
    print("----Marvellous Platform Survillence System----")
    print(Border)

    # --h and --u handling
    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h"  or sys.argv[1] == "--H" ):
            print("This automation script is used to perform")
            print("1 : It fetch the information of running proccessess")
            print("2 : It fetch information about the primary storage as RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch information about Microprocessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")


        elif (sys.argv[1] == "--u"  or sys.argv[1] == "--U" ):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_interval Folder_Name")
            print("Time_interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to proceed as there is no matching arguments")

    #Actual project code 
    elif (len(sys.argv) ==3 ):

        # print("CPU usage : ",psutil.cpu_percent())
        print("Schedular started succesfully")
        print("Press CTRL + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance,sys.argv[2])

        while (True):
            schedule.run_pending()
            time.sleep(1)
        

    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments not matching")
        print("Please use --h and --u for help and usage")


    print(Border)
    print("Thank you for using our automation System")
    print(Border)


if __name__ == "__main__":
    main()