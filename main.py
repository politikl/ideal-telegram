import keyboard
import random
import time

default_text = "The quick brown fox jumps over the lazy dog"
text = input("What is the text you would like to be typed (typing d will type the default text)? \n")

if text == "d":
    text = default_text
else:
    pass

wpm = input("What is the WPM you would like this to be type at (or you can type s for a slow speed, m for a medium speed, f for a fast speed, and sf for a super fast speed)?\n")

if wpm == "s":
    wpm = 20
if wpm == "m":
    wpm = 50
if wpm == "f":
    wpm = 80
if wpm == "sf":
    wpm = 120
else:
    pass

default_robot_speed = 19

speed = wpm/default_robot_speed

chance_of_error = (speed)/30
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

index = 0
debug_text = ""

time.sleep(5)
while index < len(text):
    time.sleep(random.random()/speed)
    if index == 0:
        keyboard.write(text[index])
        debug_text += text[index]
        index += 1
    if random.random() < chance_of_error:
        letter = letters[random.randint(0,25)]
        keyboard.write(letter)
        debug_text += letter
        time.sleep(random.random()/speed)
        keyboard.send("delete")
        debug_text += "'del'"
    else:
        keyboard.write(text[index])
        debug_text += text[index]
        index += 1
time.sleep(0.1)
print("\nYour text was successfully printed!")
print(debug_text)
