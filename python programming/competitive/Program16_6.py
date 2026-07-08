def ChkEven(No):
    if No == 0:
        return "A"
    elif No % 2 == 0:
        return "B"
    else:
        return "C"

def main():
    Value = int(input("Enter a number : "))

    Ret = ChkEven(Value)

    if Ret == "A":
        print("Zero")
    elif Ret == "B":
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()