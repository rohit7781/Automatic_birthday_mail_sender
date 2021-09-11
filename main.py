#Please see Important Notice In read me file

import smtplib, ssl
import datetime as dt
import random

#Dictonary that contain date and month(DDM{if your birth month is between 1 to 9}, else : DDMM ) as key pair
# In value pair It has a list which contain Name and gmail of a friend as string
birthday = {
    '119':['Rohit','lyavc94@gmail.com'],
    '128':['Abhishek','abhi225@gmail.com'],
    '2612':['Raj','rajn5181@hotmail.com'],
    '2910': ['Raunak','rjk55@yahoo.com']
}


#random module and file reading , so we wish them a new message every year
b = ['Wishes\wish1.txt','Wishes\wish2.txt','Wishes\wish3.txt','Wishes\wish4.txt','Wishes\wish5.txt',]
a = random.choice(b)
with open(a) as f:
    wishtext = f.read()


# Date and time module
now = dt.datetime.now()  
month = now.month    #current month
day = now.day           #current date
val =  (str(day)+str(month))        #add as a string so we can compare with key pair of birthday dictonary

if val in birthday.keys():  
    #Email sending code starts here
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "Your own Email"          #provide your email as string
    receiver_email = birthday[val][1]
    password = "Your Own email Password"        #provide Your own mail passwoed as string
    message = wishtext

 
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:

        server.starttls(context=context)

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
else:
    print('There is no bithday today')
