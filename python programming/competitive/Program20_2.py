import threading

def ChkEven(No):
    Sum = 0

    for i in range(1,No+1):
        if (No % i == 0):
            if (i % 2 == 0):
                Sum = Sum + i
    print("Sum of even factors : ",Sum)
            
def ChkOdd(No):
    Sum = 0

    for i in range(1,No+1):
        if ( No % i == 0):
            if ( i % 2 != 0):
                Sum = Sum + i
    print("Sum of odd factors : ",Sum)
            
def main():

    Value1 = int(input("Enter number : "))

    EvenFactor = threading.Thread(target = ChkEven ,args =(Value1,))

    Value2 = int(input("Enter number : "))

    OddFactor = threading.Thread(target = ChkOdd ,args = (Value2,))

    EvenFactor.start()
    EvenFactor.join()

    OddFactor.start()
    OddFactor.join()

if __name__ == "__main__":
    main()