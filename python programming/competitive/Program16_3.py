import sys

def Add(No1,No2):
    return No1 + No2 

def main():
    Value1 = int(sys.argv[1])

    Value2 = int(sys.argv[2])

    Ret = Add(Value1,Value2)

    print(f"Addition is : ",Ret)

if __name__ == "__main__":
    main()