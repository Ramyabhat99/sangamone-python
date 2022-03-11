#generates random password
import random

upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case=upper_case.lower()
digits="0123456789"
symbols="/><;':}{]["
#to display characters of password intializing with different variable 
upper,lower,num,sym = True,True,True,False   #here this doesnt print symbols since value is false
pswrd = ""
if upper:
    pswrd += upper_case
if lower:
    pswrd += lower_case
if num:
    pswrd += digits
if sym:
    pswrd += symbols
length=8 #length of password
number_of_pswrd=4
for i in range(number_of_pswrd):
    password="".join(random.sample(pswrd,length)) #join joins the the iterable characters that are generated and sample will return randomly selection of items
    print(password)
