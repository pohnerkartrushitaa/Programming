import threading

def Display(Data):
    for No in range(1,Data+1):
        print(No)
    

def RevDisplay(Data):
    for No in range(Data,0,-1):
        print(No)
    
def main():

    Thread1 = threading.Thread(target = Display  ,args =(50,))

    Thread2 = threading.Thread(target = RevDisplay ,args = (50,))

    print("Display number : ",)
    Thread1.start()
    Thread1.join()

    print("Display reverse : ",)
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()