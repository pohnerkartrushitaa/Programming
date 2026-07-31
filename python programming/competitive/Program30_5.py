import schedule
import time
import datetime
import sys

def File():
    FileName = (sys.argv[1])
    fobj = open(FileName,"a")

    time = str(datetime.datetime.now())

    fobj.write("Task executed at : " + time + "\n")

    fobj.close()

def main():

    schedule.every(5).minutes.do(File)

    while (True):
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()