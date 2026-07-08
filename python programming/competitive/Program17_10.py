def AddNum(no):
    temp = no
    Sum = 0
    while (no != 0):
        Digit = no % 10
        Sum = Sum + Digit
        no = int(no / 10)
    return Sum

def main():
    Value = int(input("Enter a number : "))

    Ret = AddNum(Value)

    print(f"Addition of {Value} is {Ret}")

if __name__ == "__main__":
    main()