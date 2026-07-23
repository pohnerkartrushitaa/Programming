import sys

def main():
    try:
        FileName = (sys.argv[1])

        fobj = open(FileName,"r")

        Count = 0 

        for lines in fobj:
            Data = len(lines.split())
            Count = Count + Data

        print(Count)

        fobj.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()