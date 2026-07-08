def Display(No):
    for i in range(No):
        for j in range(No):
            print(" * ",end="")
        print()

def main():
    Size = 0
    Size = int(input("Enter a number : "))

    Display(Size)

if __name__ == "__main__":
    main()