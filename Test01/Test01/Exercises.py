# Exercise 1 (and Solution)

# Create a program that asks the user to enter their name and their age. Print out a 
# message addressed to them that tells them the year that they will turn 100 years old.
import time
year = int(time.strftime("%Y"))
name = input("Enter your name: ")
age = input("Enter your age: ")
year100 = year+100-int(age)
print("%s : you will be 100 years old in %d" % (name, year100))



# Extras:
# 1.Add on to the previous program by asking the user for another number and printing 
#   out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2.Print out that many copies of the previous message on separate lines. 
#   (Hint: the string "\n is the same as pressing the ENTER button)

import time
year = int(time.strftime("%Y"))
name = input("Enter your name: ")
age = input("Enter your age: ")
num = input("Number of times: ")
year100 = year+100-int(age)

for i in range(int(num)):
    print("%s : you will be 100 years old in %d\n" % (name, year100))


#------------------------------------------------------------------------------------------------

# Exercise 2 (and Solution)

# Ask the user for a number. Depending on whether the number is even or odd, print out an 
# appropriate message to the user. Hint: how does an even / odd number react differently
# when divided by 2?

num = input("Enter a number: ")
num = int(num)

if num % 2 == 0:
    print("%d is even" % (num))
else:
    print("%d is odd" % (num))

# Extras:
# 1.If the number is a multiple of 4, print out a different message.

num = input("Enter a number: ")
num = int(num)

if num % 4 == 0:
    print("%d is divisible by 4" % (num))
elif num % 2 == 0:
    print("%d is even" % (num))
else:
    print("%d is odd" % (num))


# 2.Ask the user for two numbers: one number to check (call it num) and one number to 
# divide by (check). If check divides evenly into num, tell that to the user. If not, 
# print a different appropriate message.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 % num2 == 0:
    print("%d is exactly divisible by %d" % (num1, num2))
else:
     print("%d is NOT exactly divisible by %d" % (num1, num2))

#------------------------------------------------------------------------------------------------
# Exercise 3 (and Solution)

# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num < 5:
        print(num)


# Extras:
# 1.Instead of printing the elements one by one, make a new list that has all the elements 
# less than 5 from this list in it and print out this new list.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
aSorted = sorted(a)
aDivisibleBy5 = [num for num in aSorted if num < 5]
print(aDivisibleBy5)

# 2.Write this in one line of Python.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([num for num in sorted(a) if num < 5])

# 3.Ask the user for a number and return a list that contains only elements from the 
# original list a that are smaller than that number given by the user.
n = int(input("Enter a number: "))
print([i for i in sorted(a) if i < n])

#------------------------------------------------------------------------------------------------
# Exercise 4 (and Solution)

# Create a program that asks the user for a number and then prints out a list of all the 
# divisors of that number. (If you don�t know what a divisor is, it is a number that divides 
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

n = int(input("Enter a number: "))

divisor = []

for i in range(1,n+1):
    if n % i == 0:
        divisor.append(i)

print(divisor)

#------------------------------------------------------------------------------------------------

# Exercise 5 (and Solution)

# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between 
# the lists (without duplicates). Make sure your program works on two lists of different sizes.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
for i in a:
    if i in b:
        common.append(i)

print(common)


# Extras:
# 1.Randomly generate two lists to test this
import random
a = random.sample(range(1,101), 15)
b = random.sample(range(1,101), 30)
common = []
for i in a:
    if i in b:
        common.append(i)

print(common)


# 2.Write this in one line of Python (don�t worry if you can�t figure this out at this point - we�ll get to it soon)
import random
a = random.sample(range(1,101), 15)
b = random.sample(range(1,101), 30)
common = [i for i in a if i in b]
print(sorted(a))
print(sorted(b))
print(sorted(common))

#------------------------------------------------------------------------------------------------
# Exercise 6 (and Solution)

# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)
strx = input("Enter a string: ")
if strx == strx[::-1]:
    print('"%s" is a palindrome' % strx)
else:
    print('"%s" is NOT a palindrome' % strx)

#------------------------------------------------------------------------------------------------
# Exercise 7 (and Solution)

# Let�s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even 
# elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]
print(b)

#------------------------------------------------------------------------------------------------

# Exercise 8 (and Solution)

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the players 
# want to start a new game)

# Remember the rules:
#   Rock beats scissors
#   Scissors beats paper
#   Paper beats rock
import random

dictRPS = { 'r':'Rock', 'p':'Paper', 's':'Scissors' }

dict = {    'rr':'draw', 'rp':'lose', 'rs':'win',
            'pr':'win',  'pp':'draw', 'ps':'lose',
            'sr':'lose', 'sp':'win',  'ss':'draw'
        }

n = 5
while n > 0:
    urps = input("Rock/Paper/Scissors ? (r/p/s): ")
    crps = "rps"[random.randint(0,2)]
    print("%s.. You %s." % (dictRPS[crps], dict[urps + crps]))
    n -= 1


#------------------------------------------------------------------------------------------------
# Exercise 9 (and Solution)

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
import random

x = random.randint(1,9)
ui = 'y'
c = 0

while ui.lower() != 'e':
    ui = input("Guess the number between 1 and 9   or 'e' to exit: ")
    if ui == 'e':
        print("You tried %d time(s) but did not get the number" % (c))
        break
    
    c+=1
    if int(ui) < x:
        print("Too Low !")
    elif int(ui) > x:
        print("Too High !")
    elif int(ui) == x:
        print("You got it in %d tries!" % (c))
        ui = 'e'
    
# Extras:
# Keep the game going until the user types �exit�
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


#------------------------------------------------------------------------------------------------
# Remove duplicates in a list

a = [2, 4, 2, 5, 3, 5, 6, 8, 5, 2]
print(a)
a = list(set(a))
print(a)


#------------------------------------------------------------------------------------------------

# Exercise 11 (and Solution)

# Ask the user for a number and determine whether the number is prime or not. (For those who 
# have forgotten, a prime number is a number that has no divisors.). 

x = int(input("Enter a number: "))

def isPrime(n):
    if n < 2: return False

    for i in range(2, int((n ** 0.5)-1)):
        if not n % i:
            return False
    return True

if isPrime(x):
    print("%d is a Prime Number" % (x))
else: 
    print("%d is NOT a Prime Number" % (x))

#------------------------------------------------------------------------------------------------
# Exercise 12 (and Solution)

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
# a new list of only the first and last elements of the given list. For practice, write this code 
# inside a function.

a = [5, 10, 15, 20, 25]

def firstLast(r):
    return [ r[0], r[-1] ]

print(firstLast(a))

#------------------------------------------------------------------------------------------------
# Fibonacci    
 

# Exercise 13 (and Solution)

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter 
# the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of 
# numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while n != 0:
        result.append(b)
        a, b = b, a+b
        n-=1
    return result

x = int(input("Enter how many Fibinocci numbers are needed: "))
print(fib(x))


#------------------------------------------------------------------------------------------------

# Exercise 15 (and Solution)

# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order


stra = 'This is a string' 
revword = stra.split() 
revword.reverse() 
revword=' '.join(revword)
print(revword)



#------------------------------------------------------------------------------------------------
# Exercise 16 (and Solution)

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords 
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be 
# random, generating a new password every time the user asks for a new password. Include your run-time 
# code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
 
n = random.randint(12, 27)
s = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+:?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
lens = len(s)-1
password = ""
for i in range(n):
    password+=s[random.randint(0,lens)]

print(password)

#------------------------------------------------------------------------------------------------
# Exercise 18 (and Solution)

# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that 
# the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed 
# correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many 
# “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track 
# of the number of guesses the user makes throughout the game and tell the user at the end.

import random

# num = str(random.randint(1000,9999))

# 4-digit number without repetition
num = "0"

while int(num) < 1000:
    num = ""
    numRange = list(range(0, 9))
    random.shuffle(numRange)

    for i in range(4):
        num += str(numRange.pop())

print(num) # cheat!

tries = 0
ui = ''

while ui != 'e':
    ui = input("Guess the 4-digit number or 'e' to exit: ")

    if ui == 'e':
        print("You tried %d time(s) but did not get the number - %s." % (tries, num))
        break
    
    tries += 1
    numtmp = 'x'+ num + 'x'
    uitmp = 'x'+ ui + 'x'
    bulls = 0
    cows = 0

    for i in range(1,5):
        if uitmp[i] == numtmp[i]:
            cows += 1
            numtmp = numtmp[:i] + 'x' + numtmp[i+1:]
            uitmp  = uitmp[:i]  + 'x' + uitmp[i+1:]

    if cows != 4:
        for i in range(1,5):
            if (uitmp[i] != 'x') and (uitmp[i] in numtmp):
                bulls += 1
                uitmp  = uitmp[:i] + 'x' + uitmp[i+1:]
        print("%d cows, %d bulls.\n" % (cows, bulls))
    else:
        print("You've got the number! - %s - in %d tries." % (num, tries))
        ui = 'e'


#------------------------------------------------------------------------------------------------

# Exercise 20 (and Solution)

# Write a function that takes an ordered list of numbers (a list where the elements are in order 
# from smallest to largest) and another number. The function decides whether or not the given 
# number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
# Use binary search.

import random

lst = []
for i in range(10):
    lst.append(random.randint(1,100))
lst = sorted(lst)
print(lst)

def findElement(n, lst):
    try:
        pos = lst.index(n)
    except:
        pos = -1
    return pos

#print(findElement(32, lst))

def findElementBinary(n, lst):
    p1 = 0
    p2 = len(lst) - 1

    while int((p2-p1) / 2) != 0:
        p = p1 + int((p2-p1) / 2)
        if n == lst[p]:
             return p
        elif n < lst[p]:
            p2 = p
        else: 
            p1 = p
    return -1

print(lst)
print(findElementBinary(68, lst))

#------------------------------------------------------------------------------------------------
# Exercise 24 (and Solution)

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, 
# Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#        --- --- --- 
#       |   |   |   | 
#        --- --- ---  
#       |   |   |   | 
#        --- --- ---  
#       |   |   |   | 
#        --- --- --- 

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 
# 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen 
# using Python’s print statement.

n = int(input("Game board size? :"))

for i in range(n):
    print("\t" + " ---" * n)
    print("\t" + "|   " * n + "|")
print("\t" + " ---" * n)



#------------------------------------------------------------------------------------------------

# Exercise 25 (and Solution)

# You, the user, will have in your head a number between 0 and 100. The program will guess a number, 
# and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess.

tries = 0
n1 = 0
n2 = 100
ans = ""

while int((n2-n1)/2) != 0 and ans != 'c':
    print (n1, " ", n2)
    n = n1 + int((n2-n1) / 2)
    ans = input("Is it " + str(n) + "? Too High/Too Low/Correct (h/l/c)")
    tries += 1
    if ans == 'c':
        print("Ans: %d,  found in %d tries!" % (n, tries))
    if ans == 'l':
        n1 = n
    elif ans == 'h':
        n2 = n

if int((n2-n1)/2) == 0:
    print("Something wrong - no guess.  %d tries." % (tries))


#------------------------------------------------------------------------------------------------
# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 
# means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, 
# tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in 
# a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have 
# won - assume that in every board there will only be one winner.


def isSame(l):
    return len(set(l)) == 1 and l[0] != 0


def checkGrid(game):
    for i in range(3):
        if isSame(game[i]):
            return game[i][0]

    # transpose list of lists
    game = list(map(list, zip(*game)))
    for i in range(3):
        if isSame(game[i]):
            return game[i][0]
        
    diag1 = []
    diag2 = []
    for i in range(3):
        diag1.append(game[i][i])
        diag2.append(game[i][2-i])

    if isSame(diag1):
        return diag1[0]
    if isSame(diag2):
        return diag2[0]

    return 0

game = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]


print(checkGrid(game))

#------------------------------------------------------------------------------------------------
# Tic-Tac-Toe game

def initBoard():
    board = [[0 for i in range(3)] for j in range(3)]
    return board

def displayBoard(board):
    sym = ' xo'
    print("\t    " + "  1 " + "  2 " + "  3 ")
    for i in range(3):
        print("\t    " + " ---" * 3)
        print("\t  " + str(i+1) + " | " + sym[board[i][0]] + " | " + sym[board[i][1]] + " | " + sym[board[i][2]] + " |")
    print("\t    " + " ---" * 3)

def play(board, user):
    correct = False
    while not correct:
        pos = input("Player " + str(user+1) + " move ? row,col : ")
        posList = pos.split(",")
        row = int(posList[0])-1
        col = int(posList[1])-1

        if board[row][col] == 0:
            board[row][col] = user+1
            correct = True
        else:
            print("That square %s is taken!\n" % pos)
    return board


def checkBoardForWinner(board):
    def isSame(l):
        return len(set(l)) == 1 and l[0] != 0

    for i in range(3):
        if isSame(board[i]):
            return board[i][0]

    # transpose list of lists
    board = list(map(list, zip(*game)))

    for i in range(3):
        if isSame(board[i]):
            return board[i][0]
        
    diag = [board[i][i] for i in range(3)]
    if isSame(diag):
        return diag[0]

    diag = [board[i][2-i] for i in range(3)]
    if isSame(diag):
        return diag[0]

    return 0


# Main
game = initBoard()

emptySquares = 9
winner = 0
user = 1

while emptySquares != 0 and winner == 0:
    user = 1 - user
    displayBoard(game)
    game = play(game, user)
    emptySquares-=1
    winner = checkBoardForWinner(game)

displayBoard(game)

if winner == 0:
    print("Draw!")
else: 
    print("player %d wins!" % (user+1))

    

def mystery(N):
    s = []
    while N > 0:
        s.append(N % 3)
        N = int(N / 3)
    print(s)
    buf = ""
    while len(s) > 0:
        buf += str(s.pop())
    return buf

print(mystery(50))

