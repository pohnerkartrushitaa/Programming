import sys

Multiplication = lambda No1,No2 : No1 * No2

def main():

    if(len(sys.argv) == 3):
    
        No1 = int(sys.argv[1])

        No2= int(sys.argv[2])

        Ret = Multiplication(No1,No2)

        print(f"Multiplication of {No1} and {No2} is : {Ret}")

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()