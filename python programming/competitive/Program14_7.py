Divisible = lambda No : (No % 5 == 0)

def main():
    Value = int(input("Enter number : "))

    Ret = Divisible(Value)

    if Ret == True:
        print(f"{Value} is divisible by 5 ")

    else:
        print(f"{Value} is not divisble by 5")

if __name__ == "__main__":
    main()