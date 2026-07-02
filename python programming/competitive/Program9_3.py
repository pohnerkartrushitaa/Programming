def Square(Num):
    
    return Num*Num


def main():

    Value = int(input("Enter a number : "))

    Ret = Square(Value)

    print("Square is ",Ret)


if __name__=="__main__":
    main()
