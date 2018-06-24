
                                  TUPLES
                                  
#Q.1- Write a program to create a tuple with different data types and do the following operations. 
#Find the length of tuples.

tuple="apple",1,"orange",4,"banana"
print(tuple)
print(len(tuple))


#Q.2-Find largest and smallest elements of a tuples. 

tup1 = (12,65,87,-2,-10)
print("Largest element is :",max(tup1))
print("Smallestt element is :",min(tup1))


#Q.3- Write a program to find the product of all elements of a tuple. 

tup = (1,3,5,7,6)
product = tup[0]*tup[1]*tup[2]*tup[3]*tup[4]
print("The product of all the elements are :",product)

                                   SETS

#Q.1- Create two set using user defined values.
#1. Calculate difference between two sets.

my_set1=set()
my_set1.add(2)
my_set1.add(3)
my_set1.add(4)
print(my_set1)
my_set2=set()
my_set2.add(6)
my_set2.add(2)
my_set2.add(9)
print(my_set2)
set3 = my_set1 - my_set2  #difference
print(set3)

#2. Compare two sets.

seta = set(["green","blue"])
setb = set(["blue","yellow","green"])
issubset = seta <= setb
print(issubset)
issuperset = seta >= setb
print(issuperset)
comp = seta != setb
print(comp)

#3. Print the result of intersection of two sets.

my_set1=set()
my_set1.add(2)
my_set1.add(3)
my_set1.add(4)
print(my_set1)
my_set2=set()
my_set2.add(6)
my_set2.add(2)
my_set2.add(9)
print(my_set2)
set3 = my_set1 & my_set2  #intersection
print(set3)

                                 DICTIONARIES

#Q.1- Create a dictionary to store name and marks of 10 students by user input.

dictionary = {}
count = 0

while count < 10:
   name = input("Enter your name: ")
   mark = input("Enter your marks: ")
   if name not in dictionary:
       dictionary[name] = mark
       count = count + 1
   else:
       name = input("Enter a unique name: ")
       mark = input("Enter the marks ")
       if name not in dictionary:
          dictionary[name] = mark
          count = count + 1
print(dictionary)


#Q.2-Sort the dictionary created in previous question according to marks.

dictionary = {}
count = 0

while count < 3:
   name = input("Enter your name: ")
   mark = input("Enter your marks: ")
   if name not in dictionary:
       dictionary[name] = mark
       count = count + 1
   else:
       name = input("Enter a unique name: ")
       mark = input("Enter the marks ")
       if name not in dictionary:
          dictionary[name] = mark
          count = count + 1

print(dictionary)  #dict sorted by values that are marks
print(sorted(dictionary.items(), key=lambda t: t[1]))


#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI".
#Store count of every letter with the letter in a dictionary.

def count_dict(mystring):
    d = {}

    for ele in mystring:
        d[ele] = mystring.count(ele)

    for k in sorted(d):
        print (k + ': ' + str(d[k]))

mystring="MISSISSIPPI"
count_dict(mystring)

                                 
