def Display(No):
    return " * " * No

def main():
    Value = int(input("Enter a number : "))

    Ret= Display(Value)

    print(Ret)

if __name__ == "__main__":
    main()