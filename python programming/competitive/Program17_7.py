def Display(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

def main():

    Size = int(input("Enter a number : "))

    Display(Size)

if __name__ == "__main__":
    main()