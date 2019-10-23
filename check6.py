# Alejandro Parra
# period 6

# variable Declaration and assignment
myVariable = "Parra" #String variable
myNumber = 12 # int variable
myDecimal = 12.6 # float variable

# Make a variable of type String
myString = ""

# while loops
x = 1
while x <= 10:
	print(x)
	x += 1
# challenge: Make a while loop to count down from 100 to 1
y = 100
while y >= 1:
	print(y)
	y -= 100

# String concatenation
# example 
String1 = "Hello"
String2 = "world"
print(String1 + String2 + "!")

# challenge: Make a variable with your favorite movie
# print "My favorite movie is"
String3 = "My favorite movie is"
String4 = " The Great Gatsby"
print(String3 + String4 + ".")

# input
# Example 
yourName = input("What is your name? ")
print("Hello" + yourName)

#challenge
#promts for favorite song 
#print your favorite song is ...
# favorite song Last night a DJ saved my life
yourSong = input("What is your favorite song? ")
print(" I love that song" + yourSong)

# casting chenge one type into another
myNum = input("Enter a number") #myNum is a string type
myNum = int(myNum) + 10 # myNum is now an int
print("The answer is" + str(myNum))

# ask for two numbers, add them, and print the sum
Num1 = input("Enter a number")
Num2 = input ("Enter a second number")

# if and if/else
# example 
num = int(input("What is your number: "))

if num > 100: 
	print("Your number is more than 100")
elif num == 100:
	print("Your number is 100")
else:
	print("Your number is less than or equal to 100")

# challenge ask if today is your birthday 
# if it os print happy birthday

if today is your birthday == "yes":
 print("Happy birthday")
elif today is your birthday == "no":
	print("Have a good day!")
else: 
	print("Sorry not sorry it's not your birthday")
