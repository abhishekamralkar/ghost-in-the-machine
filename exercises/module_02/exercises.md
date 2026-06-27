# Module 2 Exercises — Python

Open VS Code, create a new `.py` file for each section, and run it with `python3`.

> **You've got this!** These exercises build on each other, so try them in order. If you get stuck, read the hints below each exercise. Getting stuck is totally normal — even professional programmers get stuck all the time!

---

## Section A: Variables and Types

Think of variables like labeled boxes. You put a value inside the box and give it a name so you can use it later. Python has different *types* of values — text (strings), whole numbers (integers), decimal numbers (floats), and true/false values (booleans). This section helps you get comfortable creating and using them.

**Exercise 1**
Create variables for:
- Your name (string)
- Your age (integer)
- Your height in feet (float)
- Whether you like coding (boolean)

Then print a sentence using all four variables with an f-string.

> **Hint:** An f-string looks like this: `print(f"My name is {name} and I am {age} years old.")` — put an `f` before the opening quote and wrap variable names in `{}`.
>
> **Stuck?** Try creating each variable one at a time and printing just that one first, before putting them all in one sentence.

**Exercise 2**
What will Python print for each line below? Write your answer BEFORE running it.

```python
x = 10
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

> **Hint:** `//` is *floor division* — it divides and then throws away any decimal, keeping only the whole number. `%` is the *remainder* (called modulo) — it tells you what's left over after dividing. `**` means "to the power of". Try to work them out in your head before you run the code!

**Exercise 3**
Fix the bug in this code:
```python
age = input("How old are you? ")
next_year = age + 1
print("Next year you will be", next_year)
```

> **Bug hint:** The bug is on the line that uses `age`. Think about what type of value `input()` gives back — is it a number or text? Look up how to convert it into the right type before doing math with it.
>
> **Stuck?** Remember: `input()` always gives you a **string** (text), even if the user types a number. You need to convert it with `int()` before you can add 1 to it.

---

## Section B: If / Elif / Else

Programs need to make decisions — just like you do! `if`, `elif`, and `else` let your program choose different paths depending on what's true. This section is all about writing code that thinks for itself.

**Exercise 4**
Write a program that:
- Asks the user for a temperature (in Fahrenheit)
- Prints `"Freezing!"` if below 32
- Prints `"Cold"` if 32–59
- Prints `"Warm"` if 60–79
- Prints `"Hot!"` if 80 or above

> **Hint:** Don't forget to convert the input to a number using `int()` or `float()` — `input()` gives you a string, and you can't compare a string to a number like 32.
>
> **Stuck?** Start by just handling the first case (`"Freezing!"`), run it, then add one `elif` at a time.

**Exercise 5**
Write a program that asks for a password.
- If the password is `"dragon123"`, print `"Access granted!"` and a secret message of your choice.
- Otherwise, print `"Wrong password. Access denied."`

> **Hint:** To check if two strings are the same, use `==` (two equals signs). A single `=` is for *storing* a value, not comparing! `if password == "dragon123":` is what you want.

**Exercise 6 — What's the output?**
Trace through this code and write what gets printed, WITHOUT running it first.

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

print("Done")
```

> **Hint:** Go through each condition one at a time, from top to bottom. As soon as one condition is `True`, Python runs that block and *skips the rest*. Also notice that `print("Done")` is outside the if/elif/else — what does that mean for when it runs?

---

## Section C: Loops

Loops let you repeat actions without writing the same code over and over. A `for` loop is great when you know how many times to repeat. A `while` loop keeps going as long as something is true. These are some of the most powerful tools in Python!

**Exercise 7**
Write a `for` loop that prints the numbers 1 through 10, one per line.

> **Hint:** `range(1, 11)` gives you the numbers 1, 2, 3, ... 10. Remember that `range` stops *before* the last number you give it. So `range(1, 11)` goes up to 10, not 11.

**Exercise 8**
Write a `for` loop that prints only the **odd** numbers from 1 to 19.
Hint: `range(1, 20, 2)` counts by 2 starting at 1.

**Exercise 9**
Write a `while` loop that:
- Starts with `coins = 100`
- Subtracts 7 coins each loop
- Prints the coins remaining after each round
- Stops when coins drop below 0
- Prints `"Game over! You ran out of coins."` at the end

> **Hint:** Your `while` condition should keep the loop going as long as `coins >= 0`. Inside the loop, subtract 7 from `coins` each time. The `print("Game over!")` line should be *outside* and *after* the while loop (no indentation under `while`).
>
> **Stuck?** Be careful about infinite loops! If the loop never ends, press **Ctrl + C** in the terminal to stop it.

**Exercise 10 — Loop Tracing**
What does this print? Write it out before running.

```python
total = 0
for i in range(1, 6):
    total = total + i
    print(f"i={i}, total={total}")
print("Final:", total)
```

> **Hint:** Go through the loop step by step. What is `i` on the first round? What does `total` become? Then the second round? Fill in a small table: `i | total`. The last `print` is outside the loop — it only runs once, after all the rounds are done.

---

## Section D: Lists and Dictionaries

Lists let you store many items in one variable — like a shopping list. Dictionaries are like a real dictionary: each word (key) has a meaning (value). Together they are the backbone of almost every Python program you'll ever write!

**Exercise 11**
Create a list called `heroes` with 5 superhero names.
- Print the first hero
- Print the last hero using a negative index
- Add a new hero to the end
- Remove the second hero
- Print the total number of heroes remaining

> **Hint:** Lists start at index `0`, so the first item is `heroes[0]`. The last item is `heroes[-1]` — negative indexes count from the end! Use `.append()` to add to the end and `.remove()` to take something out. Use `len()` to count how many are left.

**Exercise 12**
Write a program that:
- Creates a list of 5 numbers: `[4, 17, 2, 9, 31]`
- Prints the largest number
- Prints the smallest number
- Prints the sum
- Prints the list sorted from smallest to largest

> **Hint:** Python has built-in functions that do the hard work for you! Try `max()`, `min()`, `sum()`, and `sorted()` — each one takes a list as input. For example: `print(max(numbers))`.

**Exercise 13**
Create a dictionary for a video game character with:
- `name`, `class`, `level`, `hp`, `weapon`

Then:
- Print the character's name and weapon in a sentence
- Change their weapon to something better
- Add a new key `"gold"` with a value of `250`
- Print all keys and values using a loop

> **Hint:** Access a dictionary value with `character["name"]`. Change a value the same way: `character["weapon"] = "Flame Sword"`. To loop through all keys and values together, use `for key, value in character.items():`.
>
> **Stuck?** Build the dictionary first and just print it with `print(character)` to check it looks right, before trying the other steps.

---

## Section E: Functions

Functions are like mini-programs inside your program. You write them once and can use them as many times as you want. They help keep your code tidy and avoid repeating yourself. Every professional programmer uses functions constantly!

**Exercise 14**
Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.
Formula: `F = (C × 9/5) + 32`

Test it with: 0°C, 100°C, 37°C (body temperature).

> **Hint:** Your function should **return** the result, not just print it. Then call the function and print the returned value: `print(celsius_to_fahrenheit(100))`. Using `return` means you can use the result in other calculations later.

**Exercise 15**
Write a function `is_even(number)` that returns `True` if the number is even, `False` if odd.
Then use it in a loop to print "even" or "odd" for every number 1–10.

> **Hint:** A number is even if the remainder when divided by 2 is 0. In Python: `number % 2 == 0`. If that's `True`, the number is even! Your function can literally `return number % 2 == 0` in one line.

**Exercise 16**
Write a function `grade(score)` that takes a number and returns the letter grade:
- 90–100 → "A"
- 80–89 → "B"
- 70–79 → "C"
- 60–69 → "D"
- Below 60 → "F"

Test it on scores: 95, 83, 71, 64, 42.

> **Hint:** Use `if / elif / elif / elif / else` inside the function, and `return` the letter each time. Remember to test each score and make sure the right grade comes out!

**Exercise 17 — Fix the Bug**
```python
def multiply(a, b)
    result = a * b
    return result

answer = multiply(6, 7
print("6 x 7 =", answer)
```

> **Bug hint:** There are **two** bugs hidden in this code. Look carefully at the function definition line and at the line that calls the function. Python is very picky about punctuation — check every character on those lines.
>
> **Stuck?** Hint 1: Every `def` line needs a specific punctuation mark at the end. Hint 2: Every opening `(` needs a matching `)`.

---

## Section F: Files

Programs can save information to files and read it back later — even after you close Python! This is how apps store your settings, high scores, and data. It's a really important skill.

**Exercise 18**
Write a program that:
- Creates a file called `favourite_things.txt`
- Writes at least 5 of your favourite things (one per line)
- Closes the file
- Opens it again and prints each line with a number in front

Expected output:
```
1. Pizza
2. Minecraft
3. ...
```

> **Hint:** Use `open("favourite_things.txt", "w")` to open a file for *writing* (`"w"` mode). Use `open("favourite_things.txt", "r")` to open it for *reading* (`"r"` mode). Use a `with` statement so Python closes the file automatically: `with open("file.txt", "w") as f:` then `f.write("something\n")` inside. The `\n` at the end of each line is the newline character (like pressing Enter).
>
> **Stuck?** Write the "create and write" part first, run it, then check that the file was created in the same folder as your script. Then write the "read and print" part separately.

**Exercise 19**
Write a program that reads `favourite_things.txt` and counts how many things are in the list.
Print: `"You have X favourite things."`

> **Hint:** When you read lines from a file with `f.readlines()`, you get a list — and `len()` of a list gives you the count! Watch out for blank lines at the end of the file that might be counted accidentally.

---

## Section G: Mini Programs

You've learned all the building blocks — now put them together! These exercises combine variables, if/else, loops, lists, functions, and input all at once. Take your time and plan before you start coding.

> **Tip for all mini programs:** Before writing any code, grab a piece of paper and write down the steps in plain English. Then translate each step into Python, one at a time.

**Exercise 20 — Simple Calculator**
Write a calculator program that:
- Asks for two numbers and an operation (`+`, `-`, `*`, `/`)
- Prints the result
- Handles division by zero with a friendly error message
- Keeps running until the user types `quit`

> **Concepts to use:** `while` loop, `input()`, `float()` for conversion, `if/elif/else` for operations, and a special check for division by zero (`if num2 == 0`).
>
> **Stuck?** Build it step by step: first get it working for just `+`, then add `-`, then `*`, then `/`. Add the `while` loop last.

**Exercise 21 — Word Counter**
Write a program that:
- Asks the user to type a sentence
- Counts how many words are in it
- Counts how many characters (including spaces)
- Prints the most common letter

Hint: `sentence.split()` splits by spaces. `sentence.count("a")` counts letter "a".

> **Concepts to use:** `input()`, string methods (`.split()`, `.count()`, `len()`), a `for` loop through the alphabet to find the most common letter.
>
> **Stuck on the most common letter?** Loop through each letter of the alphabet (`"abcdefghijklmnopqrstuvwxyz"`), count how many times it appears in the sentence (use `.lower()` first!), and keep track of which one has the highest count.

**Exercise 22 — Number Stats**
Write a program that:
- Keeps asking the user for numbers until they type `done`
- Then prints: the count, the sum, the average, the minimum, and the maximum
- Handle the case where no numbers were entered

> **Concepts to use:** `while True` loop with a `break`, an empty list `[]` to collect the numbers, `float()` to convert input, and `len()`, `sum()`, `min()`, `max()` on the list at the end.
>
> **Stuck?** Start with just collecting the numbers and printing the list — check that works before adding the stats.

---

## Bonus: RPG Extension Challenges

Extend the RPG battle game from Module 2:

1. Add a **"Run away"** option that has a 50% chance of escaping (use `random.random() < 0.5`)
2. Add a **level-up system**: after winning, the hero's max HP increases by 10 and attack by 2
3. Add a **shop** between battles: spend gold earned from battles on potions or attack upgrades
4. Create a second, harder monster that appears after the hero wins the first fight
5. Save the **high score** (fewest turns to win) to a file called `highscore.txt`
