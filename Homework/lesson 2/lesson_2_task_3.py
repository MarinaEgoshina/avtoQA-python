import math

def square(sideSquare):
    numberSide = math.ceil(sideSquare)
    return numberSide*numberSide

getSquare = 2.1
print("Площадь квадрата:", square(getSquare))