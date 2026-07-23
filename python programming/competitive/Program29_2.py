import sys

def main():
    try:
        FileName = (sys.argv[1])

        fobj = open(FileName,"r")

        Data = fobj.read()

        print(Data)

        fobj.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()