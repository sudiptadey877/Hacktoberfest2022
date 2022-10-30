a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
print("press 1 for add\n")
print("press 2 for subtract\n")
print("press 3 for multiply\n")
print("press 4 for divide\n")
choice=int(input("enter your choice:"))
if(choice==1):
    print("additon is:",a+b)
elif(choice==2):
     print("subtarction is:",a-b)
elif(choice==3):
     print("multiplication is:",a*b)
elif(choice==4):
     print("division is:",a//b)
else:
    print("false choice")     

