import threading

def Sum(Data):
    Sum = 0
    for no in Data:
        Sum = Sum + no
    global Add
    Add = Sum
    
def Product(Data):
    Sum = 1 
    for no in Data:
        Sum = Sum * no 
    global Prod 
    Prod = Sum
    
def main():
    Arr = []
    Size = int(input("Enter number of elements : "))

    print("Enter number : ")
    for No in range(Size):
        No = int(input())
        Arr.append(No)

    print(Arr)

    t1 = threading.Thread(target = Sum ,args =(Arr,))

    t2 = threading.Thread(target = Product ,args = (Arr,))

    t1.start()
    t1.join()

    t2.start() 
    t2.join()

    print(f"Sum of {Arr} : ",Add)
    print(f"Product {Arr} : ",Prod)

if __name__ == "__main__":
    main()