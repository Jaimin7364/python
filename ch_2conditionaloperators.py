m=input("Enter your marks :") #for user input you should write input
m=int(m)#for conver user input into int data type bcz it will be in string value so you must convert it
print("your marks :",m)
if m>=85 and m<=100: #colone is must be present in if statement
 print("A grade")
elif m>=70 and m<85:
 print("B grade")
elif m>=50 and m<70:
 print("C grade")
elif m>=35 and m<50:
 print("D grade")
else :
 print("you are fail")