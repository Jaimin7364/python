import keyword

print("Hello world, \nthis is jaimin")
#for print hello world
print("hey there, this is print statement 2")
'''comment 
long comment '''
'''Variables
int n=5
string a="jaimin"
float b=5.5
boolian c=false/true
null d=none
'''
#string variable print karava mate
string = "jaimin" # here we can use any name of variable for string and aslo for intiger
name ="jaimin"
print(name)
#integer
roll_number =111
rn = roll_number #value of roll_number is assigned to rn so that both have same value
print(roll_number)
#floating number
pr =98.67
print(pr)
#boolean
is_student = True
print(is_student)
#data type variable check karva mate 
print(type(name))
#full sentence
print("My name is "+name+"and my roll number is ",roll_number)
'''here roll number is int so that we can not use + sign we can use coma
sign for the combine sentense'''
#print expressipns
print("My persantage has changed to",pr+1)
#print with seprators
print(name, roll_number, pr, is_student,sep="-")
#int - 100,-5,63
#float - 3.5,60.45
#complex - 1+2j, 60+250j
#string - "jaimin", "bhai"
'''
sequence data types
1.list - ex.sequnce of intigers [,2,3,4]
2.list - ex.sequnce of strings["jaimin","bhai"]
'''
'''
Acii and unicode values
A-Z=65-90
a-z=97-122
'''

#keywords of python
'''
keywords = keyword.kwlist #for print the list of keywords
print(keywords)


->list of keywords

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

'''
# print sum #for substraction we can use same thing

a = 5
b = 6
sum = a+b
print(sum)

'''

'''
#expression execution 

a,b = 5,6 #multiple variable assign karva mate 
txt = "@"
print(2*txt*3) #for print the @ 6 times

#string operations

A,B = "2",3
txt = "@"
print((A+txt)*B) #for print the 2@2@2@ 

'''

'''
#floor values

A,B = 5,2
print(A//B) #for print the floor value of 5/2 in this ans will be 2.5 but we wil get 2 as ans using //

# means that we can use it to get closest int value of the division

'''

'''
#modulus operator

A,B = -5,2
print(A%B) #for print the remainder of 5/2 in this ans will be 1

#but when we have -5 and 2 than we get 1 as ans , but when we have 5 and -2 than we get -1 as ans , then when we have -5 and -2 than we get 1 as ans

'''

'''
--->input in python

#1. string input

name = input("Enter your name: ")
print("Name is :"+name)

#2. integer input
age = int(input("Enter your age: "))
print("Age is :",age)  #for print int after any string we can use coma

#3. float input

percentage = float(input("Enter your percentage: "))

print("Percentage is :",percentage)

'''


'''
#conditional statements

#1. simple if statement
a,b = 5,2

if a>b:
    print("5 is greater than 2")
elif a==b:
    print("5 is equal to 2")
else:
    print("5 is less than 2")

#2. nested if statement
if a>b:
    if a==b:
        print("5 is equal to 2")
    else:
        print("5 is greater than 2")
else:
    print("5 is less than 2")

#3. if statement with logical operators

if a>b and a==b:
    print("5 is greater than 2 and 5 is equal to 2")
else:
    print("5 is less than 2")

'''

'''
#singlel line conditional statement -- ternary operator

food = input("Enter your favourite food: ")

eat = "Yes" if food=="Pizza" else "No"
print(eat)
-we can write also following

print("yes") if food=="Pizza" else print("no")

'''

'''
#2nd reet 

age = int(input("Enter your age: "))

vote = ("no","yes")[age>18] # here we will write right option at right side like yes and wrong at left side like no
print(vote)

sal = float(input("Enter your salary: "))
tax = sal*(0.1,0.2)[sal>10000] # here when sal is greater than 10000 than we will get 20% tax and when sal is less than 10000 than we will get 10% tax
print(tax)

'''

#type conversion #type casting
#type conversion ae auto mate thay che
#type casting ae manually thay che

#type conversion 
a= 2
b=2.5

sum = a+b
print(sum) #here we will get 4.5 as ans

#type casting
a= 2
b=2.5
c= int(b) #here we will get 2 as ans
sum = a+c
print(sum) #here we will get 4 as ans
