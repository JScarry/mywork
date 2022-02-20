

months =("January", "February", "March", "April", "May", "June", "july",
"August", "September", "October", "November", "December")

summer = months[4:7]

for month in summer:
    print(month)


days = ('Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday')

weekend = days[5:7]

for days in weekend:
    print(days)




#currentDateTime = dt.datetime.today()
#print (currentDateTime)
#print ('day', currentDateTime.day)
#stringDate = currentDateTime.strftime('%A, %B %d, %Y')
#print(stringDate)
#stringDay = currentDateTime.strftime('%A')
#print(stringDay)



import datetime as dt #import datetime as dt #https://www.programiz.com/python-programming/datetime

#day = dt.date.today()
#stringDate = day.strftime('%A')
#print('Today is: ')
#print(stringDate)

dayNumber = dt.date.today().weekday() #using today method of the date class of datetime module,
                                        #Then adding the weekday() gives the week dayNumber 0-6
print ()
if dayNumber < 5: # if the day number is less than 5 it is a week day (0 Mon,1 Tue, 2 Wed, 3 Thu, 4 Fri)
    print ("Yes, unfortunately today is a weekday") #print this out if above is true
else:  # if ti is day 5 or 6 it is the weekend (5 Sat, 6 Sun)
    print ("It is the weekend, yay!") #if the first condition is false (not a week day) then print this out

#now = datetime.datetime.now()
#print ("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))


