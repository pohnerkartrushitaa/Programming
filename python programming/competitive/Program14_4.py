Minimum = lambda No1,No2 : No1 < No2


def main():
    Value1 = int(input("Enter number : "))

    Value2 = int(input("Enter number : "))

    Ret = Minimum(Value1,Value2)

    if Ret == True:
        print(f"{Value1} is lower than {Value2}")

    else:
        print(f"{Value2} is lower than {Value1}")

if __name__ == "__main__":
    main()