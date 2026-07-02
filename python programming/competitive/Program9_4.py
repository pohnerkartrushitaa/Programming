def Cube(Num):

    return Num*Num*Num

def main():

    Value=int(input("Enter a number : "))

    Ret = Cube(Value)

    print("Cube of ",Value," is :",Ret)


if __name__=="__main__":
    main()