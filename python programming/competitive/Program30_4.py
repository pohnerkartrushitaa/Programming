import schedule
import time
import datetime

def Display():
    print("Namaskar!..")

def main():

    schedule.every().day.at("09:00").do(Display)

    while (True):
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()

