questions=[]
choices=[]
answers=[]
marks=[]

f1=open("QuestionBin_Medical_Hematology.txt","r")
for i in range(0,3,1):
    
    choice=[]
    info1=f1.readline()
    #print(info1)
    list1=info1.split("#")
    questions.append(list1[0])
    choice.append(list1[1])
    choice.append(list1[2])
    choice.append(list1[3])
    choice.append(list1[4])
    choices.append(choice)
    info2=list1[5]
    #print(info2)
    list2=info2.split(" ")
    answers.append(list2[1])
print("Your Quiz Program starts now")
for j in range(0,3,1):
    
    print(questions[j])
    for i in range(0,4,1):
        print(choices[j][i])
    response=input()
    if(response==answers[j]):
        marks.append(10)
    else:
        marks.append(0)
        print("The correct answer is",answers[j])

print("Your Marks is" ,marks)
print("Total Marks scored",sum(marks))





