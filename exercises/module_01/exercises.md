# Module 1 Exercises — Linux & Git

Try each exercise in your terminal. Don't look at the answers until you've tried!

---

## Section A: Command Recall

Write the Linux command that does each thing:

1. Print your username to the screen: `__________`
2. Show which directory you are currently in: `__________`
3. List all files in the current directory: `__________`
4. List all files including hidden ones: `__________`
5. Create a new directory called `lab`: `__________`
6. Go into the `lab` directory: `__________`
7. Go back up one directory level: `__________`
8. Create an empty file called `test.txt`: `__________`
9. Write the text `"hello"` into `test.txt`: `__________`
10. Read and print the contents of `test.txt`: `__________`
11. Copy `test.txt` to `backup.txt`: `__________`
12. Rename `backup.txt` to `copy.txt`: `__________`
13. Delete `copy.txt`: `__________`
14. Search for the word `"hello"` inside `test.txt`: `__________`
15. Read the manual for the `ls` command: `__________`

---

## Section B: What Does This Do?

Read each command and describe what it does in plain English.

1. `ls -l | grep ".sh"`
   Answer: ________________________________________________

2. `cat notes.txt | wc -l`
   Answer: ________________________________________________

3. `find . -name "*.py"`
   Answer: ________________________________________________

4. `grep -r "dragon" ~/hoard/`
   Answer: ________________________________________________

5. `chmod +x myscript.sh`
   Answer: ________________________________________________

6. `rm -rf old_folder`
   Answer: ________________________________________________

---

## Section C: Fix the Bug

Each script below has ONE mistake. Find it and write the corrected version.

**Script 1:**
```bash
#!/bin/bash
echo "What is your name"
read name
echo "Hello $Name!"
```

**Script 2:**
```bash
#!/bin/bash
for i in 1 2 3 4 5
    echo "Number: $i"
done
```

**Script 3:**
```bash
#!/bin/bash
echo "How old are you?"
read age
if [ $age -ge 10 ]
    echo "You are 10 or older!"
fi
```

---

## Section D: Write the Script

Write a complete shell script for each task. Test it in your terminal.

**Exercise 1 — Greeting Script**
Write a script called `greet.sh` that:
- Asks for the user's name
- Asks for their favourite colour
- Prints: `"Hello [name]! [colour] is a great colour."`

**Exercise 2 — Countdown**
Write a script called `countdown.sh` that:
- Counts down from 10 to 1
- Prints `"BLAST OFF!"` at the end
- Hint: use a `for` loop with `for i in 10 9 8 7 6 5 4 3 2 1`

**Exercise 3 — Even Numbers**
Write a script called `evens.sh` that prints all even numbers from 2 to 20.
Hint: use `for i in 2 4 6 8 10 12 14 16 18 20`

**Exercise 4 — File Checker**
Write a script called `check.sh` that:
- Asks for a filename
- Checks if the file exists using `if [ -f "$filename" ]`
- Prints "File found!" or "File not found!" accordingly

---

## Section E: Git Practice

Do each step in your terminal and write what you see.

1. Create a new directory called `~/git_practice` and go into it.
2. Run `git init`. What does it print?
3. Create a file called `hero.txt` with `echo "My hero is a wizard" > hero.txt`
4. Run `git status`. What colour is `hero.txt` and what does that mean?
5. Run `git add hero.txt`, then `git status` again. What changed?
6. Run `git commit -m "add hero description"`. What does it print?
7. Change `hero.txt`: `echo "My hero has a magic sword" >> hero.txt`
8. Run `git diff`. What do you see?
9. Stage and commit this change with a good message.
10. Run `git log --oneline`. How many commits do you see?

---

## Section F: Pipe Challenge

Use pipes `|` to answer each question with ONE command:

1. List all files in `/etc` and count how many there are.
   Hint: `ls /etc | wc -l`

2. Show only the first 3 lines of `/etc/os-release`.
   Hint: use `cat` and `head`

3. List all running processes and search for `python`.
   Hint: `ps aux | grep python`

---

## Bonus: Dragon Hoard Challenge

Add these features to the Dragon Hoard system from the module:

1. Write a script `count_items.sh` that counts the total number of `.txt` files across all hoard categories and prints: `"The dragon owns X items."`

2. Write a script `biggest_category.sh` that finds which category has the most items.

3. Modify `add_item.sh` to automatically add a date stamp to every item using `$(date)`.
