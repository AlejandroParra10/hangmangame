# Alejandro Parra
# Period 6

import time
import os

frameList = [
'''
  O
 /|\\
 / \\
     ''', '''
  O
 /|->
 / \\
    _____
 __/  0  \__
  |   _   |
  |__| |__|                                                                   

        ___________
       //     |    \\
 _____//______|_____\\________
 |    __             __     |
 |___/  \\___________/  \\____| 
     \\__/           \\__/        

                           '''
]

while True:
	for frame in frameList:
	    os.system("cls")
	    print(frame)
	    time.sleep(.10)