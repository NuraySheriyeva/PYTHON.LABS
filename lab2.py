'''All EXAMPLES     BOOLEANS
-------------------------------------------
print(10 > 9)
print(10 == 9)
print(10 < 9)
-------------------------------------------
Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
------------------------------------------
Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
-------------------------------------------
Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
-------------------------------------------
The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
-------------------------------------------
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
-------------------------------------------
You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())
-------------------------------------------
Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
-------------------------------------------
Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
__________________________________________________________________
ALL EXERCICES 

print(5>3)  will be True
print(10>9) will be True
print(10==9) will be False
print(10<9) will be False
print(bool("abc")) will be True
print(bool(0)) will be False
__________________________________________________________________


ALL EEXAMPLES OPERATORS

print(10 + 5)
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
----------------------------------------------------------
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
----------------------------------------------------------
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)
----------------------------------------------------------
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
----------------------------------------------------------
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
----------------------------------------------------------
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is n
----------------------------------------------------------
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not
----------------------------------------------------------
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
----------------------------------------------------------
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR

_____________________________________________________________________
ALL EXERCICES 
x=5
x+=3
print(x) will be 8

to multiply print(10*5)

to divide print(10/2)

to check apples presence 
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!") will be Yes, apple is a fruit!

to check if not equal 
if 5 != 10:
    print(not equal) will be not equal

to make condition to do smth if at least one condition is True  will be OR 
_______________________________________________________________________


ALL EXAMPLES   LISTS

Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]
----------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist)

----------------------------------------------------------
Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
----------------------------------------------------------
Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
----------------------------------------------------------
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
----------------------------------------------------------
A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
----------------------------------------------------------
From Python's perspective, lists are defined as objects with the data type 'list':

<class 'list'>
----------------------------------------------------------
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
---------------------------------------
Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
---------------------------------------
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
---------------------------------------
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
---------------------------------------
This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
---------------------------------------
This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
---------------------------------------
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
---------------------------------------
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
------------------------------------
Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
--
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
--
Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
--
Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
--
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
------------------------------------------------
Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

Packing a tuple:

fruits = ("apple", "banana", "cherry")

Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
----------------------------------------------------------------------
Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

There are several ways to join two or more sets in Python.
♥The union() and update() methods joins all items from both sets.
♠The intersection() method keeps ONLY the duplicates.
♣The difference() method keeps the items from the first set that are not in the other set(s).
♦The symmetric_difference() method keeps all items EXCEPT the duplicates.
------------------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
---------------------------------------------------------------
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
----------------------------------------------------------------
Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
------------------------------------------------------------------
Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

Loop through the letters in the word "banana":

for x in "banana":
  print(x)

__________________________________________________________
'''
'''ALL EXERCICES 
------------------------------------
mylist = ['apple', 'banana', 'cherry']
print(mylist[1]) WILL BE BANANA

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2]) WILL BE BANANA

'List items cannot be removed after the list has been created.' WILL BE FALSE

Select the correct function for returning the number of items in a list:

thislist = ['apple', 'banana', 'cherry']
print(_____(thislist)) WILL BE LEN

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1]) will be cherry

Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(______) will be fruits[1]

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4]) will be 'banana', 'cherry', 'orange'

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[___]) will be [2:5]

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1]) will be banana

Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
______ = ______ will be fruits[0] = "kiwi"

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2]) will be mango

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1]) will be apple

Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
__________ will be fruits.append("orange")

Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
________ "lemon") will be fruits.insert(1,

What is a List method for removing list items? pop()

Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"] 
_________ will befruits.remove("banana")

What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist) will be ['apple', 'cherry']

What is a correct syntax for looping through the items of a list?
for x in ['apple', 'banana', 'cherry']:
  print(x)

Insert the missing part of the while loop below to loop through the items of a list.
mylist = ['apple', 'banana', 'cherry']
i = 0
_____ i < ____ (mylist): will be while & len
  print(mylist[i])
  i = i + 1

What is a correct syntax for looping through the items of a list?
[print(x) for x in ['apple', 'banana', 'cherry']]

Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
What will be the value of newlist? will be 'banana'

What is a correct syntax for sorting a list?
mylist.sort()

What is a correct syntax for making a copy of a list?
list2 = list1.copy()

What is a correct syntax for joining list1 and list2 into list3?
list3 = list1 + list2
------------------------------------
Which one of these is a tuple?
will be thistuple = ('apple', 'banana', 'cherry')

Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(_____) will be len(fruits))

You can access tuple items by referring to the index number, but what is the index number of the first item?
will be 0

Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(___) will be fruits[0]

You cannot change the items of a tuple, but there are workarounds. 
Which of the following suggestion will work?
Convert tuple into a list, change item, convert back into a tuple.

Which is a correct syntax to delete a tuple?
del mytuple

fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
What will be the value of y? will be banana

What is a correct syntax for looping through the items of a tuple?
for x in ('apple', 'banana', 'cherry'):
  print(x)

What is a correct syntax for joining tuple1 and tuple2 into tuple3?
tuple3 = tuple1 + tuple2
-----------------------------------
Which one of these is a set?
myset = {'apple', 'banana', 'cherry'}

Set items cannot be removed after the set has been created.
false

A set cannot have two items with the same value. True

You can access set items by referring to the index. False

What is a correct syntax for adding items to a set?
add()

What is a correct syntax for removing an item from a set?
remove()

What is a correct syntax for looping through the items of a set?
for x in {'apple', 'banana', 'cherry'}:
  print(x)

What is a correct syntax for joining set1 and set2 into set3?
set3 = set1.union(set2)
----------------------------------------
Which one of these is a dictionary?
x = {'type' : 'fruit', 'name' : 'banana'}

Dictionary items cannot be removed after the dictionary has been created.
false

A dictionary cannot have two keys with the same name.
true

You can access item values by referring to the key name.
true

Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

x = {'type' : 'fruit', 'name' : 'banana'}
What is a correct syntax for changing the type from fruit to berry?
x['type'] = 'berry'

Which one of these dictionary methods can be used to add items to a dictionary?
update()

What is a dictionary method for removing an item from a dictionary?
pop()

What is a correct syntax for looping through the values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'} will be 
for y in x.values():
  print(y)

looping through both keys and values
for y, z in x.items():
  print(y, z)

What is a correct syntax for making a copy of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}

What is a correct syntax for making a copy of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
will be y = x.copy()

a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
what will be a correct syntax for printing the name 'May'?
print(customers['c2']['name'])
-------------------------------------------------
What will be the result of the following code:
x = 5
y = 8
if x > y:
  print('Hello')
else:
  print('Welcome')<--
------------------------------------------------
Which statement is a correct syntax to break out of a loop?
break
------------------------------------------------
What will be the result of the following code:
for x in range(3):
  print(x)

0
1
2
---------------------------------------------
__________________________________________________________
'''

