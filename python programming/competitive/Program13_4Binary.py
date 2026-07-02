def Binary(Num):

    while (Num != 0):
        Binary = (int)(Num % 2)
        print(Binary,end="")
        Num = (int) (Num / 2)

def main():

    Value = int(input("Enter a number : "))
    Binary(Value)

if __name__ == "__main__":
    main()