import sys

def main():

    try:
        FileName = (sys.argv[1])

        fobj = open(FileName,"r")

        Count = len(fobj.readlines())

        print(Count)

        fobj.close()

    except Exception as eobj:
        print("File not found in directory")

if  __name__ == "__main__":
    main()