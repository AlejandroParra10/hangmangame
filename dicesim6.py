import random
import time
roll = input("Would you like to roll a dice?")

while roll == "Yes" or roll == "yes":
  print("ROLLING DICE")
  time.sleep(2)
  print(random.randint(1,6))
  roll = input("Would you like to roll again?")

while roll == "no" or roll == "No":
  print("Ok, bye.")
  break