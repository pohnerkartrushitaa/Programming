import schedule
import time
import datetime

def DisplayMonday():
    print("Start your weekly goals")

def DisplayWednesday():
    print("Review your weekly progress")

def DisplayFriday():
    print("Weekly work completed")

def main():

    schedule.every().monday.at("09:00:00").do(DisplayMonday)
    schedule.every().wednesday.at("17:00:00").do(DisplayWednesday)
    schedule.every().friday.at("18:00:00").do(DisplayFriday)

    while True:
        schedule.run_pending()
        time.sleep(100)

if __name__ == "__main__":
    main()