Largest = lambda No1,No2,No3:(
    "A" if No1>No2 and No1>No3 else
    "B" if No2>No1 and No2>No3 else
    "C")


def main():
    Value1 = int(input("Enter number : "))

    Value2 = int(input("Enter number : "))

    Value3 = int(input("Enter number : "))

    Ret = Largest(Value1,Value2,Value3)

    if Ret == "A":
        print(f"{Value1} is greater than {Value2} and {Value3}")

    elif Ret == "B":
        print(f"{Value2} is greater than {Value1} and {Value3}")
    
    else:
        print(f"{Value3} is greater than {Value1} and {Value2}")

if __name__ == "__main__":
    main()