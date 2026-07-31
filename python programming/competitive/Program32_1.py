import schedule
import time
import datetime

def CreateFile():

    DateTime = time.strftime("_%d_%m_%Y_%H_%M_%S")

    CreationDate = time.strftime("%d-%m-%Y")

    CreationTime = time.strftime("%I-%M-%S %p")

    FileName = ("File%s.txt")%DateTime

    fobj = open(FileName,"w")

    fobj.write(f"Filename : {FileName} \n")

    fobj.write(f"Creation date : {CreationDate}\n")

    fobj.write(f"Creation time : {CreationTime}\n")

    fobj.close()

def main():

    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()