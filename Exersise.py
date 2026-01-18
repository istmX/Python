import time 

name = input('enter your name: ')

current_time = time.localtime()
hour = current_time.tm_hour

if hour < 12 :
    print('Good Morning 🌺',name)
elif hour < 17:
    print('Good afterNoon ☀🌻',name)
elif hour < 21:
    print('Good Evening 🌞',name)
else :
    print('Good night 🌙',name)