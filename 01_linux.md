# Module 1: Linux — Talking to Your Computer Like a Pro

```
LEVEL 1 UNLOCKED: Hacker Mode
==============================
Most people use computers with a mouse and pretty buttons.
You're about to learn to talk directly to the machine.
No mouse. Just words. The computer obeys.
```

## What Is Linux?

Linux is a **free operating system** — the software that runs your computer.
You probably use Windows or macOS. Linux is the third big one, and it powers:

- Most websites on the internet (Google, YouTube, Amazon)
- Android phones
- Raspberry Pi
- Supercomputers and **actual space robots** (the Mars rovers run Linux!)

The coolest part of Linux is the **terminal** — a text window where you type
commands and the computer obeys instantly. No mouse needed. It looks exactly
like what hackers use in movies — because it IS what hackers (and engineers) use.

> **Fun Fact:** The International Space Station switched to Linux in 2013. Astronauts
> use the same commands you're about to learn! 🚀

---

## Week 1: Finding Your Way Around

### Lesson 1.1 — Opening the Terminal

The terminal is your direct line to the computer. Think of it like a chat window — except instead of texting a friend, you're texting the computer itself. It does exactly what you say, instantly. No clicking through menus. No waiting. Just you and the machine talking. This is how professional engineers and hackers in movies get things done — and now you will too.

On most Linux systems, press `Ctrl + Alt + T` to open a terminal.
You'll see something like:

```
aaa@mycomputer:~$
```

- `aaa` — your username (your hacker alias!)
- `mycomputer` — your computer's name
- `~` — you are in your home directory (your base!)
- `$` — the computer is waiting for your command

> Think of the `$` prompt like a video game waiting for your input.
> You type a command, the game responds. You're in control.

**What you should see:** A blinking cursor after the `$`. That means the terminal is alive and ready. If you see it, you're in!

**Try this!** Look at your username in the prompt. That's your Linux identity. Try pressing **Enter** without typing anything — the computer just shows you a new prompt line. It's patiently waiting. It never gets bored.

---

### Lesson 1.2 — Your First Commands

Every journey starts with a first step. These four commands are the handshake between you and Linux. They don't DO anything dangerous — they just ask the computer questions. `echo` makes the computer speak. `whoami` tells you your identity. `pwd` tells you where you are. `date` tells you when it is. Simple, powerful, fun.

Type each command and press **Enter**. Read what happens.

```bash
# Print a message on screen
echo "Hello, I am a Linux user!"

# Find out who you are
whoami

# Find out where you are (print working directory)
pwd

# See what date and time it is
date
```

**What you should see:** Something like this (your details will be different):

```
Hello, I am a Linux user!
aaa
/home/aaa
Thu Jun 26 10:32:15 UTC 2026
```

Each command answered your question instantly. That's the power of the terminal — direct answers, no loading screens.

**Challenge 1:** Make the computer say your name using `echo`.

**Challenge 2 (Hacker Edition):** Can you make the terminal say this?
```
**********************
*  SYSTEM ACTIVATED  *
*  WELCOME, HACKER!  *
**********************
```
Hint: you need four `echo` commands, one for each line.

**Try this!** Run `echo $USER` — that's a special variable Linux already knows. It automatically contains your username. Variables in Linux always start with `$`. Keep that in mind for later!

---

### Lesson 1.3 — Files and Directories

Everything in Linux lives in **directories**.
Think of it like a filing cabinet.

In Minecraft, you have chests organized by what's inside — one for wood, one for tools, one for food. Linux directories are exactly like that. Every file lives in a folder (called a directory), and folders can be inside other folders. The `ls` command is how you peek inside a chest and see what's there.

```bash
# List files and directories in the current directory
ls

# List with more details (size, date, permissions)
ls -l

# List including hidden files (files starting with a dot)
ls -a
```

**What you should see:** Running plain `ls` shows you the names of files and folders. Running `ls -l` shows you a detailed table. Running `ls -a` reveals hidden files that start with a dot (`.`) — those are usually settings files that stay out of the way.

**What you'll see in `ls -l`:**

```
drwxr-xr-x  2  aaa  aaa  4096  Jun 10  documents
-rw-r--r--  1  aaa  aaa   128  Jun 10  notes.txt
```

Breaking down each column:

```
drwxr-xr-x   2   aaa   aaa   4096   Jun 10   documents
│└────────┘   │   │     │     │      │        └── name
│ permissions │   │     │     │      └── last modified date
│             │   │     │     └── size in bytes
│             │   │     └── group owner
│             │   └── owner (that's you!)
│             └── number of links (ignore for now)
└── d = directory, - = file
```

The **permissions** block (`rwxr-xr-x`) uses three letters repeated three times:
- `r` = **r**ead (look inside)
- `w` = **w**rite (change it)
- `x` = e**x**ecute (run it as a program)
- `-` = that permission is turned OFF

The three groups are: **owner** | **group** | **everyone else**

```
rwx  r-x  r-x
│    │    └── everyone else: can read and run, but NOT write
│    └── group: can read and run, but NOT write
└── owner (you): can read, write, AND run
```

**Try this!** Run `ls -lh` — the `-h` flag makes file sizes human-readable (like `4.0K` instead of `4096`). Flags are like cheat codes you add to commands!

---

### Lesson 1.4 — Moving Around

If directories are like rooms in a building, then `cd` is how you walk between them. Right now you start in your home directory (the `~` room). The whole Linux system is one giant building of rooms inside rooms. You can walk forward into a room, back out to the hallway (`..`), or teleport straight home (`~`) no matter where you are. Navigating the terminal is like reading a map — once you know where you are, you know where to go.

```bash
# Change directory (go into a directory)
cd documents

# Go back up one level (to the parent directory)
cd ..

# Go straight home no matter where you are
cd ~

# Go to the root of the whole computer
cd /
```

**What you should see:** After each `cd` command, run `pwd` to confirm where you ended up. After `cd ~` you'll see `/home/yourname`. After `cd /` you'll see just `/` — that's the very top of the entire filesystem, like the lobby of the building.

**Challenge:** Start at home (`~`), go into `/tmp`, list the files, then go back home.

**Try this!** After `cd /`, run `ls` to see the top-level directories of Linux. You'll see folders like `bin`, `home`, `etc`, `var`. Every file on the entire computer lives somewhere under `/`. It's like seeing the whole map of the building from above!

---

### Lesson 1.5 — Making and Removing Things

Now you can do something real — create and destroy. This is where Linux starts to feel like actual power. You're not just looking at things — you're building your own corner of the filesystem. Creating directories is like placing rooms. Creating files is like placing signs. And `rm` is like the TNT of Linux — it blows things up with no warning and no undo. Use it carefully!

```bash
# Make a new directory
mkdir my_cool_directory

# Go into it
cd my_cool_directory

# Create an empty file
touch hello.txt

# Write something into a file
echo "This is my first file!" > hello.txt

# Read what's in a file
cat hello.txt

# Remove a file (careful — no undo!)
rm hello.txt

# Go back up before removing the directory
cd ..

# Remove an empty directory
rmdir my_cool_directory

# Remove a directory and everything inside it (very careful!)
# Only use this if the directory still has files in it
rm -rf my_cool_directory
```

**What you should see:** After `cat hello.txt`, you'll see:

```
This is my first file!
```

That's text you wrote into a file using `echo` and the `>` symbol. The `>` means "send output INTO this file." It's like pouring water into a cup instead of onto the floor.

> **Safety Rule:** `rm -rf` deletes forever. Always double-check before using it.

**Try this!** Use `echo "more stuff" >> hello.txt` (two `>` symbols instead of one) before you delete the file. Then `cat hello.txt` again. See what happened? Two `>` means APPEND (add to the end). One `>` means OVERWRITE (replace everything). That's a big difference!

---

### Lesson 1.6 — Copying and Moving Files

Making things is great — but sometimes you want a backup copy, or you want to rename something. `cp` and `mv` are your tools for that. Think of `cp` like duplicating a Minecraft item using creative mode — you get two of it. Think of `mv` like picking something up and placing it somewhere else — or just giving it a new name. These two commands do a LOT of the everyday work in real engineering.

```bash
# Copy a file
cp original.txt backup.txt

# Move (or rename) a file
mv old_name.txt new_name.txt

# Copy a whole directory
cp -r my_directory my_directory_backup
```

**What you should see:** After `cp original.txt backup.txt`, run `ls` — you'll see both files exist. After `mv old_name.txt new_name.txt`, run `ls` again — the old name is gone, replaced by the new one. The `-r` flag on `cp` means "recursive" — copy the directory AND everything inside it.

**Try this!** Create a file called `test.txt`, write something in it, then copy it to `test_backup.txt`. Now edit `test.txt` using `echo "new content" > test.txt`. Check both files with `cat`. Notice that `test_backup.txt` still has the old content — that's why backups matter!

---

## Week 2: Becoming a Power User

### Lesson 2.1 — Finding Things

What happens when you have hundreds of files and you can't remember where something is? You search! `find` is like using a search bar in Windows — except it works on the terminal and it's incredibly powerful. `grep` is even cooler — it searches INSIDE files for specific words. Imagine being able to search every file on your computer for a single word in under a second. That's what `grep` does. Real engineers use these commands constantly.

```bash
# Search for a file by name
find . -name "hello.txt"

# Search for text inside files
grep "python" my_notes.txt

# Search recursively in all files in a directory
grep -r "hello" ~/documents/
```

**What you should see:** `find` prints the path to every matching file, like `./documents/hello.txt`. `grep` prints every line in the file that contains your search word, with the filename in front. If nothing matches, it shows nothing — silence means "not found."

**Try this!** Run `grep -r "the" ~/` — this searches for the word "the" in EVERY file in your home directory. It'll probably find a lot of matches! Now try `grep -r -l "the" ~/` — the `-l` flag shows just the filenames instead of every matching line. Much cleaner!

---

### Lesson 2.2 — The Manual (Your Superpower)

Every command has a manual. Type `man` before any command:

Here's the secret that separates real engineers from beginners: they don't memorize everything. They know HOW to find answers. The `man` command is a built-in help system for every single Linux command. It's like having the instruction booklet for every tool right there in the terminal. Whenever you see a flag you don't recognize — like `-r` or `-h` — look it up in `man` and you'll understand it in seconds.

```bash
man ls
man echo
man grep
```

**What you should see:** A full-screen document with the command's description, options, and examples. It looks like a book page. Scroll through it to see all the flags available.

Press `q` to quit the manual. Press spacebar to scroll down.

**Try this!** Run `man man` — yes, the manual has a manual for itself! Read the first paragraph. Then press `q` to exit. Now try `ls --help` — many commands also have a quick `--help` flag that gives a shorter summary right in the terminal.

---

### Lesson 2.3 — Piping (Chaining Commands Together)

The `|` symbol (called a **pipe**) sends the output of one command into another.

This is one of the coolest ideas in all of computing. Instead of one giant command that does everything, Linux gives you small focused commands and lets you chain them together. It's like a factory assembly line — one machine does step one, hands the result to the next machine, which does step two, and so on. You can build incredibly powerful combinations from simple pieces.

```bash
# List files, then filter to only show .txt files
ls -l | grep ".txt"

# Count how many lines are in a file
cat notes.txt | wc -l

# See the first 5 lines of a file
cat long_file.txt | head -5

# See the last 5 lines
cat long_file.txt | tail -5
```

**What you should see:** With `ls -l | grep ".txt"`, only lines containing `.txt` appear — everything else is filtered out. With `cat notes.txt | wc -l`, you get a single number — the total line count of the file. `head -5` shows lines 1 through 5. `tail -5` shows the last 5.

**Try this!** Run `ls -l ~ | wc -l` to count how many items are in your home directory. Then try `ls -l ~ | grep "^d"` — that `^d` means "lines starting with d" which means directories only. You just filtered a list using a pattern!

---

### Lesson 2.4 — Permissions

Every file has rules about who can read, write, or run it.

Think of file permissions like the lock system in a video game dungeon. Some doors (files) only you can open. Some doors everyone can walk through. Some are locked to everyone except the admin. Linux uses a simple three-letter system (`rwx`) to control all of this. Understanding permissions means you know who can touch your files — and you can change those rules anytime.

```bash
# See permissions
ls -l

# Make a file executable (runnable)
chmod +x my_script.sh

# Make a file read-only (no changes allowed)
chmod 444 important.txt
```

**What you should see:** After `chmod +x my_script.sh`, run `ls -l my_script.sh` — you'll see the permissions changed to include `x`. It now shows something like `-rwxr-xr-x` instead of `-rw-r--r--`. That `x` is what lets you run it with `./my_script.sh`.

Permission letters:
- `r` = read
- `w` = write
- `x` = execute (run)

**Try this!** Create a file called `secret.txt` and write something in it. Then run `chmod 000 secret.txt` — that removes ALL permissions from everyone. Try `cat secret.txt` now. You'll get "Permission denied" — even from yourself! Fix it with `chmod 644 secret.txt` to get normal permissions back.

---

### Lesson 2.5 — Writing Your First Shell Script

A shell script is a text file full of commands. The computer runs them all in order.

This is huge. Up until now, you've typed one command at a time. A shell script lets you write MANY commands into a file — and run them all at once just by typing the filename. It's like programming a robot with a list of instructions. This is how real system administrators automate boring jobs: instead of typing the same 10 commands every morning, they write a script and run it in one shot.

**Quick nano guide** (nano is the text editor you'll use):

| Key | What it does |
|-----|-------------|
| Just type | Writes text at the cursor |
| Arrow keys | Move around |
| `Ctrl+S` | Save the file |
| `Ctrl+X` | Exit (it will ask to save if you haven't) |
| `Y` then `Enter` | Confirm save when exiting |

**Step 1:** Create the file

```bash
nano my_first_script.sh
```

**Step 2:** Type this inside nano:

> The first line `#!/bin/bash` is called a **shebang**. It tells Linux "run this file
> using the bash shell." Always put it at the top of every shell script.

```bash
#!/bin/bash
# This is a comment — the computer ignores it

echo "==========================="
echo "  Hello from my script!    "
echo "==========================="
echo ""
echo "Today is:"
date
echo ""
echo "You are logged in as:"
whoami
echo ""
echo "You are in this directory:"
pwd
```

**Step 3:** Save and exit nano: press `Ctrl+X`, then `Y`, then `Enter`

**Step 4:** Make it runnable and run it:

```bash
chmod +x my_first_script.sh
./my_first_script.sh
```

**What you should see:**

```
===========================
  Hello from my script!
===========================

Today is:
Thu Jun 26 10:45:00 UTC 2026

You are logged in as:
aaa

You are in this directory:
/home/aaa
```

Every line of output came from your script running each command in order — like a playlist playing songs one after another.

**Try this!** Add more lines to your script! Open it with `nano my_first_script.sh` again and add `echo "My hostname is: $(hostname)"` near the bottom. Save, run it again. You can add as many commands as you want — scripts can be thousands of lines long.

---

### Lesson 2.6 — Variables and User Input in Shell

In shell scripts, variables store information just like in Python — but with two differences:
- **No spaces** around the `=` sign: `name="Alex"` ✓ &nbsp;&nbsp; `name = "Alex"` ✗
- To **use** a variable, put `$` in front of the name: `$name`

Variables are like labeled boxes. You put something in the box, give it a name, and later you can open that box and use what's inside. The `read` command is magic — it PAUSES your script and waits for the person running it to type something. That's how you make interactive programs that feel like a real app. Think of it like an RPG asking "What is your character's name?"

```bash
#!/bin/bash

# Ask the user for their name
echo "What is your name?"
read user_name          # 'read' waits for the user to type something

# Use the variable with $
echo "Hello, $user_name! Welcome to Linux!"

# Variables can store numbers too
my_number=42
echo "My favorite number is $my_number"
```

**What you should see:** The script pauses after "What is your name?" and waits. When you type your name and hit Enter, it greets you with it. Your input becomes the value of `$user_name` — the box now holds your name.

```
What is your name?
Alex
Hello, Alex! Welcome to Linux!
My favorite number is 42
```

**Try this!** Add a second question: ask for the user's favorite color and store it in `$favorite_color`. Then print `"Your favorite color is $favorite_color — great choice!"`. You just made a real interactive program!

---

### Lesson 2.7 — If/Else in Shell Scripts

Now your scripts can make decisions. This is where programs get smart. An `if` statement is like a fork in the road — the computer checks a condition, and if it's true, it goes left; if it's false, it goes right. You've seen this in Scratch or Python. Shell scripts work the same way, just with slightly different symbols. Once you know `if/else`, your scripts can react differently depending on what the user types.

```bash
#!/bin/bash

echo "How old are you?"
read age

if [ $age -ge 10 ]; then
    echo "You are 10 or older!"
else
    echo "You are younger than 10!"
fi
```

**What you should see:** If you type `9`, the script says "You are younger than 10!" If you type `10` or more, it says "You are 10 or older!" The script reacts to YOUR input. That's a real program.

- `-ge` means "greater than or equal to"
- `-eq` means "equal to"
- `-lt` means "less than"

**Try this!** Add an `elif` branch to handle exactly age 10:

```bash
if [ $age -gt 10 ]; then
    echo "You are older than 10!"
elif [ $age -eq 10 ]; then
    echo "You are exactly 10 — double digits!"
else
    echo "You are younger than 10!"
fi
```

`elif` means "else if" — a middle option between the first condition and the final `else`. Now your script has THREE possible paths!

---

### Lesson 2.8 — Loops in Shell Scripts

What if you need to do the same thing 100 times? You don't type it 100 times — you write a loop. A `for` loop is like a conveyor belt in a factory: you set it up once, and it runs the same action over and over, changing only what's different each time. Loops are one of the most powerful ideas in ALL of programming — master this and you can automate almost anything.

```bash
#!/bin/bash

# Count from 1 to 5
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

# Loop through files
for file in *.txt; do
    echo "Found file: $file"
done
```

**What you should see:** The first loop prints:

```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

The second loop finds every `.txt` file in the current directory and prints its name. If you have three `.txt` files, you get three lines. The loop runs once for EACH file automatically.

**Try this!** Change `1 2 3 4 5` to `Monday Tuesday Wednesday Thursday Friday` and change the echo message to `"Day: $i"`. Loops work with words too, not just numbers! Now try counting to 10 by adding more numbers. Or to really level up, use `{1..10}` instead of listing them all — that's a shortcut for "1 through 10."

---

## Mini Project: System Info Script

Build a script that shows:
1. Your username
2. The date and time
3. How much disk space is left
4. The 5 newest files in your home directory

You've learned all the pieces — `whoami`, `date`, `df`, and `ls`. Now you're combining them into a single polished script that gives a complete status report. Real engineers write scripts exactly like this to check server health. Yours will run on your own computer. This is your first real sysadmin tool!

```bash
#!/bin/bash

echo "=============================="
echo "   MY COMPUTER STATUS REPORT  "
echo "=============================="
echo ""
echo "User:    $(whoami)"
echo "Date:    $(date)"
echo ""
echo "-- Disk Space --"
df -h ~
echo ""
echo "-- 5 Newest Files in Home --"
ls -lt ~ | head -6
echo ""
echo "=============================="
echo "End of report"
echo "=============================="
```

**What you should see:** A formatted status report that looks like this (your details will vary):

```
==============================
   MY COMPUTER STATUS REPORT
==============================

User:    aaa
Date:    Thu Jun 26 10:55:00 UTC 2026

-- Disk Space --
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   12G   36G  25% /home/aaa

-- 5 Newest Files in Home --
total 48
drwxr-xr-x  5 aaa aaa 4096 Jun 26 10:30 documents
-rw-r--r--  1 aaa aaa  128 Jun 26 10:28 notes.txt
...

==============================
End of report
==============================
```

The `$(command)` syntax is called **command substitution** — it runs a command and drops the output right into your string. Very powerful!

**Try this!** Add a new section to the script that shows your computer's memory usage. Add these lines after the disk space section:

```bash
echo ""
echo "-- Memory Usage --"
free -h
```

`free -h` shows how much RAM is being used. Now your script is a proper system health dashboard!

---

## Week 2 Bonus: Git — Never Lose Your Work Again

### What Is Git?

**Git** is a tool that remembers every version of your code.
Imagine you're writing a story and you save a copy every time you finish a paragraph.
If you ruin it later, you can go back to any earlier copy. Git does this automatically.

Developers use git on every real project in the world. Learning it now puts you ahead.

### Key Concepts

- **Repository (repo):** A project directory that git is tracking
- **Commit:** A saved snapshot of your files at a point in time
- **History:** The list of all your commits — like a timeline

---

### Lesson G.1 — Setting Up Git

Install git (if not already installed):

```bash
sudo apt install git -y
```

Tell git who you are (do this once):

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

### Lesson G.2 — Starting a Repository

```bash
# Go into your project directory
cd ~/notebook

# Tell git to start tracking this directory
git init
```

You'll see: `Initialized empty Git repository in ~/notebook/.git/`

That hidden `.git` directory is where git stores all the history.

---

### Lesson G.3 — Your First Commit

```bash
# See what git knows about your files
git status
```

Files shown in red are **untracked** — git sees them but isn't saving them yet.

```bash
# Stage all files (tell git "I want to save these")
git add .

# Check again — files should now be green
git status

# Save a snapshot with a message describing what you did
git commit -m "First commit: added notebook scripts"
```

**The commit message is for future-you.** Write something that explains what changed.

---

### Lesson G.4 — Making More Commits

The workflow is always the same:

```
1. Change some files
2. git add <filename>   (or git add . for everything)
3. git commit -m "describe what you changed"
4. Repeat
```

```bash
# Example: you improved add_note.sh
git add add_note.sh
git commit -m "add date stamp to notes in add_note.sh"
```

---

### Lesson G.5 — Viewing History

```bash
# See all your commits
git log

# Shorter version — one line per commit
git log --oneline
```

You'll see something like:

```
a3f9c12 add date stamp to notes in add_note.sh
b1e2044 add search feature to notebook
7d8f3a1 First commit: added notebook scripts
```

Each line is a commit. The weird letters/numbers are the commit's unique ID.

---

### Lesson G.6 — Seeing What Changed

```bash
# See changes you made but haven't committed yet
git diff

# See what's staged and ready to commit
git diff --staged
```

---

### Lesson G.7 — Going Back in Time

```bash
# See a file as it was in a previous commit
git show 7d8f3a1:add_note.sh

# Undo changes to a file before you've committed
git restore add_note.sh
```

> **Rule:** Always commit before you do something risky. Then you can always go back.

---

### Git Workflow Summary

```
┌─────────────────────────────────────────────────────┐
│                   GIT WORKFLOW                       │
│                                                      │
│  Edit files                                          │
│       ↓                                              │
│  git add <files>    ← stage your changes             │
│       ↓                                              │
│  git commit -m ""   ← save a snapshot                │
│       ↓                                              │
│  git log            ← see your history               │
│       ↓                                              │
│  repeat forever                                      │
└─────────────────────────────────────────────────────┘
```

---

## Linux Cheat Sheet

| Command | What It Does |
|---------|-------------|
| `pwd` | Show current directory |
| `ls` | List files |
| `cd dirname` | Go into a directory |
| `cd ..` | Go up one level |
| `mkdir name` | Make a directory |
| `touch file` | Make an empty file |
| `cat file` | Show file contents |
| `cp a b` | Copy file a to b |
| `mv a b` | Move/rename file |
| `rm file` | Delete a file |
| `echo "text"` | Print text |
| `grep word file` | Search in file |
| `man command` | Read the manual |
| `chmod +x file` | Make file runnable |
| `\|` | Pipe: send output to next command |
| `git init` | Start tracking a directory with git |
| `git add .` | Stage all changed files |
| `git commit -m ""` | Save a snapshot with a message |
| `git log --oneline` | See commit history |
| `git diff` | See uncommitted changes |
| `git restore file` | Undo changes to a file |

---

## What's Next?

Once you're comfortable with the terminal, move on to **Module 2: Python**!
Python scripts run right in this same terminal — you already know how.

---

## Practical Exercise: Build a Dragon's Inventory System 🐉

This exercise uses everything from both weeks. Complete all steps in order.

### The Story

You are the keeper of a dragon's hoard. Dragons collect gold, potions, and weapons.
Your job is to track everything the dragon owns using only the terminal.
Build scripts that let you add items, search the hoard, and list everything.

### Goal

Create a command-line inventory manager that stores items in files, organized by category.

---

### Step 1 — Set Up the Dragon's Hoard

```bash
mkdir ~/hoard
mkdir ~/hoard/gold
mkdir ~/hoard/potions
mkdir ~/hoard/weapons
```

Verify it worked:

```bash
ls ~/hoard
```

You should see three directories: `gold`, `potions`, `weapons`.

---

### Step 2 — Add Starting Items to the Hoard

```bash
# Some gold pieces
echo "500 gold coins — stolen from the merchant king" > ~/hoard/gold/coins.txt

# A powerful potion
echo "Potion of Fire Breath — doubles flame range for 10 minutes" > ~/hoard/potions/fire_breath.txt

# A legendary sword
echo "Sword of Thunder — found in the ancient vault of Zargon" > ~/hoard/weapons/thunder_sword.txt
```

Read one back to check:

```bash
cat ~/hoard/weapons/thunder_sword.txt
```

---

### Step 3 — Write a Script to Add Items

Create `add_item.sh`:

```bash
nano ~/hoard/add_item.sh
```

Type this inside:

```bash
#!/bin/bash

echo "================================"
echo "   DRAGON'S HOARD — ADD ITEM   "
echo "================================"
echo "Which category? (gold / potions / weapons)"
read category

# Check the category exists
if [ ! -d ~/hoard/$category ]; then
    echo "Category '$category' does not exist. Creating a new one..."
    mkdir ~/hoard/$category
fi

echo "Item name (no spaces, e.g. magic_ring.txt):"
read filename

echo "Describe the item:"
read description

echo "$description" >> ~/hoard/$category/$filename
echo ""
echo "✓ Added to the hoard: ~/hoard/$category/$filename"
```

Save, exit, make it runnable:

```bash
chmod +x ~/hoard/add_item.sh
./hoard/add_item.sh
```

---

### Step 4 — Write a Script to Search the Hoard

Create `search_hoard.sh`:

```bash
nano ~/hoard/search_hoard.sh
```

Type this inside:

```bash
#!/bin/bash

echo "================================"
echo "   DRAGON'S HOARD — SEARCH     "
echo "================================"
echo "What are you searching for?"
read search_term

echo ""
echo "Searching for '$search_term' in the hoard..."
echo "----------------------------"
grep -r "$search_term" ~/hoard/ 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Nothing found! The hoard does not contain '$search_term'."
fi
```

```bash
chmod +x ~/hoard/search_hoard.sh
./hoard/search_hoard.sh
```

Try searching for `Thunder` — it should find your thunder sword.

---

### Step 5 — Write a Script to List All Items

Create `list_hoard.sh`:

```bash
nano ~/hoard/list_hoard.sh
```

```bash
#!/bin/bash

echo "================================"
echo "    🐉 THE DRAGON'S HOARD 🐉    "
echo "================================"
echo ""

for category_dir in ~/hoard/*/; do
    category=$(basename "$category_dir")

    # Skip if it's not a real directory
    if [ ! -d "$category_dir" ]; then
        continue
    fi

    echo "[ $category ]"

    count=0
    for item in "$category_dir"*.txt; do
        if [ -f "$item" ]; then
            echo "  - $(basename $item)"
            count=$((count + 1))
        fi
    done

    if [ $count -eq 0 ]; then
        echo "  (this category is empty)"
    fi

    echo ""
done
echo "================================"
```

```bash
chmod +x ~/hoard/list_hoard.sh
./hoard/list_hoard.sh
```

---

### Step 6 — Combine Everything Into the Hoard Menu

Create `hoard.sh`:

```bash
nano ~/hoard/hoard.sh
```

```bash
#!/bin/bash

while true; do
    echo ""
    echo "================================"
    echo "    🐉 DRAGON HOARD MANAGER 🐉  "
    echo "================================"
    echo "1) Add an item"
    echo "2) List all items"
    echo "3) Search the hoard"
    echo "4) Inspect an item"
    echo "5) Quit"
    echo ""
    read -p "Choose (1-5): " choice

    case $choice in
        1)
            bash ~/hoard/add_item.sh
            ;;
        2)
            bash ~/hoard/list_hoard.sh
            ;;
        3)
            bash ~/hoard/search_hoard.sh
            ;;
        4)
            echo "Category (gold/potions/weapons):"
            read category
            echo "Item filename:"
            read fname
            path=~/hoard/$category/$fname
            if [ -f "$path" ]; then
                echo ""
                echo "--- $fname ---"
                cat "$path"
                echo ""
            else
                echo "Item not found: $path"
            fi
            ;;
        5)
            echo "The dragon guards the hoard. Farewell!"
            break
            ;;
        *)
            echo "Please enter a number from 1 to 5."
            ;;
    esac
done
```

```bash
chmod +x ~/hoard/hoard.sh
./hoard/hoard.sh
```

---

### Checklist — Did You Complete Everything?

- [ ] Created `~/hoard` with three sub-directories
- [ ] Used `echo >` to write item descriptions into files
- [ ] Used `cat` to read an item back
- [ ] Wrote `add_item.sh` and added an item with it
- [ ] Wrote `search_hoard.sh` and found an item by keyword
- [ ] Wrote `list_hoard.sh` and saw your hoard tree
- [ ] Wrote `hoard.sh` as a complete menu program
- [ ] Used `chmod +x` on every script before running it

### Bonus Challenges 🏆

1. Add a **"Remove an item"** option to `hoard.sh` using `rm`
2. Add a **date stamp** to every item using `$(date)` inside `add_item.sh` so you know when it was found
3. Add a **"Backup the hoard"** option that copies `~/hoard` to `~/hoard_backup` using `cp -r`
4. Count how many items the dragon owns in total and show it at the top of the menu

---

## 🏆 Module 1 Badge: Terminal Ninja

Earn this badge by completing:
- [ ] All 8 checklist items above
- [ ] At least 2 bonus challenges
- [ ] Write a brand new shell script that does something the hoard system doesn't already do (be creative!)
