# -> jem biji languages ma array hoy tem pyhton ma list hoy chhe .

marks = [100, 70, 75.5, 40.2, 80] # list of marks
print(marks)
print(type(marks)) # <class 'list'> aa ano type thase 
print(type(marks[0])) # 100 ama 100 no type int thase <class 'int'>
print(len(marks)) # 5 lenth of list

#-> python ma aapde list ma kai pan type ni value store kari shakie chhe. jyare biji languages ma ek j type ni value store kari shakie chhe. 

student=["Jaimin",18,"Rampura"] 
print(student)

#-> list ma aapde koi pan value ne cange kari shakie chhe. jyare string  ma value ne badli shakati nathi. 

student[1]=19
print(student)

# str = "Jaimin"
# str[1] = "k" # TypeError: 'str' object does not support item assignment

#List slicing

#-> list slicing ma aapde list ni value ne slice kari shakie chhe. jem ke sting ni substring hoy chhe. tem aapde aama pam koi pan value ne slice kari shakie chhe.jene sublist kehvay chhe.

marks = [100, 70, 75.5, 40.2, 80]
print(marks[1:4]) # 70, 75.5, 40.2

#-> list slicing ma aapde start index and end index pass kari shakie chhe. jyare start index thi end index sudhi ni value ne slice kari shakie chhe. jema last index ni value nathi aavti. jem ke 1:4 ma 1,2 ,3 ni value aave chhe. 4 ni value nathi aavti.

print(marks[:3]) # 100, 70, 75.5
print(marks[-3:-1]) # 75.5, 40.2 print thse etle ke 80 ne -1 malse and 100 ne -5 malse.

#List methods or functions here some basic functions are given but there are many more functions available in python.

lis = [1, 2, 3, 4, 5]

lis.append(6) # append function is used to add element at the end of the list.
print(lis) # 1, 2, 3, 4, 5, 6

lis.sort() # sort function is used to sort the list in ascending order.
print(lis) # 1, 2, 3, 4, 5, 6

lis.reverse() # reverse function is used to reverse the list.
print(lis) # 6, 5, 4, 3, 2, 1

lis.sort(reverse=True) # sort function is used to sort the list in descending order.
print(lis) # 6, 5, 4, 3, 2, 1

lis.insert(2, 10) # insert function is used to insert element at the given index.
print(lis) # 6, 5, 10, 4, 3, 2, 1

lis.remove(10) # remove function is used to remove the element from the list.
print(lis) # 6, 5, 4, 3, 2, 1

lis.pop() # pop function is used to remove the last element from the list.
print(lis) # 6, 5, 4, 3, 2

lis.clear() # clear function is used to remove all the elements from the list.
print(lis) # []


#-> Tuples

#-> Tuples are similar to list but the only difference is that tuples are immutable. It means that once the tuple is created, we cannot change the values of the tuple. Tuples are created using () brackets.

#-> Tuples are faster than list because tuples are immutable and list are mutable.

#-> Tuples are used when we want to store the data which should not be changed.

tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup)) # <class 'tuple'>

#-> Tuples slicing is similar to list slicing.

tup = (1, 2, 3, 4, 5)
print(tup[1:4]) # 2, 3, 4

#-> Tuples methods or functions

tup = (1, 2, 3, 4, 5)

print(tup.count(2)) # count function is used to count the number of times the element is present in the tuple.
print(tup.index(3)) # index function is used to find the index of the element in the tuple.
#-> function are the same for the tuples as list but the only difference is that tuples are immutable and list are mutable.



#=> Let's practicce 

#=> WAP to check if a list contains a palidrom of elements.

list1 = [1,2,2,1]
list2 = [1,2,3,4]

#let check list1 and list2 are palidrom or not. here we can see list1 is palidrom and list2 is not palidrom.

copy_list1 = list1.copy()
copy_list1.reverse()
if list1 == copy_list1:
    print("List1 is palidrom")
else:
    print("List1 is not palidrom")

copy_list2 = list2.copy()
copy_list2.reverse()
if list2 == copy_list2:
    print("List2 is palidrom")
else:
    print("List2 is not palidrom")



#-> Dictionary in python

#-> Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed. Dictionaries are written with curly brackets {} and they have keys and values.

#-> python ma dictionary oh jyare biji languages jem ke cpp and java ma map and hashmap hoy.

#-> Dictionary is used when we want to store the data in key-value pairs.

#-> Dictionary is mutable.

dict = {
    "name": "Jaimin",
    "age": 18,
    "city": "Rampura",
    "marks": [100, 70, 75.5, 40.2, 80],
}
print(dict)  
#-> we can search the value of the key in the dictionary using the key.

print(dict["name"]) # Jaimin
dict["age"] = 19 # we can change the value of the key in the dictionary.
print(dict["age"]) # 19

#-> we can aslo write 

print(dict.get("city")) # Rampura

#-> we can also write nested dictionary.

info = {
    "student1": {
        "name": "Jaimin",
        "age": 18,
        "city": "Rampura",
    },
    "student2": {
        "name": "Mahin",
        "age": 10,
        "city": "Rampura",
    }
}

print(info["student1"]["name"]) # Jaimin
print(info["student2"])
print(type(info)) # <class 'dict'>
print(len(info)) # 2

#-> we can convert the dictionary into the list.

print(list(info)) # ['student1', 'student2']
print(info.keys()) # dict_keys(['student1', 'student2'])
print(list(info.keys())) # ['student1', 'student2']
print(len(info.keys()))


#-> Dictionary methods or functions

myDict = {
    "name": "Jaimin",
    "age": 18,
    "city": "Rampura",
    "marks": [100, 70, 75.5, 40.2, 80],
}

print(myDict.get("name")) # Jaimin -> we can also print the name using print 

