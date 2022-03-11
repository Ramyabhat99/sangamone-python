import random 
  
def otpgeneration():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    print ("Your 4 digit One Time Password is ")
    print (otp)


def otpgenerate():
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))
    print ("Your 6 digit One Time Password is ")
    print (otp)


def otpgen():
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))
    print ("Your 8 digit One Time Password is ")
    print (otp)


n1=int(input("Enter the number of otp "))
if(n1==4):
    otpgeneration()
elif(n1==6):
    otpgenerate()
else:
    otpgen()

