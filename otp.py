import random 

def otpgeneration():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    print ("Your One Time Password is ")
    print (otp)
otpgeneration()
