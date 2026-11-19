import math
import numpy as np

def MarvellousEucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier():
    Border = "-"*30

    Data = [
        {'point': 'A','X': 1, 'Y':2,'label':'Red'},
        {'point': 'B','X': 2, 'Y':3,'label':'Red'},
        {'point': 'C','X': 3, 'Y':1,'label':'Blue'},
        {'point': 'D','X': 5, 'Y':6,'label':'Blue'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    new_point = {'X' : 3, 'Y' : 3}

    print("Distance of all points : ")
    print(Border)

    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_point)
        
    for d in Data:
        print(d)

    print(Border)

    Sorted_Data = sorted(Data, key = lambda item : item['distance'])

    print('Sorted Data : ')
    print(Border)

    for d in Sorted_Data:
        print(d)

    print(Border)

    K = 3

    nearest = Sorted_Data[:K]

    print(Border)
    print("Nearest 3 members are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(d)

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()