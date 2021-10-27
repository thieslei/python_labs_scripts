### Level BASIC

### This script will:
# - Receive an array of numbers
# - Show the second smallest and the second largest number

def array(list):
    list.sort()
    print ("The second smalest is ", list[1])
    print ("The second largest is ", list[-2])

array([0,10,69,2,14,22,15,100,50,51,54,3,9,67,88,92,72])