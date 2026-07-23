import sys 

def main():

    try:
        count = 0

        FileName = (sys.argv[1])

        fobj = open(FileName,"r")

        for lines in fobj:
            count = count + 1

        print(count)

        fobj.close()

    except Exception as eobj:
        print("File not found in directory")

if __name__ == "__main__":
    main()