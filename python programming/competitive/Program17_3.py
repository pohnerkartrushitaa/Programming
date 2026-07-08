def Fact(no):
    Fact = 1

    for no in range(no,0,-1):
        Fact = Fact * no
    
    return Fact

def main():
    Value = int(input("Enter a number : "))

    Ret = Fact(Value)

    print(f"Factorial of {Value} is {Ret}")

if __name__ == "__main__":
    main()