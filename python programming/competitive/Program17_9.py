def ChkLen(no):
    return len(no)

def main():
    Value = input("Enter a number : ")

    Ret = ChkLen(Value)

    print(f"Number of Digit in {Value} : {Ret}")

if __name__ == "__main__":
    main()