class Demo:
    def __init__(self):       # Constructor
        print("Inside constructor")

    def __del__(self):        # Destructor
        print("Inside destructor")

obj1= Demo()
obj2 = Demo()

print("End of application")