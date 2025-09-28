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

def calculate_accuracy(original, typed):
    """Calculate accuracy between original and typed text"""
    if len(original) == 0:
        return 100.0
    
    correct_chars = 0
    min_length = min(len(original), len(typed))
    
    # Count correct characters
    for i in range(min_length):
        if original[i] == typed[i]:
            correct_chars += 1
    
    # Penalize for length differences
    length_penalty = abs(len(original) - len(typed))
    total_chars = len(original)
    
    accuracy = ((correct_chars - length_penalty) / total_chars) * 100
    return max(0, accuracy)  # Don't allow negative accuracy

def take_typing_test():
    """Conduct a typing test and return WPM and accuracy"""
    test_texts = [
        "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet and is perfect for typing practice.",
        "Programming is not about what you know; it's about what you can figure out. The best way to learn is by doing and making mistakes.",
        "Practice makes perfect, but perfect practice makes permanent. Focus on accuracy first, then build up your speed gradually over time.",
        "Technology is best when it brings people together. Good software should be intuitive, reliable, and solve real problems for users.",
        "The only way to do great work is to love what you do. If you haven't found it yet, keep looking and don't settle for less."
    ]
    
    test_text = random.choice(test_texts)
    
    print("\n" + "="*60)
    print("TYPING TEST")
    print("="*60)
    print("You will be given a text to type. Type it as accurately and quickly as possible.")
    print("Press Enter when you're ready to start...")
    input()
    
    print("\nText to type:")
    print("-" * 40)
    print(test_text)
    print("-" * 40)
    print("\nStart typing now (press Enter when finished):")
    
    start_time = time.time()
    typed_text = input()
    end_time = time.time()
    
    # Calculate metrics
    time_taken = end_time - start_time
    word_count = len(test_text.split())
    wpm = (word_count / time_taken) * 60
    accuracy = calculate_accuracy(test_text, typed_text)
    
    # Count character-level mistakes
    mistakes = 0
    min_length = min(len(test_text), len(typed_text))
    for i in range(min_length):
        if test_text[i] != typed_text[i]:
            mistakes += 1
    
    # Add mistakes for length differences
    mistakes += abs(len(test_text) - len(typed_text))
    
    print("\n" + "="*60)
    print("TYPING TEST RESULTS")
    print("="*60)
    print(f"Time taken: {time_taken:.1f} seconds")
    print(f"Words per minute (WPM): {wpm:.1f}")
    print(f"Accuracy: {accuracy:.1f}%")
    print(f"Total mistakes: {mistakes}")
    print(f"Characters typed: {len(typed_text)}")
    print(f"Expected characters: {len(test_text)}")
    
    return wpm, accuracy, mistakes, len(test_text)

default_text = "The quick brown fox jumps over the lazy dog"

# Choose input method
while True:
    print("\nChoose input method:")
    print("1. Type text directly")
    print("2. Load text from file")
    print("3. Use default text")
    print("4. Take typing test to set bot parameters")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
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
        # Take typing test and use results
        user_wpm, user_accuracy, user_mistakes, text_length = take_typing_test()
        
        # Ask if they want to use these results
        use_results = input(f"\nWould you like the bot to type at {user_wpm:.1f} WPM with {user_accuracy:.1f}% accuracy? (y/n): ").lower()
        if use_results == 'y':
            # Set WPM based on test results
            wpm = int(user_wpm)
            
            # Ask for text to type
            print("\nNow choose what text the bot should type:")
            print("1. Type text directly")
            print("2. Load text from file") 
            print("3. Use default text")
            
            text_choice = input("Enter your choice (1-3): ").strip()
            
            if text_choice == "1":
                text = input("Enter the text you want the bot to type: ")
            elif text_choice == "2":
                file_input = input("Enter file path or filename: ")
                file_content = read_file_content(file_input)
                if file_content is not None:
                    text = file_content
                    print(f"Successfully loaded text from file ({len(text)} characters)")
                    if len(text) > 100:
                        print(f"Preview: {text[:100]}...")
                else:
                    print("File not found. Using default text.")
                    text = default_text
            else:
                text = default_text
                print("Using default text: " + default_text)
            
            break
        else:
            continue
    elif choice == "5":
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

# Get WPM if not set by typing test
if 'wpm' not in locals():
    while True:
        wpm_input = input("What is the WPM you would like this to be typed at "
                    "(or s=slow, m=medium, f=fast, sf=super fast)?\n")
        if wpm_input == "s":
            wpm = 20
            break
        elif wpm_input == "m":
            wpm = 50
            break
        elif wpm_input == "f":
            wpm = 80
            break
        elif wpm_input == "sf":
            wpm = 120
            break
        try:
            wpm = int(wpm_input)
            if wpm <= 0:
                raise WPMInvalid("WPM must be greater than 0.")
            break
        except ValueError:
            print("Invalid input: please enter a number or one of s/m/f/sf.")

default_robot_speed = 19

speed = wpm/default_robot_speed

# Calculate error rate based on WPM (or use typing test results if available)
if 'user_accuracy' in locals():
    # Use actual error rate from typing test
    chance_of_error = (100 - user_accuracy) / 100 * 0.5  # Scale down for more realistic bot behavior
    print(f"Bot will type at {wpm} WPM with approximately {chance_of_error*100:.1f}% error rate based on your typing test.")
else:
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

print(f"\nStarting to type in 3 seconds at {wpm} WPM...")
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
    
    if index < len(text):
        if random.random() < chance_of_error:
            if text[index] == " ":
                keyboard.write(text[index])
                index += 1
                continue
            else:
                # Check if the character has neighbors defined
                if text[index].lower() in keyboard_neighbors:
                    neighbors = keyboard_neighbors[text[index].lower()]
                    letter = neighbors[random.randint(0, len(neighbors)-1)]
                    keyboard.write(letter)
                    debug_text += letter
                    time.sleep(random.random()*2/speed)
                    keyboard.send("delete")
                    debug_text += "'del'"
                    mistakes += 1
                else:
                    # If no neighbors defined, just type the correct character
                    keyboard.write(text[index])
                    debug_text += text[index]
                    index += 1
        else:
            keyboard.write(text[index])
            debug_text += text[index]
            index += 1

end = time.time()
words = len(text.split())
real_wpm = 60*words/(end-start)
time.sleep(0.01)
print("\nYour text was successfully printed!")
print(f"debug_text={debug_text}, mistakes={mistakes}, ratio={mistakes/len(text):.3f}, time took={end-start:.1f}s, real wpm = {real_wpm:.1f}")
