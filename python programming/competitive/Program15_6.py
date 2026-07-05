from functools import reduce 

Minimum = lambda No1,No2 : (No1 if No1<No2 else No2)

def main():
    Data = [10,12,41,53,89]

    RData = reduce(Minimum,Data)

    print(RData)

if __name__ == "__main__":
    main() 