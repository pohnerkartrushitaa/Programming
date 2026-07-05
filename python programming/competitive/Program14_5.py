CheckEven = lambda No : (No % 2 == 0)

def main():
    Value = int(input("Enter number : "))


    Ret = CheckEven(Value)

    if Ret == True:
        print(f"{Value} is Even")

    else:
        print(f"{Value} is Odd")

if __name__ == "__main__":
    main()