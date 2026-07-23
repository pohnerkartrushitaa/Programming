import sys

def main():
    try:
        FileName = (sys.argv[1])

        fobj = open(FileName,"r")

        SearchWord = (sys.argv[2])

        Count = 0 

        for lines in fobj:
            Words = lines.split()
            for str in Words:
                if SearchWord == str: 
                    Count = Count + 1 

        print(f"{SearchWord} appears {Count} times")

        fobj.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()