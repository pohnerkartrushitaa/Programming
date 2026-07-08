def PrimeNum(no):
    count = 0 
    for i in range(1,no):
        if (no % i == 0):
            count = count + 1
    if count>1:
        return False
    else:
        return True

def main():
    Value = int(input("Enter a number : "))

    Ret = PrimeNum(Value)

    if Ret == False:
        print("Not Prime Number")

    else:
        print("Prime Number")

if __name__ == "__main__":
    main()