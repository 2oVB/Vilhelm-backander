import os
os.system("pause")
import time

x = 0
il = [500]

input = input("Type a max number! ")

fixedinput = int(input)

while True:
    if input.isdigit() == True:
        if( x < fixedinput):
            time.sleep(0.5)
            x = x + 1
            print(x)
