CheckOdd = lambda No : (No % 2 != 0)

def main():
    Value = int(input("Enter number : "))


    Ret = CheckOdd(Value)

    if Ret == True:
        print(f"{Value} is Odd")

    else:
        print(f"{Value} is Even")

if __name__ == "__main__":
    main()