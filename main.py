import keyboard
import random
import time

text = input("What is the text you would like to be typed? \n")
chance_of_error = 1/10
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

index = 0
debug_text = ""

time.sleep(5)
while index < len(text):
    time.sleep(random.random())
    if index == 0:
        keyboard.write(text[index])
        debug_text += text[index]
        index += 1
    if random.random() < chance_of_error:
        letter = letters[random.randint(0,25)]
        keyboard.write(letter)
        debug_text += letter
        time.sleep(random.random())
        keyboard.send("delete")
        debug_text += "'del'"
    else:
        keyboard.write(text[index])
        debug_text += text[index]
        index += 1
time.sleep(0.1)
print("\nYour text was successfully printed!")
print(debug_text)
