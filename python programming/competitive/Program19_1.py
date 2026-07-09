import sys

Square = lambda No : No ** 2 

def main():
    if(len(sys.argv)==2):
        Value = int(sys.argv[1])
        Ret = Square(Value)
        print(f"Power of {Value} is {Ret}")
    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()