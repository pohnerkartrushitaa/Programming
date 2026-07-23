import sys

def main():
    try:
        FileName = (sys.argv[1])

        fobj = open(FileName,"r")

        Word = (sys.argv[2])

        found = False

        for lines in fobj:

            words = lines.split()
            for str in words:
                if Word == str:
                    found = True 

        if found == True:
            print(f"{Word} is found in {FileName}")

        else:
            print(f"{Word} is not found in {FileName}")

        fobj.close()

    except Exception as eobj:
        print("File not found in directory")

if __name__ == "__main__":
    main()