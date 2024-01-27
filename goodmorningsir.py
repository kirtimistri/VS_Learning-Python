#exercise 2 : good morning sir
import datetime
currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
   print('Good morning.')
elif 12 <= currentTime.hour < 18:
 print('Good afternoon.')
else:
 print('Good evening.')