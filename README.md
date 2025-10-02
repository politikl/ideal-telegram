# ideal-telegram

**ideal-telegram** is a Python-based typing automation tool that simulates natural human typing. Unlike simple "copy-paste" automation, this project adds realistic variations in keystroke speed, timing, pauses, and even mistakes (with corrections), making the output feel organic and indistinguishable from actual human typing.

This tool is lightweight, customizable, and designed for scenarios where human-like typing behavior is essential—whether for demos, automation scripts, editor integrations, or typing simulations.

## Features

### Human-like Typing Simulation
- Types characters one by one instead of pasting the full text instantly.
- Randomized delays between keystrokes for natural rhythm.
- Configurable typing speed in **WPM (Words Per Minute)** or presets (`slow`, `medium`, `fast`, `super fast`).

### Input Options
- Enter text manually.
- Load text from a file (supports `.txt`, `.md`, `.py`, `.js`, `.html`, `.css`, `.json`).
- Use default text (`The quick brown fox jumps over the lazy dog`).
- Take a typing test to benchmark your own speed and accuracy, then let the bot type at your level.

### Typing Test Integration
- Built-in typing test with randomly selected passages.
- Calculates:
  - Words per minute (WPM)  
  - Accuracy (%)  
  - Mistakes made  
  - Characters typed vs expected  
- Optionally sets bot parameters (WPM, error rate) based on your real typing test results.

### Realistic Mistakes and Corrections
- Occasionally makes errors similar to humans (configurable probability).
- Mistakes mimic adjacent keyboard keys (e.g., pressing "s" instead of "a").
- Automatically deletes the wrong character and retypes the correct one.

### Configurable Parameters
- **Typing Speed**: Choose exact WPM or presets (`s`, `m`, `f`, `sf`).
- **Error Rate**: Adjusted based on WPM or typing test accuracy.
- **Keyboard Neighbor Mapping**: Defines which "wrong keys" might realistically be pressed.

### Debugging and Metrics
- Tracks and reports:
  - Mistakes made
  - Ratio of errors to characters
  - Actual WPM achieved vs requested speed
  - Time taken to type the full text

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/politikl/ideal-telegram.git
   cd ideal-telegram
2. Run the python file:
   ```bash
   python3 ideal-telegram.py
