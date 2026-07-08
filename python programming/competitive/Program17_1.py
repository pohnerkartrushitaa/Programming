from Arithmetic import Add,Sub,Mult,Div

def main():
    Value1 = int(input("Enter first number : "))

    Value2 = int(input("Enter second number : "))

    Ret1 = Add(Value1,Value2)

    Ret2 = Sub(Value1,Value2)

    Ret3 = Mult(Value1,Value2)

    Ret4 = Div(Value1,Value2)

    print(f"Addition of {Value1} and {Value2} is {Ret1}")

    print(f"Subtraction of {Value1} and {Value2} is {Ret2}")

    print(f"Multiplication of {Value1} and {Value2} is {Ret3}")

    print(f"Division of {Value1} and {Value2} is {Ret4}")

if __name__ == "__main__":
    main()
    