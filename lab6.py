import time
import math
import os as o

#to multiply all the numbers in a list
def multiply(list):
    prod=1
    for numbers in list:
        prod=prod*numbers
    return prod
    
list=[1,2,3,4,5]
result=multiply(list)
print("Result: ", result)
#function that accepts a string and calculate the number of upper case letters and lower case letters
def sum(s):
    up=0
    low=0
    for letter in s:
        if letter.isupper():
            up=up+1
        elif letter.islower():
            low=low+1
        else:
            continue
    return up, low

text="HelLo WorLd!"
big, little =sum(text)
print("Uppercase letters:", big, " Lowercase letters:", little)
#function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  
print(is_palindrome("hello")) 

#program that invoke square root function after specific milliseconds.
#Sample Input:
#25100
#2123
#Sample Output:
#Square root of 25100 after 2123 miliseconds is 158.42979517754858
def delays(num, delay):
    time.sleep(delay/1000)
    return math.sqrt(num)

num=int(input("Number: "))
delay=int(input("Delay: "))

result = delays(num, delay)
print(f"Square root of {num} after {delay} milliseconds.")
#program with builtin function that returns True if all elements of the tuple are true.
tuple = (True, True, True)

print(all(tuple))
#--------------------------------------------------------------------------------------------------------------------------------------

#program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

path = "C:\\Users\\Nuray\\OneDrive\\Desktop\\githowto\\repositories\\work"

if o.path.exists(path):
    print("Path exists!")

    if o.access(path, o.R_OK):
        print("readable.")
    else:
        print("NOT readable.")

    if o.access(path, o.W_OK):
        print("writable.")
    else:
        print("NOT writable.")

    if o.access(path, o.X_OK):
        print("executable.")
    else:
        print("NOT executable.")

else:
    print("Path does NOT exist.")

#program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
path = "C:\\Users\\Nuray\\OneDrive\\Desktop\\githowto\\repositories\\work"

if o.path.exists(path):
    print("Path exists!")

    #directory portion
    directory = o.path.dirname(path)
    print("Directory:", directory)

    #filename portion
    filename = o.path.basename(path)
    print("Filename:", filename)

else:
    print("Path does NOT exist.")
#program to count the number of lines in a text file.
file = open("my.txt", "r")
def count(file):
    lines=file.readlines()
    sum=len(lines)
    file.close()
    return sum

print("Number of lines:", count(file))

file = open("my.txt", "a")
def listing(list, file):
    for item in list:
        file.write(item+"\n")
    
    file.close()
    print("Everything added")

list = ["one", "two", "three"]
listing(list, file)
#program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os as o
folder="LETTERS"
o.makedirs(folder, exist_ok=True)

def gen():
    for i in range(65, 91):
        name= o.path.join(folder, chr(i) + ".txt")
        file= open(name, "w")
        file.write("sleep")
        file.close()
    print("Created")

gen()
#program to copy the contents of a file to another file
def copy(file, copycat):
    content=file.read()
    file.close()
    copycat.write(content)
    copycat.close()
    print("Copied and pasted")

file=open("my.txt", "r")
copycat=open("copy.txt", "w")
copy(file, copycat)
#program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

path = "C:\\Users\\Nuray\\OneDrive\\Desktop\\githowto\\repositories\\work"

if o.path.exists(path):
    print("Path exists!")

    if o.access(path, o.R_OK):
        print("readable.")
        if o.access(path, o.W_OK):
            print("writable.")
            o.remove(path)
            print("File deleted successfully!")
    else:
        print("NOT readable and NOT writable and IS NOT deleted.")

else:
    print("Path does NOT exist.")

'''

#open(filename, mode)
modes:
    r   read
    a   append
    w   write
    x   create

file handling:
    t   text mode
    b   binary mode
_________________________________________________________________________________________________
open()      opens file
read()      reads the content of the file. returns the whole text.
            f.read(5) - first 5 characters of the file
readline()  return one line. by writing it to times you can read 2 first lines
write()     adds new lines of text of choice

f=open("demofile.txt", "r")
for x in f:
print(x)        LOOP THROUGH TH E FILE LINE BY LINE

close()     closes the file. if you dont close it might not show 
_________________________________________________________________________________________________

new parameters for open():
"a"     append- will append to the end of the file
"w"     write- will overwrite any existing content
"x"     create- will create a file, returns error if the file already exists
_________________________________________________________________________________________________

deletes this file:

import os 
os.remove("demofile.txt")

check if the file exists: (if exists, returns True)

import os 
os.path.exists("demofile.txt") 

deletes entire folder: (you can only delete empty folders)
import os 
os.rmdir("myfolder")

'''
'''
try     lets you test a block of code for errors
except  lets you handle the error
else    lets you execute code when there is no error
finally lets you execute code, regardless of the result of the try-except blocks

You can define as many exception blocks as you want, e.g. 
if you want to execute a special block of code for a special kind of error:

Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong)
finally:
  print("Try-except is finished")

raise   is used to raise an exception

x=-1

if x<0:
raise Exception("Sowwy, 2 loww")


'''