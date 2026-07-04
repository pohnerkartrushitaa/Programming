def Multiplication(No):
    
    for i in range(1,11):
        Sum = No * i
        print(Sum)

def main():
    Value = int(input("Enter a number : "))

    Multiplication(Value)

if __name__ == "__main__":
    main()