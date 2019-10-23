print("Welcome to the To Do List!")
todolist = ["English", "Science", "History", "Math", "Coding"]
print(todolist)


while True: 
	print("Enter a to add a item")
	print("Enter r to remove an item")
	print("Enter p to print list")
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q":
		break
	elif choice == "a":
		todolist.insert(3, "English")
		print(todolist)
		# add an item to the list
		pass
	elif choice == "r":
		todolist.remove("Science")
		print(todolist)
		# remove an item from the list
		pass
	elif choice == "p":
		print(todolist)
		# print the list
		pass
	else:
		print("This was not a choice, try again")