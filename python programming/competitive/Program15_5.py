from functools import reduce

Maximum = lambda No1,No2 : (No1 if No1>No2 else No2)

def main():
    Data = [10,12,41,53,89]

    Ret = reduce(Maximum,Data)

    print(Ret)

if __name__ == "__main__":
    main() 