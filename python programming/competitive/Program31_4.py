import schedule
import time
import datetime

def CreateLog():

    CurrentTime = time.strftime("_%d_%m_%Y_%H_%M_%S")

    Time = time.strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open(f"MarvellousLog{CurrentTime}.txt","w")

    fobj.write("Log file created successfully\n")

    fobj.write(f"Creation Time : {Time}")

    fobj.close()


def main():

    schedule.every(1).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()

