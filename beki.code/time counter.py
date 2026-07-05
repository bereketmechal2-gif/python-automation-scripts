import time
my_time = int(input("Enter how many second do you want : "))
for x in range(my_time,-1,-1):
    second = x % 60
    minuet = int(x/60)%60
    hour = int(x/3600)%24
    day = int(x/86400)%7
    week = int(x/604800)%4
    month = int(x/2629800)%12
    year = int(x/31536000)
    print(f"{year:02}:{month:02}:{week:02}:{day:02}:{hour:02}:{minuet:02}:{second:02}" , end ="\r")
    time.sleep(1)
print("TIMES UP!!!!!")