def ChkGreater(No1,No2):
    if No1 > No2:
        print(No1, " is Greater than ",No2)

    else:
        print(No2,"is Greater than No1 ",No1)


def Main():

    Value1=int(input("Enter a number "))

    Value2=int(input("Enter a number "))

    ChkGreater(Value1,Value2)


if __name__=="__main__":
    Main()