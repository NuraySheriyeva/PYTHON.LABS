
import datetime
#Write a Python program to subtract five days from current date.
x=datetime.datetime.now()
day= int(x.strftime("%d"))
print(x.strftime("%Y %B"), day-5)
print("_____________________________")
#Write a Python program to print yesterday, today, tomorrow.
l=datetime.datetime.now()
days= int(l.strftime("%d"))
for i in range(-1,2):
    print(l.strftime("%Y %B"), days+i)
print("_____________________________")
#Write a Python program to drop microseconds from datetime.
z=datetime.datetime.now()
print(z.strftime("%Y-%m-%d %H-%M-%S"))
print(x.strftime("%x %X"))
print("_____________________________")
#Write a Python program to calculate two date difference in seconds.
date1 = datetime.datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime.datetime(2025, 2, 11, 12, 0, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print(int(seconds))





#Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(N + 1):
        yield i * i

gen = square_generator(5)

for square in gen:
    print(square)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even(num):
    for i in range(0,num):
        if i%2==0:
            yield i


numb=int(input("Enter: "))
gen=even(numb)

for i in gen:
    print(", ".join(map(str, gen)))
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def fourthree(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield 1
        else:
            continue


n=int(input("Enter n: "))
gen=forthree(n)

for i in gen: print(i)
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a,b):
        yield i*i

a=int(input("Enter a: "))
b=int(input("Enter b: "))
gen = squares(a,b)

for i in gen: print(i)
#Implement a generator that returns all numbers from (n) down to 0.
def down(c):
    for i in range(c, 0, -1):
        yield i
    
c=int(input("Enter c:"))
gen = down(c)

for i in gen: print(i)





import math 
#Write a Python program to convert degree to radian.
#first way
degree=15
p=math.pi
radian=degree*p/180
print(round(radian,6))
print(" ")
#second way
x=15
print(round(math.radians(x), 6))
print("_____________________________")
#Write a Python program to calculate the area of a trapezoid.
a=5
b=6
h=5
area=(a+b)*h/2
print(area)
print("_____________________________")
#Write a Python program to calculate the area of regular polygon.
sides=4
length=25
ct=1/math.tan(p/sides)
area=sides*pow(length, 2)*ct/4
print(math.floor(area))
print("_____________________________")
#Write a Python program to calculate the area of a parallelogram.
base=5
height=6
area=float(base*height)
print(area)
