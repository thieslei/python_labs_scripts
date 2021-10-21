### Level BASIC

### This script will:
# - Read 2 numbers (length + width)
# - Return the remainder from two numbers
# - There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.


num1 = float(input('pick a number: '))
num2 = float(input('pick second number: '))

def remainder(num1, num2):
    calc = num1 % num2
    print("The remainder number is = ", int(calc))

remainder(num1, num2)


### Autor thieslei@gmail.com