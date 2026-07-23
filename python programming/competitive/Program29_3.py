import sys

def main():

    try:

        FileName = (sys.argv[1])

        fobj1 = open(FileName,"r")

        Data = fobj1.read()

        FileName = (sys.argv[2])

        fobj2 = open(FileName,"w")

        fobj2.write(Data)

        print("Copied Successfuly")

        fobj1.close()
        fobj2.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()