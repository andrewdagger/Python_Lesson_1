# This program says hello and asks for my name
import time


print("Hi")
time.sleep(2)
print("give me")
time.sleep(2)
print("one second, I just")
time.sleep(1)
print("got up from a nap")

time.sleep(2)
for i in "LOADING.....":
    print(i, sep=' ')
    time.sleep(1)

print()
time.sleep(2)
print("Hello and Welcome to my wonderful laughter shop.")
time.sleep(2)

print("Let's introduce each other first. My name is Ms. Robot!")
time.sleep(2)

print("What is your name?")
time.sleep(1)

name = input("Please type your name here: ")
for i in range(2):
    print("Processing...")
    time.sleep(1)

print(f"Welcome, {name}. It is a pleasure to meet you!")
time.sleep(3)

print("Let's get to know each other a bit better. I was born a few weeks ago, how old are you?")
time.sleep(2)

age = int(input("Please type your age here: "))

print()
print()

if age > 25:
    print("Geez I can't believe you are this old!")
    time.sleep(2)
    print()
    print("You have been alive for...")
    
    for i in range(age):
        if i % 2 != 0 and i < 15:
            print(i)
            i += 1
            time.sleep(1)
    print("Wow, I can't even count that far. You are old my Friend, Sooooorry!")
else:
    print("Awwww! You are such a baby :)")
                      
time.sleep(4)                      
print(f"Let me tell you what I can do for you today, {name}.")
time.sleep(1)
print("We are going to make a deal.")
time.sleep(1)
print("I am going to make 3 jokes and if I make you laugh at least 2 out of 3 times, I win and you have to buy me an oil martini for my parts.")
time.sleep(1)
print("Otherwise, I will buy you pizza! I hope you are ready!")

wins = 0

loss = 0

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Joke 1! " + "-" * 30)
print("-" * 70)

#### Let's get started with some jokes

time.sleep(1)
print("How many tickles does it take to make an Octopus laugh?")
answer1 = input("Please type your answer here: ")

if answer1.lower() == 'tentickles':
    print("haha, that's correct. I guess you can be funny too!")
else:
    print("No silly")
    print("The answer is Ten-Tickles :)")

time.sleep(1)
record1 = input("Did you laugh??? Please answer yes or no: ")
time.sleep(1)

if record1.lower() == 'yes':
    wins += 1
else:
    loss += 1

print("Cool, let's keep going!")

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Joke 2! " + "-" * 30)
print("-" * 70)


time.sleep(1)
print("People think 'icy' is the easiest word to spell. Come to think of it, I see why.")

record2 = input("Did you laugh??? Please answer yes or no: ")
time.sleep(1)
if record2.lower() == 'yes':
    wins += 1
else:
    loss += 1
    
print("Cool, let's keep going!")



time.sleep(2)
print("-" * 70)
print("-" * 30 + " Joke 3! " + "-" * 30)
print("-" * 70)


time.sleep(1)
print("What's a balloon's least favorite type of music?")

answer3 = input("Please type your answer here: ")

if answer3.lower() == 'pop':
    print("haha, that's correct. I guess you can be funny too!")
else:
    print("No silly")
    print("Pop! :)")

record3 = input("Did you laugh??? Please answer yes or no: ")
time.sleep(1)
if record3.lower() == 'yes':
    wins += 1
else:
    loss += 1 
    
time.sleep(2)
print("Okay, let's tally thing up!")
time.sleep(2)
print("-" * 70)
print("I won {} times, and you won {} times.".format(wins, loss))

if wins > loss:
    
    print("Wohoooooo!!! I won, and now you have to buy me my oil martini with extra gears in it ;)")
    time.sleep(3)
    print("This was a lot of fun, I hope you come visit me again soon. Take care!")
else:
    print("Dang it, I thought I was funny. Ohh well, I will definitely get you next time.")
    time.sleep(3)
    print(f"This was a lot of fun {name}, I hope you come visit me again soon. Take care!")