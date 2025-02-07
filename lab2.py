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

fkjk
sjidjsidj
__________________________________________________________

ALL EXERCICES 

mylist = ['apple', 'banana', 'cherry']
print(mylist[1]) WILL BE BANANA

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2]) WILL BE BANANA

'List items cannot be removed after the list has been created.' WILL BE FALSE

Select the correct function for returning the number of items in a list:

thislist = ['apple', 'banana', 'cherry']
print(_____(thislist)) WILL BE LEN
__________________________________________________________
'''

