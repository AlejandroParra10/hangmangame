# Make a list
myClasses = ["Algebra", "English", "World History"]
print(myClasses)

# add an item to the list
# append or insert
# append will add to the back of the list
myClasses.append("Coding")
print(myClasses)
favClass = input("What is your favorite class? ")
myClasses.append(favClass)
print(myClasses)
# insert 
myClasses.insert(3, "Art")
print(myClasses)
# overtime/replace
myClasses[4] = "Science"
print(myClasses)

# remove list items 
# remove, pop
# remove will remove a specific item 
myClasses.remove("Science")
print(myClasses)
# myClasses.remove("Lunch")
# pop will remove at a specific index
myClasses.pop() # erases the last item
print(myClasses)
myClasses.pop(1)
print(myClasses)
# len - it returns the length of a list 
print("myClasses is " + str(len(myClasses))+ " items long")

print(myClasses[len(myClasses) - 1])

# loop through a list 
count = 1 
for aClass in myClasses:
	print("Item" + str(count) + "is" + aClass)
	count = count + 1

numbers = [1, 3, 5, 7, 9,]
print(numbers)
# challenge: loop thorugh the list add the numbers and print the sum 

total = 0 

for number in numbers:
	total += number

print(total)
#myClasses.append("Cooking")

if "cooking" in myClasse:
	print("Have fun cooking")
else:
	print("Okay then")