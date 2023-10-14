## CIRCLE AREA CALCULATOR BY TAKING INPUT RADIUS
from decimal import *
import math
def circle_area_calc():
    while True:
        number1 = input("Write your circle radius for area calculation down bellow:\n")
        if number1 == int or float:
            getcontext().prec = 5
            area = Decimal(math.pi) * Decimal(number1) **Decimal(2)
            print(f"Yours circle area is {area}")
            print("Print x to exit")
        elif number1 == "x":
            StopIteration
        else:
            raise SyntaxError
circle_area_calc()
