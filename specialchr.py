#a_string = "How are you ? Oh my God, you are bleeding! Let us go to the doctor quickly."

print("Enter string")
a_string = input()
alphanumeric = ""

for character in a_string:
    if character.isalnum():
        alphanumeric += character
print("The resultant statement is:  " +alphanumeric)
