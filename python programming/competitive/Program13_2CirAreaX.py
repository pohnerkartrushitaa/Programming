CircleArea = lambda R,PI=3.14 : PI * R * R 

def main():

    Radius = int(input("Enter Radius : "))

    Ret = CircleArea(Radius)

    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()