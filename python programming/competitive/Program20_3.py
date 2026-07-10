import threading 

def ChkEven(Data):
    Sum = 0
    for No in Data:
        if ( No % 2 == 0 ):
            Sum = Sum + No
    global SumEven
    SumEven = Sum            

def ChkOdd(Data):
    Sum = 0
    for No in Data:
        if ( No % 2 != 0):
            Sum = Sum + No
    global SumOdd
    SumOdd = Sum 

def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter elements : ")
    for No in range(Size):
        No = int(input())
        Arr.append(No)

    EvenList = threading.Thread(target = ChkEven ,args =(Arr,))

    OddList = threading.Thread(target = ChkOdd ,args = (Arr,))

    EvenList.start()
    EvenList.join()

    OddList.start()
    OddList.join()

    print("Sum of Even number in list : ",SumEven)

    print("Sum of Odd number in list : ",SumOdd)

if __name__ == "__main__":
    main()