def CheckPerfect(Num):

    count = 0

    for i in range(1,Num):
        if Num % i == 0:
            count = count + i 

    if count == Num:
        return True

    else:
        return False
        
def main():

    Value = int(input("Enter a number : "))

    Ret = CheckPerfect(Value)

    if Ret == True:
        print("Perfect Number")

    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()