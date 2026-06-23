# Module 2 Answers — Python

---

## Section A: Variables and Types

**Exercise 1**
```python
name = "Alex"
age = 9
height = 4.5
likes_coding = True

print(f"My name is {name}, I am {age} years old, {height} feet tall, and I like coding: {likes_coding}")
```

**Exercise 2 — Expected Output**
```
13    # 10 + 3
7     # 10 - 3
30    # 10 * 3
3.3333333333333335  # 10 / 3 (always float)
3     # 10 // 3 (floor division — rounds down)
1     # 10 % 3 (remainder: 10 = 3×3 + 1)
1000  # 10 ** 3 (10 to the power of 3)
```

**Exercise 3 — Bug Fix**
The bug: `input()` returns a string, and you can't add 1 to a string. Fix: convert to `int`.
```python
age = int(input("How old are you? "))
next_year = age + 1
print("Next year you will be", next_year)
```

---

## Section B: If / Elif / Else

**Exercise 4**
```python
temp = float(input("Enter the temperature in Fahrenheit: "))

if temp < 32:
    print("Freezing!")
elif temp <= 59:
    print("Cold")
elif temp <= 79:
    print("Warm")
else:
    print("Hot!")
```

**Exercise 5**
```python
password = input("Enter the password: ")

if password == "dragon123":
    print("Access granted!")
    print("SECRET: The treasure is hidden under the third stone.")
else:
    print("Wrong password. Access denied.")
```

**Exercise 6 — Output**
```
C
Done
```
Reason: score is 75. It fails the `>= 90` and `>= 80` checks, but passes `>= 70`, so it prints "C". Then the loop ends and prints "Done".

---

## Section C: Loops

**Exercise 7**
```python
for i in range(1, 11):
    print(i)
```

**Exercise 8**
```python
for i in range(1, 20, 2):
    print(i)
```
Prints: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

**Exercise 9**
```python
coins = 100

while coins >= 0:
    print("Coins remaining:", coins)
    coins -= 7

print("Game over! You ran out of coins.")
```

**Exercise 10 — Loop Tracing**
```
i=1, total=1
i=2, total=3
i=3, total=6
i=4, total=10
i=5, total=15
Final: 15
```
(This is 1+2+3+4+5 = 15)

---

## Section D: Lists and Dictionaries

**Exercise 11**
```python
heroes = ["Spider-Man", "Thor", "Black Widow", "Iron Man", "Hulk"]

print(heroes[0])       # Spider-Man
print(heroes[-1])      # Hulk

heroes.append("Captain America")
heroes.remove("Thor")

print(len(heroes))     # 5
```

**Exercise 12**
```python
numbers = [4, 17, 2, 9, 31]

print(max(numbers))        # 31
print(min(numbers))        # 2
print(sum(numbers))        # 63
print(sorted(numbers))     # [2, 4, 9, 17, 31]
```

**Exercise 13**
```python
character = {
    "name": "Zara",
    "class": "Ranger",
    "level": 5,
    "hp": 80,
    "weapon": "Short Bow"
}

print(f"{character['name']} wields a {character['weapon']}.")

character["weapon"] = "Elven Longbow"
character["gold"] = 250

for key, value in character.items():
    print(f"{key}: {value}")
```

---

## Section E: Functions

**Exercise 14**
```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(37))   # 98.6
```

**Exercise 15**
```python
def is_even(number):
    return number % 2 == 0

for i in range(1, 11):
    if is_even(i):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

**Exercise 16**
```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for s in [95, 83, 71, 64, 42]:
    print(f"{s} → {grade(s)}")
```

**Exercise 17 — Bug Fix**
Two bugs: missing `:` after `def multiply(a, b)` and missing `)` in `multiply(6, 7`.
```python
def multiply(a, b):
    result = a * b
    return result

answer = multiply(6, 7)
print("6 x 7 =", answer)
```

---

## Section F: Files

**Exercise 18**
```python
with open("favourite_things.txt", "w") as f:
    f.write("Pizza\n")
    f.write("Minecraft\n")
    f.write("Coding\n")
    f.write("Dogs\n")
    f.write("Ice cream\n")

with open("favourite_things.txt", "r") as f:
    for number, line in enumerate(f, 1):
        print(f"{number}. {line.strip()}")
```

**Exercise 19**
```python
with open("favourite_things.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

print(f"You have {len(lines)} favourite things.")
```

---

## Section G: Mini Programs

**Exercise 20 — Simple Calculator**
```python
while True:
    user_input = input("\nEnter calculation (e.g. 5 + 3) or 'quit': ").strip()

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    parts = user_input.split()
    if len(parts) != 3:
        print("Please enter: number operator number (e.g. 5 + 3)")
        continue

    try:
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])

        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            if b == 0:
                print("Can't divide by zero!")
            else:
                print(a / b)
        else:
            print(f"Unknown operator: {op}")
    except ValueError:
        print("Please enter valid numbers.")
```

**Exercise 21 — Word Counter**
```python
sentence = input("Type a sentence: ")

words = sentence.split()
word_count = len(words)
char_count = len(sentence)

# Find the most common letter (ignoring spaces)
letters_only = sentence.lower().replace(" ", "")
if letters_only:
    most_common = max(set(letters_only), key=letters_only.count)
else:
    most_common = "none"

print(f"Words: {word_count}")
print(f"Characters: {char_count}")
print(f"Most common letter: '{most_common}'")
```

**Exercise 22 — Number Stats**
```python
numbers = []

while True:
    entry = input("Enter a number (or 'done'): ").strip()
    if entry.lower() == "done":
        break
    try:
        numbers.append(float(entry))
    except ValueError:
        print("That's not a number, try again.")

if not numbers:
    print("No numbers entered.")
else:
    print(f"Count:   {len(numbers)}")
    print(f"Sum:     {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Min:     {min(numbers)}")
    print(f"Max:     {max(numbers)}")
```

---

## Bonus: RPG Extension Challenges

**1. Run Away option**
```python
elif choice == "3":   # Add inside the turn loop
    if random.random() < 0.5:
        print("  💨 You successfully ran away!")
        return
    else:
        print("  ❌ Failed to escape! The monster blocks your path.")
```

**2. Level-up after winning**
```python
# After the battle loop, if hero_hp > 0:
hero_max_hp += 10
hero_atk += 2
print(f"  ⬆️  LEVEL UP! Max HP is now {hero_max_hp}, Attack is now {hero_atk}")
```

**5. Save high score to file**
```python
import os

SCORE_FILE = "highscore.txt"

def save_score(turns):
    best = float("inf")
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE) as f:
            try:
                best = int(f.read().strip())
            except ValueError:
                pass
    if turns < best:
        with open(SCORE_FILE, "w") as f:
            f.write(str(turns))
        print(f"  🏆 NEW HIGH SCORE: {turns} turns!")
    else:
        print(f"  Your score: {turns} turns. Best: {best} turns.")
```
