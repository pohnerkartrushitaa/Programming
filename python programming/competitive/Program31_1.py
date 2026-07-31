import sys
import time
import schedule

def Display():

    Name = sys.argv[2]

    print(Name)

def main():

    Interval = int(sys.argv[1])

    if Interval > 0:

        schedule.every(Interval).seconds.do(Display)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Give time interval greater than zero")

if __name__ == "__main__":
    main()