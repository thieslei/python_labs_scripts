### Level BASIC

### This script will:
# - Read the year you were born
# - Get current year
# - Based on this information it'll calc your age
#

# importing date class from datetime module
from datetime import date
  
# creating the date object of today's date
todays_date = date.today()

# fetching the current year, month and day of today
currentyear = todays_date.year

# getting the year you were born
yearyouborn = float(input('Please type which year were you born: '))

# calc your age
age = currentyear - yearyouborn

print (' ')
print ('#############################')
print (f'You are {age:.0f} years old.')
print ('#############################')
print (' ')



### Autor thieslei@gmail.com