def Display(No):
    for i in range(No):
        for j in range(No-i):
            print(" * ",end="")
        print()

def main():

    Size = int(input("Enter a number : "))

    Display(Size)

if __name__ == "__main__":
    main()