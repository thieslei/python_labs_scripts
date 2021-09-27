### Level BASIC

### This script will:
# - Read 2 notes
# - Calc the average
# - And show the results if it's pass/failed/summer school
# - if less than 5 = failed
# - if more than 5 e less than 6.9 = summer school
# - if more than 7 = passd

note1 = float(input('Please type your first note: '))
note2 = float(input('Please type your second note: '))
average = (note1 + note2) / 2

print (' ')
print ('#############################')
if average < 4.9:
    print (f'Your average note was {average}: FAILED')
elif average >= 5.0 and average <= 6.9:
    print (f'Your average note was {average}: SUMMER SCHOOL')
else:
    print (f'Your average note was {average}: PASS!!!')
print ('#############################')
print (' ')


### Autor thieslei@gmail.com