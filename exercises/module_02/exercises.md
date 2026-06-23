# Module 2 Exercises — Python

Open VS Code, create a new `.py` file for each section, and run it with `python3`.

---

## Section A: Variables and Types

**Exercise 1**
Create variables for:
- Your name (string)
- Your age (integer)
- Your height in feet (float)
- Whether you like coding (boolean)

Then print a sentence using all four variables with an f-string.

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

**Exercise 3**
Fix the bug in this code:
```python
age = input("How old are you? ")
next_year = age + 1
print("Next year you will be", next_year)
```

---

## Section B: If / Elif / Else

**Exercise 4**
Write a program that:
- Asks the user for a temperature (in Fahrenheit)
- Prints `"Freezing!"` if below 32
- Prints `"Cold"` if 32–59
- Prints `"Warm"` if 60–79
- Prints `"Hot!"` if 80 or above

**Exercise 5**
Write a program that asks for a password.
- If the password is `"dragon123"`, print `"Access granted!"` and a secret message of your choice.
- Otherwise, print `"Wrong password. Access denied."`

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

---

## Section C: Loops

**Exercise 7**
Write a `for` loop that prints the numbers 1 through 10, one per line.

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

**Exercise 10 — Loop Tracing**
What does this print? Write it out before running.

```python
total = 0
for i in range(1, 6):
    total = total + i
    print(f"i={i}, total={total}")
print("Final:", total)
```

---

## Section D: Lists and Dictionaries

**Exercise 11**
Create a list called `heroes` with 5 superhero names.
- Print the first hero
- Print the last hero using a negative index
- Add a new hero to the end
- Remove the second hero
- Print the total number of heroes remaining

**Exercise 12**
Write a program that:
- Creates a list of 5 numbers: `[4, 17, 2, 9, 31]`
- Prints the largest number
- Prints the smallest number
- Prints the sum
- Prints the list sorted from smallest to largest

**Exercise 13**
Create a dictionary for a video game character with:
- `name`, `class`, `level`, `hp`, `weapon`

Then:
- Print the character's name and weapon in a sentence
- Change their weapon to something better
- Add a new key `"gold"` with a value of `250`
- Print all keys and values using a loop

---

## Section E: Functions

**Exercise 14**
Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.
Formula: `F = (C × 9/5) + 32`

Test it with: 0°C, 100°C, 37°C (body temperature).

**Exercise 15**
Write a function `is_even(number)` that returns `True` if the number is even, `False` if odd.
Then use it in a loop to print "even" or "odd" for every number 1–10.

**Exercise 16**
Write a function `grade(score)` that takes a number and returns the letter grade:
- 90–100 → "A"
- 80–89 → "B"
- 70–79 → "C"
- 60–69 → "D"
- Below 60 → "F"

Test it on scores: 95, 83, 71, 64, 42.

**Exercise 17 — Fix the Bug**
```python
def multiply(a, b)
    result = a * b
    return result

answer = multiply(6, 7
print("6 x 7 =", answer)
```

---

## Section F: Files

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

**Exercise 19**
Write a program that reads `favourite_things.txt` and counts how many things are in the list.
Print: `"You have X favourite things."`

---

## Section G: Mini Programs

**Exercise 20 — Simple Calculator**
Write a calculator program that:
- Asks for two numbers and an operation (`+`, `-`, `*`, `/`)
- Prints the result
- Handles division by zero with a friendly error message
- Keeps running until the user types `quit`

**Exercise 21 — Word Counter**
Write a program that:
- Asks the user to type a sentence
- Counts how many words are in it
- Counts how many characters (including spaces)
- Prints the most common letter

Hint: `sentence.split()` splits by spaces. `sentence.count("a")` counts letter "a".

**Exercise 22 — Number Stats**
Write a program that:
- Keeps asking the user for numbers until they type `done`
- Then prints: the count, the sum, the average, the minimum, and the maximum
- Handle the case where no numbers were entered

---

## Bonus: RPG Extension Challenges

Extend the RPG battle game from Module 2:

1. Add a **"Run away"** option that has a 50% chance of escaping (use `random.random() < 0.5`)
2. Add a **level-up system**: after winning, the hero's max HP increases by 10 and attack by 2
3. Add a **shop** between battles: spend gold earned from battles on potions or attack upgrades
4. Create a second, harder monster that appears after the hero wins the first fight
5. Save the **high score** (fewest turns to win) to a file called `highscore.txt`
