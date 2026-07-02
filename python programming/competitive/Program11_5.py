def Palindrome(Num):
    Temp = Num
    Rev = 0
    while (Temp != 0 ): 
        Digit = Temp % 10
        Rev = Digit + Rev*10
        Temp = (int)(Temp / 10 )    # Is used to remove last Number 
    
    if Rev == Num:
        return True 
    else:
        return False
         
def main():

    Value = int(input("Enter a number : "))
    Ret = Palindrome(Value)

    if Ret == True:
        print("Palindrome")

    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()