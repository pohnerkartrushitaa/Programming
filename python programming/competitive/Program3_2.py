def Main():
    X=10

    print(type(X))
    print(id(X))

    Y=input("Enter a value:")
    from sys import getsizeof
    print(getsizeof(Y))

if __name__=="__main__":
    Main()