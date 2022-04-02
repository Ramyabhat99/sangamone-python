number = int(input("Enter the number: "))

Sum = 0
Times = 0

Temp = number
while Temp > 0:
    Times = Times + 1
    Temp = Temp // 10

Temp = number
while Temp > 0:
    Reminder = Temp % 10
    Sum = Sum + (Reminder ** Times)
    Temp //= 10

if number == Sum:
           print("%d is armstrong " %number)
else:
           print("%d is not an armstrong" %number)

