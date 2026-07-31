import sys
import time
import schedule

def Lunch():
    print("Lunch Time!")

def Wrap():
    print("Wrap Up!!")

def main():
    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:10").do(Wrap)

    while (True):
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()