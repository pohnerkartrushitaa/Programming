def NaturalNum(No):   # No = 5

    Add = 0

    for i in range(1,No+1):
        Add = Add + i    # 1. Add = 0 + 1 for i = 1   2. Add = 1 + 2 for i = 2  3. Add = 3 + 3 for i = 3  4. Add = 6 + 4 for i = 4  5. Add = 10 + 5 for i = 5  Add = 15
    
    return Add

def main():
    
    Value = int(input("Enter a number to : "))

    Ret = NaturalNum(Value)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()