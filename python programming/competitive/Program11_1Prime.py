def Prime(No):
    count = 0
    for i in range(1,No):
        if No % i == 0:
            count = count + 1
    if count>=2:
        return True 
    else:
        return False

def main():
    Value = int(input("Enter a number : "))

    Ret = Prime(Value)

    if Ret  == True:
        print("Not prime number")
    else:
        print("Prime Number")

if __name__ == "__main__":
    main()