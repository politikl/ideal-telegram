import keyboard
import random
import time
import sys
import os

class WPMInvalid(Exception):
    pass

def read_file_content(file_input):
    """Try to read content from file, handling both full paths and filenames"""
    try:
        print(f"Debug: Current working directory: {os.getcwd()}")
        print(f"Debug: Looking for file: {file_input}")
        print(f"Debug: Files in current directory: {os.listdir('.')}")
        
        if os.path.exists(file_input):
            print(f"Debug: Found file at: {file_input}")
            with open(file_input, 'r', encoding='utf-8') as file:
                return file.read().strip()
        else:
            print(f"Debug: File not found at: {file_input}")
        
        extensions = ['.txt', '.md', '.py', '.js', '.html', '.css', '.json']
        for ext in extensions:
            test_path = file_input + ext
            print(f"Debug: Trying: {test_path}")
            if os.path.exists(test_path):
                print(f"Debug: Found file at: {test_path}")
                with open(test_path, 'r', encoding='utf-8') as file:
                    return file.read().strip()
        print("Debug: No file found with any extension")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

default_text = "The quick brown fox jumps over the lazy dog"

# Choose input method
while True:
    print("\nChoose input method:")
    print("1. Type text directly")
    print("2. Load text from file")
    print("3. Use default text")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        text = input("Enter the text you want to type: ")
        break
    elif choice == "2":
        file_input = input("Enter file path or filename: ")
        file_content = read_file_content(file_input)
        if file_content is not None:
            text = file_content
            print(f"Successfully loaded text from file ({len(text)} characters)")
            if len(text) > 100:
                print(f"Preview: {text[:100]}...")
            break
        else:
            print("File not found or could not be read. Please try again.")
            continue
    elif choice == "3":
        text = default_text
        print("Using default text: " + default_text)
        break
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

while True:
    wpm = input("What is the WPM you would like this to be typed at "
                "(or s=slow, m=medium, f=fast, sf=super fast)?\n")
    if wpm == "s":
        wpm = 20
        break
    elif wpm == "m":
        wpm = 50
        break
    elif wpm == "f":
        wpm = 80
        break
    elif wpm == "sf":
        wpm = 120
        break
    try:
        wpm = int(wpm)
        if wpm <= 0:
            raise WPMInvalid("WPM must be greater than 0.")
        break
    except ValueError:
        print("Invalid input: please enter a number or one of s/m/f/sf.")

default_robot_speed = 19

speed = wpm/default_robot_speed

chance_of_error = ((speed/20)**1.3)/1.5

keyboard_neighbors = {
    # Letters
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
    "q": ["w", "a", "1"],
    "r": ["e", "d", "f", "t"],
    "s": ["a", "w", "e", "d", "x", "z"],
    "t": ["r", "f", "g", "y"],
    "u": ["y", "h", "j", "i"],
    "v": ["c", "f", "g", "b"],
    "w": ["q", "a", "s", "e"],
    "x": ["z", "s", "d", "c"],
    "y": ["t", "g", "h", "u"],
    "z": ["a", "s", "x"],

    # Numbers and shifted symbols
    "1": ["2", "q", "!"],
    "2": ["1", "3", "w", "q", "@"],
    "3": ["2", "4", "e", "w", "#"],
    "4": ["3", "5", "r", "e", "$"],
    "5": ["4", "6", "t", "r", "%"],
    "6": ["5", "7", "y", "t", "^"],
    "7": ["6", "8", "u", "y", "&"],
    "8": ["7", "9", "i", "u", "*"],
    "9": ["8", "0", "o", "i", "("],
    "0": ["9", "-", "p", "o", ")"],

    # Punctuation and shifted symbols
    "-": ["0", "=", "p", "_"],
    "=": ["-", "[", "+"],
    "[": ["=", "]", "p", "{"],
    "]": ["[", "\\", "}"],
    "\\": ["]", "|"],
    ";": ["l", "'", ":"],
    "'": [";", "/", '"'],
    ",": ["m", ".", "<"],
    ".": [",", "/", ">"],
    "/": [".", "'", "?"],

    # Shifted symbols (mapped for possible typos)
    "!": ["1", "2", "@"],
    "@": ["2", "1", "3", "#"],
    "#": ["3", "2", "4", "$"],
    "$": ["4", "3", "5", "%"],
    "%": ["5", "4", "6", "^"],
    "^": ["6", "5", "7", "&"],
    "&": ["7", "6", "8", "*"],
    "*": ["8", "7", "9", "("],
    "(": ["9", "8", "0", ")"],
    ")": ["0", "9", "-", "("],
    "_": ["-", "+", "0"],
    "+": ["=", "_", "["],
    "{": ["[", "]"],
    "}": ["]", "\\"],
    "|": ["\\"],
    ":": [";", '"'],
    '"': ["'", ":"] ,
    "<": [",", ">"],
    ">": [".", "<"],
    "?": ["/"]
}

start = time.time()

index = 0
debug_text = ""
mistakes = 0

time.sleep(3)

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
end = time.time()
words = len(text.split())
real_wpm = 60*words/(end-start)
time.sleep(0.01)
print("\nYour text was successfully printed!")
print(f"debug_text={debug_text}, mistakes={mistakes}, ratio={mistakes/len(text)}, time took={end-start} realwpm = {real_wpm}")
