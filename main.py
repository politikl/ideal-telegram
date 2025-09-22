import keyboard
import random
import time
import sys

default_text = "The quick brown fox jumps over the lazy dog"
text = input("What is the text you would like to be typed (typing d will type the default text)? \n")

if text == "d":
    text = default_text
if text == "q":
    sys.exit()
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
    wpm = int(wpm)

default_robot_speed = 19

speed = wpm/default_robot_speed

chance_of_error = (speed/20)**1.3
keyboard_neighbors = {
    "a": ["q", "w", "s", "z"],
    "b": ["v", "g", "h", "n"],
    "c": ["x", "d", "f", "v"],
    "d": ["s", "e", "r", "f", "c", "x"],
    "e": ["w", "s", "d", "r"],
    "f": ["d", "r", "t", "g", "v", "c"],
    "g": ["f", "t", "y", "h", "b", "v"],
    "h": ["g", "y", "u", "j", "n", "b"],
    "i": ["u", "j", "k", "o"],
    "j": ["h", "u", "i", "k", "n", "m"],
    "k": ["j", "i", "o", "l", "m"],
    "l": ["k", "o", "p"],
    "m": ["n", "j", "k"],
    "n": ["b", "h", "j", "m"],
    "o": ["i", "k", "l", "p"],
    "p": ["o", "l"],
    "q": ["w", "a"],
    "r": ["e", "d", "f", "t"],
    "s": ["a", "w", "e", "d", "x", "z"],
    "t": ["r", "f", "g", "y"],
    "u": ["y", "h", "j", "i"],
    "v": ["c", "f", "g", "b"],
    "w": ["q", "a", "s", "e"],
    "x": ["z", "s", "d", "c"],
    "y": ["t", "g", "h", "u"],
    "z": ["a", "s", "x"]
}

index = 0
debug_text = ""
mistakes = 0

time.sleep(0.5)

if len(text) == 1:
    keyboard.write(text)
    sys.exit()
while index < len(text):
    time.sleep(random.random()/speed)
    if index == 0:
        keyboard.write(text[index])
        debug_text += text[index]
        index += 1
    if random.random() < chance_of_error:
        if text[index] == " ":
            keyboard.write(text[index])
            index += 1
            continue
        else:
            letter = keyboard_neighbors[text[index]][random.randint(0, len(keyboard_neighbors[text[index]])-1)]
            keyboard.write(letter)
            debug_text += letter
            time.sleep(random.random()*2/speed)
            keyboard.send("delete")
            debug_text += "'del'"
            mistakes += 1
    else:
        keyboard.write(text[index])
        debug_text += text[index]
        index += 1
time.sleep(0.01)
print("\nYour text was successfully printed!")
print(f"debug_text={debug_text} mistakes={mistakes} ratio={mistakes/len(text)}")
