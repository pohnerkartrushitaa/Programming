RectArea = lambda Num1,Num2 : Num1 * Num2

def main():

    Length = int(input("Enter length : "))

    Width = int(input("Enter Width : "))

    Ret = RectArea(Length,Width)

    print("Area of Rectangle is : ",Ret)

if __name__ == "__main__":
    main()