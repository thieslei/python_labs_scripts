### Level BASIC

### This is hard password generator:
# It prints a password sugestion of 12 to 22 characteres
# Just run it and enjoy :) 
#
#

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
#characters = string.ascii_letters + string.digits
password =  "".join(choice(characters) for x in range(randint(12, 22)))
print (password)


### Created by thieslei@gmail.com