import sys

def main():
    try:
        FileName = (sys.argv[1])

        fobj1 = open(FileName,"r")

        FileName = (sys.argv[2])

        fobj2 = open(FileName,"r")

        Data1 = fobj1.read()

        Data2 = fobj2.read()

        if (Data1 == Data2):
            print("Success")

        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()