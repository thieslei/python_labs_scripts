### Level BASIC

### This script will:
# - Read hours number
# - Return number of seconds
# - Write a function that converts hours into seconds.

num1 = float(input('Enter number of hours convert in seconds: '))

def hours(num1):
    calc = ((num1 * 60) * 60)
    print("The number of seconds in ", int(num1) , " hours is", int(calc))

hours(num1)


### Autor thieslei@gmail.com