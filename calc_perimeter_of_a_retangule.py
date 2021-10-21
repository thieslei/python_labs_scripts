### Level BASIC

### This script will:
# - Read 2 numbers (length + width)
# - Return the perimeter of a retangule
# - Create a function that takes length and width and finds the perimeter of a rectangle.


num1 = float(input('Type a retangule length: '))
num2 = float(input('Type a retangule width: '))

def retangule_perimeter(num1, num2):
    calc = ((num1 + num2)*2)
    print("The retangule area is = ", int(calc))

retangule_perimeter(num1, num2)


### Autor thieslei@gmail.com