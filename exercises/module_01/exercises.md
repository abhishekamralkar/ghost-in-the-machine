# Module 1 Exercises — Linux & Git

These exercises are hands-on — most of them ask you to type real commands in your terminal. That is the best way to learn Linux. Don't be afraid to make mistakes in the terminal; you can always try again!

Try each exercise in your terminal. Don't look at the answers until you've tried!

---

## Section A: Command Recall

This section checks that you remember the Linux commands from the lesson. Think of it like a vocabulary quiz, but instead of words you're recalling commands. Try to fill in each blank from memory first — then test it in your terminal to see if it works!

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

> **Tips:**
> - Questions 3 and 4 use the same base command — only a flag changes. Hidden files start with a `.` dot.
> - For question 9, you will need to use `echo` and the `>` redirect symbol to send text into a file.
> - For question 12, "rename" in Linux is done with the `mv` (move) command.
> - For question 15, "manual" = `man`. Type `q` to quit when you are done reading!
>
> **What to do if you're stuck on any command:** Try `man <command>` or type the command with `--help` to see what it does. For example: `ls --help`.

---

## Section B: What Does This Do?

These commands use pipes (`|`) and options you might not have seen before. The goal is to read a command and figure out what it does — like reading a recipe. Read each part of the command from left to right. What does the first part do? Then what does the second part do to that output?

Read each command and describe what it does in plain English.

1. `ls -l | grep ".sh"`

   > **Hint:** `ls -l` gives a detailed list of files. `grep ".sh"` filters to show only lines containing `.sh`. What kind of files end in `.sh`?

   Answer: ________________________________________________

2. `cat notes.txt | wc -l`

   > **Hint:** `cat` prints the file. `wc -l` counts lines. Put them together!

   Answer: ________________________________________________

3. `find . -name "*.py"`

   > **Hint:** `find` searches for files. The `.` means "start from here." The `*` is a wildcard — it matches anything. What kind of files end in `.py`?

   Answer: ________________________________________________

4. `grep -r "dragon" ~/hoard/`

   > **Hint:** `grep` searches for text. The `-r` flag means "search recursively" (inside all sub-folders too). `~/hoard/` is the folder to search in.

   Answer: ________________________________________________

5. `chmod +x myscript.sh`

   > **Hint:** `chmod` changes file permissions. `+x` adds the "execute" permission. What does it mean to be able to execute a file?

   Answer: ________________________________________________

6. `rm -rf old_folder`

   > **Hint:** `rm` removes files. `-r` means "recursively" (everything inside). `-f` means "force" (don't ask for confirmation). Be very careful with this one — there is no recycle bin in Linux!

   Answer: ________________________________________________

---

## Section C: Fix the Bug

Each script below has ONE mistake. Your job is a bug hunt! Read the script carefully from top to bottom. Look at every line — the bug could be a missing word, a wrong symbol, or a capitalisation mistake. Find it, fix it, and write the corrected version below each script.

Each script below has ONE mistake. Find it and write the corrected version.

**Script 1:**
```bash
#!/bin/bash
echo "What is your name"
read name
echo "Hello $Name!"
```

> **Bug hunting hint:** The variable is stored with `read name` using a lowercase `n`. Look at how the variable is used in the last line — is the capitalisation the same? Remember: bash variables are case-sensitive! `$name` and `$Name` are two completely different variables.

**Script 2:**
```bash
#!/bin/bash
for i in 1 2 3 4 5
    echo "Number: $i"
done
```

> **Bug hunting hint:** Look at the `for` loop structure. A bash `for` loop needs a special keyword between the list of numbers and the commands inside it. Check your notes — what keyword goes after the list and before the first command? (Hint: it rhymes with "shoe".)

**Script 3:**
```bash
#!/bin/bash
echo "How old are you?"
read age
if [ $age -ge 10 ]
    echo "You are 10 or older!"
fi
```

> **Bug hunting hint:** Look at the `if` statement. After the condition `[ $age -ge 10 ]`, there is a missing keyword before the command inside the `if`. In bash, you need a special word there — what is it? (Hint: it tells bash "do the next bit".)

---

## Section D: Write the Script

Now it's your turn to be the author! These exercises ask you to write complete bash scripts from scratch. The key commands you learned are: `echo`, `read`, `for`, `if`, `[ ]` for conditions, and `>>` / `>` for writing to files. Make sure your script starts with `#!/bin/bash` on the very first line, and remember to make it executable with `chmod +x scriptname.sh` before running it.

Write a complete shell script for each task. Test it in your terminal.

**Exercise 1 — Greeting Script**

> **Before you start:** You will need `echo` to ask questions, `read` to capture the answers into variables, and `echo` again to print the final message. Use `$variablename` to insert a variable's value into a string.

Write a script called `greet.sh` that:
- Asks for the user's name
- Asks for their favourite colour
- Prints: `"Hello [name]! [colour] is a great colour."`

**Exercise 2 — Countdown**

> **Before you start:** You will need a `for` loop. The list of numbers in the loop goes from 10 down to 1 — you write them out in order. After the loop, use `echo` to print the final message. Don't forget `do` and `done`!

Write a script called `countdown.sh` that:
- Counts down from 10 to 1
- Prints `"BLAST OFF!"` at the end
- Hint: use a `for` loop with `for i in 10 9 8 7 6 5 4 3 2 1`

**Exercise 3 — Even Numbers**

> **Before you start:** This is similar to the countdown, but this time your list only contains even numbers. The loop variable `$i` will hold each number as you go through the list. Use `echo $i` inside the loop to print it.

Write a script called `evens.sh` that prints all even numbers from 2 to 20.
Hint: use `for i in 2 4 6 8 10 12 14 16 18 20`

**Exercise 4 — File Checker**

> **Before you start:** You will need `read` to get the filename, and an `if`/`else`/`fi` block to check it. The condition `-f "$filename"` checks if a regular file exists. Always put variable names in quotes inside `[ ]` — this is a good habit that prevents bugs.

Write a script called `check.sh` that:
- Asks for a filename
- Checks if the file exists using `if [ -f "$filename" ]`
- Prints "File found!" or "File not found!" accordingly

> **What to do if you're stuck:** Write just the `echo` and `read` part first, then add the `if` block. Test each small piece before adding the next one. Small steps!

---

## Section E: Git Practice

Git is the tool that professional developers use to save their work and track every change they make — like a super-powered undo history. This section walks you through a real Git workflow. Do each step in order in your terminal and write down what you see. Pay attention to the colours and messages Git shows you!

Do each step in your terminal and write what you see.

1. Create a new directory called `~/git_practice` and go into it.

   > **Tip:** You will need two commands: `mkdir` to create the folder and `cd` to go into it.

2. Run `git init`. What does it print?

   > **Tip:** This sets up a hidden `.git` folder that tracks all your changes. You only need to run `git init` once per project.

3. Create a file called `hero.txt` with `echo "My hero is a wizard" > hero.txt`

4. Run `git status`. What colour is `hero.txt` and what does that mean?

   > **Tip:** Red means Git can see the file but is not tracking it yet. Green means it is staged and ready to be committed.

5. Run `git add hero.txt`, then `git status` again. What changed?

   > **Tip:** `git add` moves a file from "untracked" to "staged." Think of it like putting your homework in your bag before handing it in.

6. Run `git commit -m "add hero description"`. What does it print?

   > **Tip:** A commit is like taking a snapshot. The `-m` flag lets you add a message describing what you changed. Always write a short, clear message!

7. Change `hero.txt`: `echo "My hero has a magic sword" >> hero.txt`

   > **Tip:** The `>>` (two arrows) ADDS to the end of the file. A single `>` would overwrite the whole file. Make sure you use two!

8. Run `git diff`. What do you see?

   > **Tip:** Lines starting with `+` in green are new additions. Lines starting with `-` in red are removed lines. This shows exactly what changed.

9. Stage and commit this change with a good message.

   > **Tip:** Use `git add hero.txt` then `git commit -m "your message here"`. Write a message that describes what you changed, like `"add sword description"`.

10. Run `git log --oneline`. How many commits do you see?

    > **Tip:** You should see 2 commits — one from step 6 and one from step 9. The newest one is at the top.

---

## Section F: Pipe Challenge

Pipes (`|`) are one of the most powerful ideas in Linux. They let you chain commands together so the output of one command becomes the input of the next. Think of it like an assembly line! These challenges ask you to combine what you know into a single command.

Use pipes `|` to answer each question with ONE command:

1. List all files in `/etc` and count how many there are.
   Hint: `ls /etc | wc -l`

   > **Tip:** `wc -l` counts lines. Since each file is on its own line in the `ls` output, this gives you the total number of files.

2. Show only the first 3 lines of `/etc/os-release`.
   Hint: use `cat` and `head`

   > **Tip:** `head -n 3` shows the first 3 lines of whatever comes into it. Try `cat /etc/os-release | head -n 3`.

3. List all running processes and search for `python`.
   Hint: `ps aux | grep python`

   > **Tip:** Don't be surprised if you see the `grep python` command itself in the results — grep finds itself! That is normal.

---

## Bonus: Dragon Hoard Challenge

You already built the Dragon Hoard system in the module. Now it is time to level it up! These exercises are more open-ended — there is no single right answer. Use the commands and ideas from the whole module. Try each one, test it, and make sure it actually works before you call it done.

Add these features to the Dragon Hoard system from the module:

1. Write a script `count_items.sh` that counts the total number of `.txt` files across all hoard categories and prints: `"The dragon owns X items."`

   > **Hint:** Use `find ~/hoard -name "*.txt" | wc -l` inside your script to count the files, then store the result in a variable and use `echo` to print it.

2. Write a script `biggest_category.sh` that finds which category has the most items.

   > **Hint:** You might use a `for` loop to go through each category folder and count its files. Then compare the counts. This one is tricky — try it step by step!
   >
   > **What to do if you're stuck:** Start simpler. Can you write a script that just prints how many files are in ONE category? Get that working first, then add the loop.

3. Modify `add_item.sh` to automatically add a date stamp to every item using `$(date)`.

   > **Hint:** `$(date)` runs the `date` command and inserts its output. You can use it inside a string like this: `echo "Added on: $(date)"`. Try adding the date to the item name or inside the file itself.
