# Module 2: Python — Making the Computer Do What YOU Want

```
LEVEL 2 UNLOCKED: Code Wizard
==============================
Linux lets you command your computer. Python lets you BUILD things.
Games. Calculators. Story generators. AI chatbots.
This is where programming really starts.
```

## What Is Python?

Python is a **programming language** — a way to write instructions the computer understands.

Why Python?
- It reads almost like English — no weird symbols everywhere
- Netflix uses it to recommend shows. NASA uses it to analyze space data. Instagram is built with it.
- It's free and runs on Linux, Windows, Mac, and Raspberry Pi
- The AI you'll control in Module 3 is written in Python

> **Fun Fact:** Python is named after Monty Python's Flying Circus (a British comedy show),
> NOT the snake. Though the snake logo is cooler. 🐍

---

## Setting Up

Open your terminal and check Python is installed:

```bash
python3 --version
```

You should see something like `Python 3.11.2`.

To start the Python **interactive shell** (great for experimenting):

```bash
python3
```

You'll see `>>>` — that means Python is waiting for you.
Type `exit()` or press `Ctrl+D` to quit.

To run a Python file:

```bash
python3 my_program.py
```

---

### Your Code Editor: VS Code

Typing Python into `nano` works, but a real **code editor** makes life much easier.
**Visual Studio Code (VS Code)** is the editor used by millions of professional developers
at Google, Microsoft, and everywhere else. It's free, fast, and works for Python,
shell scripts, web pages, and almost anything else.

**Why VS Code?**
- Works for every language, not just Python
- Built-in terminal so you never need to switch windows
- Extensions: add features for Python, Git, AI, and more
- The same tool real software engineers use every day
- Built-in Git integration with a visual diff viewer
- Highlights errors and auto-completes as you type

**Install VS Code on Linux:**

```bash
# Download and add Microsoft's package key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/

# Add the VS Code repository
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

# Install it
sudo apt update && sudo apt install code -y
```

Open it:

```bash
code .
```

The `.` means "open VS Code in the current directory" — it will show all your files on the left.

**The VS Code window layout:**

```
┌─────────────────────────────────────────────────────────┐
│  ACTIVITY BAR   │  EXPLORER / SIDEBAR                   │
│  (left icons)   │  ← your files and directories         │
│                 ├─────────────────────────────────────  │
│                 │  EDITOR (center, top)                  │
│                 │  ← write your code here               │
│                 ├─────────────────────────────────────  │
│                 │  TERMINAL (center, bottom)             │
│                 │  ← run commands without switching app  │
└─────────────────────────────────────────────────────────┘
```

**Open the built-in terminal:** press `` Ctrl+` `` (backtick key, top-left of keyboard)

**Essential keyboard shortcuts:**

| Shortcut | What it does |
|----------|-------------|
| `Ctrl+S` | Save the file |
| `F5` | Run the program (with debugger) |
| ``Ctrl+` `` | Open / close the terminal |
| `Ctrl+Shift+P` | Command palette — search for any action |
| `Ctrl+/` | Comment or uncomment a line |
| `Ctrl+Z` | Undo |
| `Ctrl+F` | Find text in the file |
| `Ctrl+Shift+F` | Find text across all files |

**Install the Python extension** (required for Python features):

1. Press `Ctrl+Shift+X` to open Extensions
2. Search for **Python** (by Microsoft)
3. Click **Install**

Once installed, VS Code will:
- Highlight Python syntax in colour
- Show errors and warnings as you type (red/yellow underlines)
- Auto-complete variable names and functions
- Let you run and debug Python with **F5**

**Open your first Python file in VS Code:**

```bash
# Go to your project directory
cd ~/projects

# Create a new file and open it in VS Code
touch my_program.py
code my_program.py
```

**Recommended extensions to install:**

| Extension | What it adds |
|-----------|-------------|
| Python (Microsoft) | Python language support, debugger |
| GitLens | See git history and blame right in the editor |
| Indent Rainbow | Colours your indentation levels — great for Python |
| Error Lens | Shows error messages inline, next to the broken line |

---

### Virtual Environments: Your Project's Own Sandbox

Before installing extra packages, you need to know about **virtual environments**.

Imagine every project is a separate backpack. A virtual environment is like giving each
project its own backpack so packages you install for one project don't mess up another.
Without it, everything gets thrown into one big pile — and things break.

**Create a virtual environment:**

```bash
# Go to your project folder first
cd ~/projects

# Create a virtual environment called "venv"
python3 -m venv venv
```

This creates a folder called `venv/` that holds a clean copy of Python just for this project.

**Activate it** (you must do this every time you open a new terminal):

```bash
# On Linux / Mac
source venv/bin/activate
```

You'll see `(venv)` appear at the start of your terminal prompt — that means it's active:

```
(venv) alex@computer:~/projects$
```

**Deactivate it** when you're done:

```bash
deactivate
```

> **Rule:** Always activate your virtual environment before running `pip install`.
> If you don't see `(venv)` in your prompt, you're installing into the wrong place.

---

### Installing Extra Packages with pip

Python's built-in modules are great, but thousands of extra ones are available to download.
**pip** is the tool that installs them — always run it **inside an activated virtual environment**.

```bash
# Install a package
pip3 install ollama

# Install multiple packages at once
pip3 install ollama pillow requests

# See all packages you have installed
pip3 list

# Get info about a specific package
pip3 show ollama

# Uninstall a package
pip3 uninstall ollama
```

You'll use `pip3 install` every time a program needs a library that isn't built in to Python.

---

## Week 3: Python Basics

### Lesson 3.1 — Hello, World!

This is your very first Python program — and it's the same first program almost every coder ever writes. Think of it like pressing the "Start Game" button for the first time. Every single app, game, and website was built by someone who started exactly here. It feels small, but you're about to make the computer do something YOU told it to do. That's huge.

Create a file called `hello.py`:

```python
print("Hello, World!")
print("My name is Python!")
```

Each `print()` line is one instruction — Python reads your file from top to bottom and runs them in order, just like reading a recipe.

Run it in your terminal:
```bash
python3 hello.py
```

**What you should see:**
```
Hello, World!
My name is Python!
```

If you see those two lines, your Python is working perfectly. You just wrote and ran your first real program!

`print()` is a **function** — it displays text on the screen.

> **Try this!** Add a third `print()` line that says your own name. What happens if you put a number inside `print()` instead of text? Try `print(42)` and see!

---

### Lesson 3.2 — Variables

Variables are like labeled boxes in your bedroom — you put something inside, give it a name, and come back for it later. In Minecraft, imagine a chest labeled "diamonds" — that's a variable. You can check what's inside, swap the contents, or use it to build something. Variables are how your program remembers things while it runs.

```python
# Storing text (called a "string")
my_name = "Alex"
my_city = "New York"

# Storing numbers
my_age = 9
my_height = 4.5   # feet

# Print them
print("My name is", my_name)
print("I am", my_age, "years old")
print("I live in", my_city)
```

Notice how Python prints the value stored inside each variable — not the word "my_name" but the actual text "Alex". The variable name is just the label on the box.

**Types of data:**

| Type | Example | What it is |
|------|---------|-----------|
| `str` | `"hello"` | Text (string) |
| `int` | `42` | Whole number |
| `float` | `3.14` | Decimal number |
| `bool` | `True` or `False` | Yes/No value |

```python
# Check what type something is
print(type("hello"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
```

Python tells you exactly what kind of data you're working with — this helps you avoid mistakes like trying to add a number to a word.

> **Try this!** Create a variable called `favourite_game` and store your favourite game's name in it. Then `print()` it. Now try changing the value and printing again — variables can be updated any time!

---

### Lesson 3.3 — Math and Operators

Python is an incredibly powerful calculator that never makes arithmetic mistakes. Every game uses math behind the scenes — your character's health bar, score, damage, distance, speed. When you upgrade a weapon in a game, the code is doing math exactly like this. Let's learn the operations Python can do.

```python
# Basic math
print(5 + 3)     # 8  (addition)
print(10 - 4)    # 6  (subtraction)
print(3 * 7)     # 21 (multiplication)
print(20 / 4)    # 5.0 (division — always gives a decimal)
print(20 // 3)   # 6  (floor division — rounds down)
print(20 % 3)    # 2  (modulo — gives the remainder)
print(2 ** 8)    # 256 (exponent — 2 to the power of 8)

# Math with variables
apples = 10
eaten = 3
left = apples - eaten
print("Apples left:", left)
```

The `%` modulo operator is one programmers use all the time — it's great for figuring out if a number is odd or even, or when something should repeat every N turns.

**Challenge:** Calculate how many seconds are in a day.
(Hint: 60 seconds × 60 minutes × 24 hours)

> **Try this!** After solving the challenge, calculate how many seconds old you are (your age in years × 365 × 24 × 60 × 60). The number will be huge — computers handle big numbers no problem!

---

### Lesson 3.4 — Getting Input From the User

So far your programs always do the same thing every time. But real apps react to YOU — they ask for your name, your choice, your answer. `input()` is how Python pauses and waits for the user to type something. Think of every video game menu where you pick "New Game" or enter your player name — that's input in action.

```python
name = input("What is your name? ")
print("Hello,", name, "!")

age = input("How old are you? ")
age = int(age)   # Convert text to a number
next_year = age + 1
print("Next year you will be", next_year)
```

Notice that `input()` always hands you back text, even if the user typed a number. That's why we use `int(age)` to convert it — without that step, Python would refuse to add 1 to it.

> `input()` always gives you text. If you want a number, use `int()` or `float()` to convert it.

**What you should see:**
```
What is your name? Alex
Hello, Alex !
How old are you? 9
Next year you will be 10
```

> **Try this!** Ask for two numbers as input, convert both with `int()`, and print their sum. What happens if someone types "banana" instead of a number? (You'll learn how to handle that crash in Lesson 5.4!)

---

### Lesson 3.5 — If / Elif / Else (Making Decisions)

Every game needs decisions: did you win or lose? Is the enemy in range? Do you have enough gold to buy that sword? `if` statements are how programs make choices — they check a condition, and if it's true, they run a block of code. This is what makes programs feel intelligent and reactive, not just boring scripts.

```python
score = int(input("Enter your test score: "))

if score >= 90:
    print("A — Excellent!")
elif score >= 80:
    print("B — Great job!")
elif score >= 70:
    print("C — Pretty good")
elif score >= 60:
    print("D — You can do better")
else:
    print("F — Let's study more!")
```

Python checks each condition from top to bottom and runs the first one that matches — then skips the rest. The `else` at the bottom is the catch-all "none of the above" option.

**What you should see** (if you enter 85):
```
Enter your test score: 85
B — Great job!
```

**Comparison operators:**

| Symbol | Meaning |
|--------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

**Logical operators:**

```python
age = 9
has_permission = True

if age >= 8 and has_permission:
    print("You can join!")

if age < 5 or age > 100:
    print("Are you sure about that age?")

if not has_permission:
    print("You need permission first")
```

`and` means BOTH conditions must be true. `or` means AT LEAST ONE must be true. `not` flips true to false and false to true — like a toggle switch.

> **Try this!** Write a program that asks "How many lives do you have?" and prints "Game Over!" if it's 0, "Danger zone!" if it's 1, and "You're good!" for anything else. Add an `and` check: only give the "Danger zone!" message if lives is 1 AND the player has been playing for more than 5 minutes (just use another `input()` for minutes).

---

### Lesson 3.6 — Loops: Doing Things Many Times

Imagine if every enemy in a game had to be coded one by one — that would take forever! Loops let you repeat actions automatically, as many times as you want. They're one of the most powerful ideas in programming. Spawning 100 enemies, drawing a grid, checking every item in your inventory — all loops.

**For loop** — repeat a set number of times:

```python
# Count from 0 to 4
for i in range(5):
    print("Count:", i)

# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Count by 2s
for i in range(0, 20, 2):
    print(i)

# Loop over text characters
word = "Python"
for letter in word:
    print(letter)
```

`range(5)` gives you the numbers 0, 1, 2, 3, 4 — notice it stops BEFORE 5. That's because programmers count from 0.

**What you should see** (for `range(5)` loop):
```
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
```

**While loop** — repeat until something is false:

```python
lives = 3
while lives > 0:
    print("Lives remaining:", lives)
    lives = lives - 1
print("Game Over!")
```

The while loop keeps going as long as `lives > 0` is true. The moment `lives` hits 0, it stops and prints "Game Over!" — just like a real game.

**Breaking out of a loop:**

```python
for i in range(100):
    if i == 5:
        break    # Stop the loop
    print(i)
```

`break` is the emergency exit for a loop — it stops immediately, even if there were more repetitions planned.

> **Try this!** Use a `for` loop to print a countdown from 10 to 1, then print "BLAST OFF!" after the loop ends. (Hint: `range(10, 0, -1)` counts backwards!)

---

### Mini Project: Multiplication Table Generator

You've learned variables, loops, and f-strings — now combine them into something actually useful. This project generates a full times table for any number instantly. Your teacher would have to write it on the board, one line at a time. Your program does it in milliseconds. That's the power of loops.

```python
number = int(input("Which multiplication table? "))
print()
print(f"--- {number} Times Table ---")

for i in range(1, 13):
    result = number * i
    print(f"{number} x {i:2} = {result}")
```

The `:2` inside the f-string is a formatting trick — it pads the number with a space so all the equals signs line up neatly in a column.

**What you should see** (if you enter 7):
```
--- 7 Times Table ---
7 x  1 = 7
7 x  2 = 14
7 x  3 = 21
...
7 x 12 = 84
```

**Super Challenge:** After printing the table, ask the user a random question from it and check if they get it right. You'll need `import random` and `random.randint(1, 12)` to pick a random number — you'll learn exactly how `import` works in Week 5, but give it a try now!

> **Try this!** Change `range(1, 13)` to `range(1, 21)` to make a 20-times table. Then try generating tables for BOTH 6 and 7 by putting the whole loop inside another loop: `for number in [6, 7]:`.

---

## Week 4: Lists, Functions, and More

### Lesson 4.1 — Lists

A list is like your game inventory — one container that holds many items. In Minecraft, your hotbar is a list: item 0, item 1, item 2... up to item 8. Lists let you store lots of things together and loop through them one by one. Without lists, you'd need a separate variable for every single item — that gets messy fast.

```python
# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Access by index (counting starts at 0!)
print(fruits[0])    # apple
print(fruits[1])    # banana
print(fruits[-1])   # mango (last item)

# Change an item
fruits[1] = "blueberry"

# Add to the end
fruits.append("orange")

# Remove an item
fruits.remove("cherry")

# How many items?
print(len(fruits))

# Loop through a list
for fruit in fruits:
    print("I like", fruit)
```

After all those changes, your list now contains `["apple", "blueberry", "mango", "orange"]` — cherry is gone and blueberry replaced banana. You can always check a list's current state with `print(fruits)`.

**Useful list operations:**

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(sorted(numbers))     # [1, 1, 2, 3, 4, 5, 6, 9]
print(max(numbers))        # 9
print(min(numbers))        # 1
print(sum(numbers))        # 31
print(numbers.count(1))    # 2 (how many times 1 appears)
```

These built-in helpers save you from having to write your own sorting or searching code — Python already did the hard work for you.

> **Try this!** Make a list of 5 of your favourite games. Print the first one, the last one (using `-1`), and then use a loop to print them all numbered (1, 2, 3...). Then use `sorted()` to print them in alphabetical order!

---

### Lesson 4.2 — Dictionaries

A dictionary is like a contact book — you look up a name and get their phone number. Or like a Pokédex: you look up "Pikachu" and get all its stats. Dictionaries are perfect when you want to store information about one thing with many different properties. Instead of having separate variables for name, age, and score, you bundle them all together with labels.

```python
# Create a dictionary
person = {
    "name": "Alex",
    "age": 9,
    "grade": 5,
    "hobby": "coding"
}

# Access a value
print(person["name"])    # Alex
print(person["age"])     # 9

# Add or change a key
person["city"] = "New York"

# Remove a key
del person["hobby"]

# Loop through a dictionary
for key, value in person.items():
    print(key, ":", value)

# Check if a key exists
if "name" in person:
    print("Found a name!")
```

When you loop through `.items()`, Python gives you each key-value pair one at a time — perfect for printing out all the info about something like a character stats screen.

> **Try this!** Create a dictionary for your favourite video game character with keys like `"name"`, `"health"`, `"weapon"`, and `"level"`. Print each stat on its own line. Then change the `"level"` to a higher number and print it again to show a "level up!"

---

### Lesson 4.3 — Functions: Reusable Code Blocks

Imagine if every time you wanted to jump in a video game, the game had to re-describe jump physics from scratch. That would be insane — instead, "jump" is one action you can trigger whenever you want. Functions work the same way. You write the code once, give it a name, and call it as many times as you like. This is how real software is built — not one giant mess of code, but organised, named chunks that each do one job.

```python
# Define a function
def say_hello():
    print("Hello!")
    print("How are you?")

# Call the function
say_hello()
say_hello()   # You can call it as many times as you want
```

The `def` keyword means "define a function." Everything indented underneath it belongs to the function. Calling `say_hello()` runs all that code instantly — twice here!

**Functions with parameters (inputs):**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
greet("Jordan")
```

Parameters are like function settings — `name` is a slot you fill in when you call the function. `greet("Alex")` and `greet("Jordan")` run the same code but with different values plugged in.

**Functions that return values:**

```python
def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print(answer)    # 8

# Use return values directly
print(add(10, 20))   # 30
```

`return` sends a value back out of the function so you can use it elsewhere — like a vending machine: you put in a choice, it gives you back a snack.

**Functions with default values:**

```python
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}")

describe_pet("Max")           # Max is a dog
describe_pet("Whiskers", "cat")  # Whiskers is a cat
```

Default values are fallback options — if you don't specify `animal`, Python uses `"dog"` automatically. This lets functions be flexible without needing every detail every time.

> **Try this!** Write a function called `calculate_damage(attack, defense)` that returns `attack - defense` (but never less than 0). Call it with different numbers and print the results. This is literally how damage calculation works in RPG games!

---

### Lesson 4.4 — f-Strings (Fancy Text Formatting)

Plain `print()` with commas works, but f-strings are cleaner and much more powerful — they let you drop variables and even math directly into text, exactly where you want them. Professional Python developers use f-strings constantly. Once you try them, you'll never want to go back.

```python
name = "Alex"
age = 9
score = 95.7

# f-string puts variables right in the text
print(f"My name is {name} and I am {age} years old.")
print(f"My score was {score:.1f}%")   # .1f = 1 decimal place

# Math inside f-strings
width = 10
height = 5
print(f"Area = {width * height}")
```

The `f` before the quote is the magic letter — it tells Python "look inside the curly braces `{}` and replace them with real values." The `:.1f` is a formatting code that rounds to 1 decimal place, so `95.7` stays `95.7` but `95.7777` becomes `95.8`.

**What you should see:**
```
My name is Alex and I am 9 years old.
My score was 95.7%
Area = 50
```

> **Try this!** Make a "character stats" display using f-strings. Create variables for `hero_name`, `hp`, `attack`, and `gold`, then print a nicely formatted card like `"Hero: Alex | HP: 100 | ATK: 15 | Gold: 250"`. Try formatting gold with commas: `{gold:,}` turns 1000 into `1,000`!

---

### Mini Project: Number Guessing Game

Time to build your first real, playable game from scratch! This project uses almost everything from Week 3 and 4: variables, input, if/elif/else, loops, and functions. It's the same kind of logic that powers "Wordle" — make a guess, get a hint, narrow it down. You'll be surprised how fun something this small can be.

> **Note:** This project uses `import random` — a sneak peek at Week 5's modules lesson.
> Just put it at the top of your file and it works!

```python
import random

def play_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} guesses. Good luck!")
    print()

    while attempts < max_attempts:
        guess = int(input(f"Guess #{attempts + 1}: "))
        attempts += 1

        if guess == secret:
            print(f"CORRECT! You got it in {attempts} guesses!")
            return
        elif guess < secret:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"({remaining} guesses left)")

    print(f"Out of guesses! The number was {secret}.")

play_guessing_game()
```

**What you should see** (example run):
```
=== Number Guessing Game ===
I'm thinking of a number between 1 and 100.
You have 7 guesses. Good luck!

Guess #1: 50
Too low! Try higher.
(6 guesses left)
Guess #2: 75
Too high! Try lower.
(5 guesses left)
```

> **Try this!** After the game ends, wrap the whole thing in a `while True:` loop that asks "Play again? (y/n):" and only breaks if the user types `"n"`. Bonus: keep track of the player's best score (fewest guesses to win) and display it each round!

---

## Week 5: Files, Modules, and Building Real Programs

### Lesson 5.1 — Reading and Writing Files

Everything you've built so far disappears when the program ends. Files are how programs save things permanently — your high score, your to-do list, your progress. Every app you've ever used stores data in files somewhere. Learning to read and write files is the difference between a toy program and a real tool that actually remembers things.

```python
# Write to a file
with open("my_notes.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Read the whole file
with open("my_notes.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("my_notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# Append to a file (add without erasing)
with open("my_notes.txt", "a") as file:
    file.write("Fourth line added later\n")
```

The `"w"` mode creates a new file (or erases an existing one). The `"r"` mode reads it. The `"a"` mode appends — it adds to the end without wiping what's already there. The `with` keyword handles opening and closing the file safely so you never leave it accidentally open.

After running this code, open your terminal and type `cat my_notes.txt` — you'll see the actual file was created with your text inside!

> **Try this!** Write a "high score saver" — ask the player for their name and score, then save both to a file called `scores.txt` using `"a"` mode. Run the program 3 times with different names. Then read and print the file to see all scores collected!

---

### Lesson 5.2 — Importing Modules

Python comes with an enormous toolbox of pre-built code called **modules**. Instead of writing your own random number generator or calendar system, you just `import` one and use it. This is one of the things that makes Python so powerful — millions of hours of work, ready to use in one line. It's like having cheat codes for programming.

```python
# Random numbers
import random
print(random.randint(1, 10))       # Random number 1-10
print(random.choice(["a","b","c"]))  # Random item from list

# Math functions
import math
print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.141592...
print(math.floor(3.9))   # 3
print(math.ceil(3.1))    # 4

# Date and time
import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.strftime("%B %d, %Y"))   # June 12, 2026

# Time / delays
import time
print("Starting...")
time.sleep(2)   # Wait 2 seconds
print("Done!")

# Operating system
import os
print(os.getcwd())         # Current folder
print(os.listdir("."))     # Files in current folder
os.makedirs("new_folder", exist_ok=True)
```

`time.sleep(2)` pauses your program for exactly 2 seconds — great for countdown timers, dramatic pauses, or animations in text games. `os.listdir(".")` shows you the contents of the current folder, just like `ls` in Linux but from inside Python.

> **Try this!** Import `random` and `time`, then make a "countdown" program: count down from 5 to 1, sleeping 1 second between each number, then print "GO!" and pick a random item from a list of challenges like `["Do 10 pushups!", "Sing a song!", "Do a dance move!"]`.

---

### Lesson 5.3 — Debugging: Fixing Broken Code

Every programmer — beginner or expert — writes code that breaks. The skill isn't
avoiding errors, it's reading them and fixing them quickly.

Debugging is actually a detective skill. You're looking for clues about what went wrong. The good news is Python leaves very clear clues — it tells you exactly which line caused the problem and what type of error it was. Once you learn to read those messages, bugs become puzzles instead of disasters.

#### Reading a Traceback

When Python crashes, it prints a **traceback** — a message that tells you exactly
what went wrong and where.

```
Traceback (most recent call last):
  File "hello.py", line 5, in <module>
    print(mesage)
NameError: name 'mesage' is not defined
```

Read it **from the bottom up:**
1. **Last line** — the error type and message: `NameError: name 'mesage' is not defined`
2. **Middle lines** — where it happened: `File "hello.py", line 5`
3. **Top** — the chain of calls that led there (less important for now)

The message `name 'mesage' is not defined` is a big hint — you spelled `message` wrong!

---

#### The Most Common Python Errors

| Error | What It Means | Example Cause |
|-------|--------------|---------------|
| `SyntaxError` | Python can't read your code | Missing `:`, mismatched `()` |
| `IndentationError` | Spaces/tabs are wrong | Mixed spaces and tabs |
| `NameError` | Variable doesn't exist | Typo in variable name |
| `TypeError` | Wrong type for an operation | `"5" + 5` (string + number) |
| `ValueError` | Right type, wrong value | `int("hello")` |
| `IndexError` | List position doesn't exist | `my_list[99]` when list has 3 items |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |

---

#### Print Debugging

The simplest debugging technique: add `print()` statements to see what's happening.

```python
def calculate_total(prices):
    print(f"DEBUG: prices = {prices}")   # Add this
    total = 0
    for p in prices:
        print(f"DEBUG: adding {p}, total so far = {total}")   # And this
        total = total + p
    print(f"DEBUG: final total = {total}")   # And this
    return total

result = calculate_total([10, 20, 30])
print("Result:", result)
```

The `DEBUG:` labels help you spot these temporary prints so you remember to remove them. Once your bug is fixed, delete all the debug lines and test one more time.

Once you fix the bug, remove the `DEBUG:` print lines.

---

#### VS Code's Step-Through Debugger

VS Code has a powerful visual debugger. To use it:

1. Open your Python file in VS Code
2. Press **F5** to start debugging (choose "Python File" if prompted)
3. Click next to a line number to set a **breakpoint** (a red dot appears) — the program will pause there
4. Press **F10** to step one line at a time
5. Watch the **Variables panel** on the left — it shows every variable's current value
6. Spot where the value goes wrong — that's your bug

This is like watching your program run in slow motion.

---

#### A Systematic Debugging Approach

When your code breaks, follow these steps:

```
1. READ the error message from bottom to top
        ↓
2. Go to the line number it mentions
        ↓
3. Check: spelling, missing colon, wrong indent, wrong type
        ↓
4. If not obvious, add print() before that line
        ↓
5. Run again and look at the print output
        ↓
6. Narrow down where the value goes wrong
        ↓
7. Fix it, remove debug prints, run again
```

**Most bugs are one of:** a typo, a wrong indent, using the wrong variable name,
or expecting the wrong type (number vs text).

> **Try this!** Intentionally break a working program three different ways: delete a colon after an `if`, misspell a variable name, and try to `print(5 + "five")`. Read each error message carefully. After a few times, you'll start recognising these errors instantly — like a pro!

---

### Lesson 5.4 — Error Handling

What happens when your program crashes while a real user is using it? It looks bad and confuses people. `try/except` is like a safety net — it catches errors before they crash the program and lets you respond gracefully instead. Every professional app uses error handling. Think of it as the "Game Over" screen instead of the whole game freezing up.

```python
# Without error handling — this crashes:
# number = int("hello")   # ValueError!

# With error handling:
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"Your number doubled is {number * 2}")
except ValueError:
    print("That's not a number! Please enter digits only.")
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    print("This runs no matter what.")
```

Python tries the code inside `try:`. If something goes wrong, it jumps to the matching `except:` block instead of crashing. `finally:` always runs at the end — whether it worked or not. This is useful for cleanup tasks like closing files.

**What you should see** (if you type "banana"):
```
Enter a number: banana
That's not a number! Please enter digits only.
This runs no matter what.
```

**What you should see** (if you type 7):
```
Enter a number: 7
Your number doubled is 14
This runs no matter what.
```

> **Try this!** Go back to Lesson 3.4 where you converted input to `int()`. Wrap that conversion in a `try/except ValueError:` block. Now if someone types "hello" instead of a number, print a friendly message and ask them to try again — use a `while True:` loop that only `break`s when valid input is received!

---

### Mini Project: Mad Libs Story Generator

Mad Libs is a classic game where you fill in random words and end up with a hilarious story. This project is all about functions, f-strings, and user input working together. It's also great practice for `input()` — you'll call it 8 times and store all the answers in variables before building the story at the end. The result is different every single time someone plays it.

```python
def mad_libs():
    print("=== MAD LIBS STORY GENERATOR ===")
    print("Answer the questions, then read your crazy story!")
    print()

    name       = input("A person's name: ")
    animal     = input("An animal: ")
    adjective1 = input("An adjective (describing word): ")
    verb1      = input("A verb (action word): ")
    place      = input("A place: ")
    number     = input("A number: ")
    food       = input("A food: ")
    adjective2 = input("Another adjective: ")

    print()
    print("=" * 50)
    print()
    story = f"""
One {adjective1} day, {name} decided to {verb1} to {place}.
On the way, they saw a {adjective2} {animal} eating {number}
pieces of {food}. "{name}!" cried the {animal}. "I have been
waiting {number} years for someone to bring me more {food}!"
{name} smiled and said, "I always carry extra {food} for
{adjective1} adventures just like this one."

THE END.
"""
    print(story)
    print("=" * 50)

mad_libs()
```

**What you should see** (example with your inputs filled in):
```
==================================================

One SILLY day, ALEX decided to SPRINT to THE MOON.
On the way, they saw a PURPLE ELEPHANT eating 47
pieces of PIZZA. "ALEX!" cried the ELEPHANT...

THE END.

==================================================
```

> **Try this!** Write your own second story template with completely different blanks — maybe a space adventure, a cooking disaster, or a sports commentary. Put both stories in a list and use `random.choice()` to pick which one to use each time!

---

### Mini Project: Simple To-Do List

This is the most "real-world" project in Module 2 — it's basically a mini app. It combines everything: functions, lists, files, loops, input, and error handling. The to-do list saves to a file so your tasks are still there even after you close the program. This is exactly how simple apps like reminder tools work under the hood.

```python
import os

TODO_FILE = "todos.txt"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(todo + "\n")

def show_todos(todos):
    if not todos:
        print("  (no tasks yet)")
    for i, task in enumerate(todos, 1):
        print(f"  {i}. {task}")

def main():
    todos = load_todos()

    while True:
        print("\n=== TO-DO LIST ===")
        show_todos(todos)
        print()
        print("1) Add a task")
        print("2) Remove a task")
        print("3) Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            task = input("New task: ").strip()
            if task:
                todos.append(task)
                save_todos(todos)
                print("Task added!")

        elif choice == "2":
            if not todos:
                print("Nothing to remove!")
            else:
                num = input("Remove task number: ").strip()
                try:
                    idx = int(num) - 1
                    removed = todos.pop(idx)
                    save_todos(todos)
                    print(f"Removed: {removed}")
                except (ValueError, IndexError):
                    print("Invalid number.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please enter 1, 2, or 3.")

main()
```

**What you should see** when you run it:
```
=== TO-DO LIST ===
  (no tasks yet)

1) Add a task
2) Remove a task
3) Quit

Choice: 1
New task: Learn Python loops
Task added!

=== TO-DO LIST ===
  1. Learn Python loops
```

After you quit and run the program again, your tasks are still there — because `load_todos()` reads them back from the file at startup!

> **Try this!** Add a fourth menu option: `"4) Mark a task as done"`. When selected, ask for the task number, then add `" ✓"` to the end of that task and save. Tasks with a checkmark will look different in the list — a simple but satisfying feature!

---

## Python Cheat Sheet

```python
# Variables
x = 10
name = "Alex"

# Print
print("Hello")
print(f"Value is {x}")

# Input
answer = input("Your answer: ")

# If / elif / else
if x > 5:
    pass
elif x == 5:
    pass
else:
    pass

# For loop
for i in range(10):
    pass

# While loop
while x > 0:
    x -= 1

# List
items = [1, 2, 3]
items.append(4)
items[0]

# Dictionary
d = {"key": "value"}
d["new_key"] = "new_value"

# Function
def my_func(a, b):
    return a + b

# File
with open("file.txt", "r") as f:
    content = f.read()

# Import
import random
import math
import os
```

---

---

## Big Project: Text RPG Battle Game ⚔️

This is your **Module 2 capstone** — a real game that uses everything you learned.
A hero fights a monster, turn by turn. Attack, defend, use potions, and win.

```python
import random

def show_status(name, hp, max_hp, potions):
    bar_filled = int((hp / max_hp) * 10)
    bar = "█" * bar_filled + "░" * (10 - bar_filled)
    print(f"\n  {name}: [{bar}] {hp}/{max_hp} HP  | Potions: {potions}")

def hero_attack(hero_atk):
    damage = random.randint(hero_atk - 3, hero_atk + 3)
    critical = random.random() < 0.15   # 15% chance of critical hit
    if critical:
        damage *= 2
        print(f"  ⚡ CRITICAL HIT! You strike for {damage} damage!")
    else:
        print(f"  ⚔️  You attack for {damage} damage!")
    return damage

def monster_attack(monster_atk, is_defending):
    damage = random.randint(monster_atk - 2, monster_atk + 2)
    if is_defending:
        damage = damage // 2
        print(f"  🛡️  The monster strikes for {damage} damage (blocked half!)")
    else:
        print(f"  🔥 The monster attacks for {damage} damage!")
    return damage

def battle(hero_name, monster_name):
    # Hero stats
    hero_max_hp = 50
    hero_hp     = hero_max_hp
    hero_atk    = 10
    potions     = 2

    # Monster stats
    monster_max_hp = 40
    monster_hp     = monster_max_hp
    monster_atk    = 8

    turn = 1
    print(f"\n{'='*40}")
    print(f"  ⚔️  {hero_name} vs {monster_name}! ⚔️")
    print(f"{'='*40}")

    while hero_hp > 0 and monster_hp > 0:
        print(f"\n--- Turn {turn} ---")
        show_status(hero_name, hero_hp, hero_max_hp, potions)
        show_status(monster_name, monster_hp, monster_max_hp, 0)

        print("\nWhat do you do?")
        print("  1) Attack")
        print("  2) Defend (take half damage this turn)")
        if potions > 0:
            print(f"  3) Drink potion (heal 20 HP) — {potions} left")

        choice = input("\nYour move: ").strip()
        is_defending = False

        if choice == "1":
            dmg = hero_attack(hero_atk)
            monster_hp -= dmg

        elif choice == "2":
            is_defending = True
            print("  🛡️  You raise your shield and brace for impact!")

        elif choice == "3" and potions > 0:
            heal = min(20, hero_max_hp - hero_hp)
            hero_hp += heal
            potions -= 1
            print(f"  🧪 You drink a potion and recover {heal} HP!")

        else:
            print("  Invalid choice — you fumble and lose your turn!")

        # Monster attacks back (if still alive)
        if monster_hp > 0:
            dmg = monster_attack(monster_atk, is_defending)
            hero_hp -= dmg
            hero_hp = max(0, hero_hp)

        turn += 1

    print(f"\n{'='*40}")
    if hero_hp > 0:
        print(f"  🏆 VICTORY! {hero_name} defeated {monster_name}!")
        print(f"  You finished with {hero_hp} HP remaining.")
    else:
        print(f"  💀 DEFEATED! {monster_name} won this time...")
        print(f"  Train harder and try again!")
    print(f"{'='*40}\n")

# ── Main ──────────────────────────────────────────────────────────────────────

print("=== TEXT RPG BATTLE ===")
hero_name = input("Enter your hero's name: ").strip() or "Hero"

monsters = [
    "Cave Goblin",
    "Fire Drake",
    "Shadow Wraith",
    "Stone Golem",
    "Zombie Pirate",
]

monster = random.choice(monsters)
print(f"\nA wild {monster} appears!")

battle(hero_name, monster)

again = input("Play again? (y/n): ").strip().lower()
while again == "y":
    monster = random.choice(monsters)
    print(f"\nA {monster} steps out of the shadows...")
    battle(hero_name, monster)
    again = input("Play again? (y/n): ").strip().lower()
```

Run it in your terminal:
```bash
python3 rpg_battle.py
```

### RPG Bonus Challenges 🏆

1. Add a **second monster** that the hero fights if they win the first battle
2. Add an **"Escape"** option that sometimes works (use `random.random() < 0.5`)
3. Add a **different weapon** choice at the start that changes the hero's attack power
4. Track **total gold earned** — each monster drops 5–20 gold when defeated
5. Add a **boss monster** with 80 HP that only appears as the third fight

---

## 🏆 Module 2 Badge: Code Wizard

Earn this badge by completing:
- [ ] The number guessing game
- [ ] The RPG battle game
- [ ] At least 1 RPG bonus challenge
- [ ] The mad libs story generator
- [ ] The to-do list

---

## What's Next?

Now that you know Python, you are ready to use it to **talk to AI**!
Move on to **Module 3: AI with Ollama**.
