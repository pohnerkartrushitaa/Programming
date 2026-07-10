import threading

def ChkSmall(Data):
    print("Thread id of thread1 : ",threading.get_ident())
    count = 0
    for ch in Data:
        if "a" <= ch <= "z":
            count = count + 1
    print("Number of small character : ",count)

def ChkCapital(Data):
    print("Thread id of thread2 : ",threading.get_ident())
    count = 0
    for ch in Data:
        if "A" <= ch <="Z":
            count = count + 1
    print("Number of Capital character : ",count)

def ChkDigit(Data):
    print("Thread id of thread3 : ",threading.get_ident())
    count = 0
    for ch in Data:
        if ch.isdigit():
            count = count + 1
    print("Number of digit : ",count)

def main():
    Value1 = input("Enter name : ")

    Value2 = input("Enter name : ")

    Value3 = input("Enter number : ")


    Small = threading.Thread(target = ChkSmall  ,args =(Value1,))

    print("Name of thread : ",Small.name)

    

    Capital = threading.Thread(target = ChkCapital ,args = (Value2,))

    print("Name of thread : ",Capital.name)

    

    Digit = threading.Thread(target = ChkDigit ,args = (Value3,))

    print("Name of thread : ",Digit.name)

    Small.start()
    Small.join()

    Capital.start()
    Capital.join()

    Digit.start()
    Digit.join()

if __name__ == "__main__":
    main()