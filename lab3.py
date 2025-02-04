# ------------------------CLASSES----------------------------
# Task 1
class StringHandler:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

# Task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

# Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Task 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Task 6
def filter_primes(numbers):
    return list(filter(lambda x: all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)) and x > 1, numbers))

#---------------------------FUNCTIONS---1----------------------
import math
import random

# Task 1
def grams_to_ounces(grams):
    print(28.3495231 * grams)

# Task 2
def fahrenheit_to_celsius(f):
    print( (5 / 9) * (f - 32))

# Task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):  # Loop through possible chicken counts
        rabbits = numheads - chickens  # Remaining animals are rabbits
        if (2 * chickens + 4 * rabbits) == numlegs:  # Check if legs match
            print(f"Chickens: {chickens}, Rabbits: {rabbits}")
            return
    print("No solution found")  # If no valid numbers are found


# Task 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

nums = list(map(int, input("Enter numbers: ").split()))
print(filter_prime(nums))

# Task 5
def permutations(s, step=0):
    if step == len(s):
        print("".join(s))
        return
    for i in range(step, len(s)):
        s_copy = list(s)
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        permutations(s_copy, step + 1)

permutations(list(input("Enter a string: ")))


# Task 6
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_sentence(input("Your sentence:")))

# Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = list(map(int, input("Enter numbers: ").split()))
print(has_33(nums))

# Task 8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 1:
            return True
    return False

nums = list(map(int, input("Enter numbers: ").split()))
print(spy_game(nums))

# Task 9
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)
radius=int(input("Enter:"))


print(sphere_volume(radius))

# Task 10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
lst= list(map(int, input("Enter numbers: ").split()))

print(unique_elements(lst))

# Task 11
def is_palindrome(word):
    return word == word[::-1]

# Task 12
def histogram(lst):
    for num in lst:
        print("*" * num)

# Task 13
def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

#---------------------------FUNCTIONS---2----------------------
#Task 1
def is_high_rated(movie):
    return movie["imdb"] > 5.5

#Task 2
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

#Task 3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

#Task 4
def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies) if movies else 0

#Task 5
def average_imdb_by_category(movies, category):
    category_movies = [movie["imdb"] for movie in movies if movie["category"] == category]
    return sum(category_movies) / len(category_movies) if category_movies else 0


