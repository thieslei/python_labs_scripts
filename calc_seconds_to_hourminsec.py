### This script will:
# - Convert seconds, into hours, minutes and seconds.
#
# 
  
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
n = float(input('Please type the seconds you want to convert: '))
#n = 60
print (' ')
print ('###############################')
print('Convert to hh:mm:ss == ',(convert(n)))
#print (f'You are {age:.0f} years old.')
print ('###############################')
print (' ')


### Autor thieslei@gmail.com