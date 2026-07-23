import sys
import os

def main():

    try:

        FileName = (sys.argv[1])

        Ret = os.path.exists(FileName)

        if Ret == True:
            print(f"{FileName} exists")

        else:
            print(f"{FileName} not exists")

    except Exception as eobj:
        print("File not found in directory")

if __name__ == "__main__":
    main()