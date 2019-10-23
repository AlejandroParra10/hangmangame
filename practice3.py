# Conditional
print("Welcome to a new week!")
print("What day of the week is it?")

Monday = input("Is today Monday(yes/no): ")

if Monday == "yes":
	print("It's Monday, the weekend is over")
elif Monday == "no":
	print("Have a good week!")
else: 
	print("Have a good week or weekend")
print("Have a good week!")

Friday = input("Is today Friday(yes/no): ")

if Friday == "yes":
	print("It's Friday, the weekend is here")
elif Friday == "no":
	print("Have a good week or weekend!")
else: 
	print("Have a good week or weekend")

Saturday = input("Is today Saturday(yes/no): ")

if Saturday == "yes":
	print("It's the weekend, time to relax")
elif Saturday == "no":
	print("Have a good day")

Otherday = input("Any other day(yes/no): ")

if Otherday == "yes":
	print("It's not the weekend yet")
elif Otherday == "no":
	print("It's the weekend :)")