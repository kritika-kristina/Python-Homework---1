#Numbers

# Question 1
a = 400
b = 2
c = 4
d = 3
print((a+ (c - d)) / (b * b))

# Question 2
# Without Code -> 4 * (6+5) = 44
print(4 * (6+5))

# Without Code -> 4 * 6 + 5 = 29
print(4 * 6 + 5)

# Without Code -> 4 + 6 * 5 = 34
print(4 + 6 * 5)

#Question 3 - The type would be a float.

# Question 4 
#Square Root
import math

square_root = (math.sqrt(25))
print(square_root)

#Square 

a = 9
sqaure = a ** 2
print(sqaure)

#Strings

#Question 1
s = 'hello'
print(s[1])

#Question 2
st = 'hello'
print(st[::-1])

#Question 3

#Method 1:
str = 'hello'
print(str[4])

#Method 2:
print(str[-1])

#Lists
# Question 1 
list1 = [0,0,0]
print(list1)

list2 = [0,0]
list2.append(0)
print(list2)

list3 = [1,2]
list4 = [3,4,'hello']
list3.append(list4)
list3[2][2] ='goodbye'
print(list3)

list5 = [5,4,3,6,1]
list5.sort()
print(list5)

#Dictionaries

#Question 1

#d = {'simple_key': 'hello'}
#d['simple_key']

#Question 2 

#d1 = {'k1':{'k2':'hello'}}
#d1['k1']['k2']

#Question 3 

#d2 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
#d2['k1']['nest_key']['this is deep']

# Question 4 

#d3 = {'k1':[1,2,{'k2' :['this is tricky',{'tough':[1,2,['hello']]}]}]}
#d3['k1']

#Question 5 -> Can you sort a dictionary? Why or why not? 
# Ans -> No, you cannot. They are supposed to be unsorted and random.

# Tuples

#Question 1 - They major difference between a tuple and a list is that a tuple cannot be changed. 

#Question 2 

t = ('Monday','Tuesday','Wednesday')
print(t)

# Sets

#Question 1 -> They have unique elements

#Question 2 

list6 =[1,2,2,33,4,4,11,22,3,3,2]
x = set(list6)
print(x)

# Booleans
a = 2 
b = 3
# 2 > 3 --> False
print(a>b)
# 3 <= 2 --> False
print(b<=a)
# 3 == 2.0 --> False
c = 2.0
print(b==c)
# 3 == 3.0 --> True
d = 3.0
print(b==d)
# 4**0.5 != 2 --> False
e = 4
f = 0.5
print(e**f != a)

#Final Question

my_list = [1,2,[3,4]]
my_list2 = [1,2,{'k1',4}]
print(my_list [2][0] >= my_list2 [2]['k1'] )


