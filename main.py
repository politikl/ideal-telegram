import keyboard
import random
import time

text = input("What is the text you would like to be typed? \n")
chance_of_delete = 1/20

index = 0

time.sleep(5)
while index < len(text):
    time.sleep(random.random())
    if index == 0:
        keyboard.write(text[index])
        index += 1
    if random.random() < chance_of_delete:
        keyboard.send("delete")
        index -= 1
    else:
        keyboard.write(text[index])
        index += 1
time.sleep(0.1)
print("\nYour text was printed!")
