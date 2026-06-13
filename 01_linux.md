# Module 1: Linux — Talking to Your Computer Like a Pro

## What Is Linux?

Linux is a **free operating system** — the software that runs your computer.
You probably use Windows or macOS. Linux is the third big one, and it powers:

- Most websites on the internet
- Android phones
- Raspberry Pi
- Supercomputers and space robots

The coolest part of Linux is the **terminal** — a text window where you type
commands and the computer obeys. No mouse needed. It feels like being a hacker.

---

## Week 1: Finding Your Way Around

### Lesson 1.1 — Opening the Terminal

On most Linux systems, press `Ctrl + Alt + T` to open a terminal.
You'll see something like:

```
aaa@mycomputer:~$
```

- `aaa` — your username
- `mycomputer` — your computer's name
- `~` — you are in your home directory (your room!)
- `$` — the computer is waiting for your command

---

### Lesson 1.2 — Your First Commands

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

**Challenge:** Make the computer say your name using `echo`.

---

### Lesson 1.3 — Files and Directories

Everything in Linux lives in **directories**.
Think of it like a filing cabinet.

```bash
# List files and directories in the current directory
ls

# List with more details (size, date, permissions)
ls -l

# List including hidden files (files starting with a dot)
ls -a
```

**What you'll see in `ls -l`:**

```
drwxr-xr-x  2  aaa  aaa  4096  Jun 10  documents
-rw-r--r--  1  aaa  aaa   128  Jun 10  notes.txt
```

- `d` at the start = it's a directory
- `-` at the start = it's a file
- The letters after = who is allowed to read/write/run it

---

### Lesson 1.4 — Moving Around

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

**Challenge:** Start at home (`~`), go into `/tmp`, list the files, then go back home.

---

### Lesson 1.5 — Making and Removing Things

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

# Remove an empty directory
rmdir my_cool_directory

# Remove a directory and everything inside it (very careful!)
rm -rf my_cool_directory
```

> **Safety Rule:** `rm -rf` deletes forever. Always double-check before using it.

---

### Lesson 1.6 — Copying and Moving Files

```bash
# Copy a file
cp original.txt backup.txt

# Move (or rename) a file
mv old_name.txt new_name.txt

# Copy a whole directory
cp -r my_directory my_directory_backup
```

---

## Week 2: Becoming a Power User

### Lesson 2.1 — Finding Things

```bash
# Search for a file by name
find . -name "hello.txt"

# Search for text inside files
grep "python" my_notes.txt

# Search recursively in all files in a directory
grep -r "hello" ~/documents/
```

---

### Lesson 2.2 — The Manual (Your Superpower)

Every command has a manual. Type `man` before any command:

```bash
man ls
man echo
man grep
```

Press `q` to quit the manual. Press spacebar to scroll down.

---

### Lesson 2.3 — Piping (Chaining Commands Together)

The `|` symbol (called a **pipe**) sends the output of one command into another.

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

---

### Lesson 2.4 — Permissions

Every file has rules about who can read, write, or run it.

```bash
# See permissions
ls -l

# Make a file executable (runnable)
chmod +x my_script.sh

# Make a file read-only (no changes allowed)
chmod 444 important.txt
```

Permission letters:
- `r` = read
- `w` = write
- `x` = execute (run)

---

### Lesson 2.5 — Writing Your First Shell Script

A shell script is a text file full of commands. The computer runs them all in order.

**Step 1:** Create the file

```bash
nano my_first_script.sh
```

**Step 2:** Type this inside nano:

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

---

### Lesson 2.6 — Variables and User Input in Shell

```bash
#!/bin/bash

# Ask the user for their name
echo "What is your name?"
read user_name

# Use the variable with $
echo "Hello, $user_name! Welcome to Linux!"

# Variables can store numbers too
my_number=42
echo "My favorite number is $my_number"
```

---

### Lesson 2.7 — If/Else in Shell Scripts

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

- `-ge` means "greater than or equal to"
- `-eq` means "equal to"
- `-lt` means "less than"

---

### Lesson 2.8 — Loops in Shell Scripts

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

---

## Mini Project: System Info Script

Build a script that shows:
1. Your username
2. The date and time
3. How much disk space is left
4. The 5 newest files in your home directory

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

## Practical Exercise: Build Your Own Digital Notebook

This exercise uses everything from both weeks. Complete all steps in order.

### Goal

Create a command-line notebook that stores text notes in files, organized into directories by topic.

---

### Step 1 — Set Up the Directory Structure

```bash
mkdir ~/notebook
mkdir ~/notebook/school
mkdir ~/notebook/ideas
mkdir ~/notebook/lists
```

Verify it worked:

```bash
ls ~/notebook
```

You should see three directories: `school`, `ideas`, `lists`.

---

### Step 2 — Create Your First Notes

```bash
# A school note
echo "Photosynthesis: plants turn sunlight into food using chlorophyll." > ~/notebook/school/science.txt

# An ideas note
echo "Idea: build a robot that waters plants automatically." > ~/notebook/ideas/robot.txt

# A shopping list
echo "Apples
Bread
Peanut butter
Milk" > ~/notebook/lists/shopping.txt
```

Read one back to check:

```bash
cat ~/notebook/school/science.txt
```

---

### Step 3 — Write a Script to Add Notes

Create `add_note.sh`:

```bash
nano ~/notebook/add_note.sh
```

Type this inside:

```bash
#!/bin/bash

echo "=== ADD A NOTE ==="
echo "Which topic? (school / ideas / lists)"
read topic

# Check the directory exists
if [ ! -d ~/notebook/$topic ]; then
    echo "Topic '$topic' does not exist. Creating it..."
    mkdir ~/notebook/$topic
fi

echo "Note filename (no spaces, e.g. math.txt):"
read filename

echo "Type your note (press Enter when done):"
read note_text

echo "$note_text" >> ~/notebook/$topic/$filename
echo "Note saved to ~/notebook/$topic/$filename"
```

Save, exit, make it runnable:

```bash
chmod +x ~/notebook/add_note.sh
./notebook/add_note.sh
```

---

### Step 4 — Write a Script to Search All Notes

Create `search_notes.sh`:

```bash
nano ~/notebook/search_notes.sh
```

Type this inside:

```bash
#!/bin/bash

echo "=== SEARCH NOTES ==="
echo "What word are you looking for?"
read search_term

echo ""
echo "Results for '$search_term':"
echo "----------------------------"
grep -r "$search_term" ~/notebook/ 2>/dev/null

if [ $? -ne 0 ]; then
    echo "No results found."
fi
```

```bash
chmod +x ~/notebook/search_notes.sh
./notebook/search_notes.sh
```

Try searching for `robot` — it should find your ideas note.

---

### Step 5 — Write a Script to List All Notes

Create `list_notes.sh`:

```bash
nano ~/notebook/list_notes.sh
```

```bash
#!/bin/bash

echo "=== YOUR NOTEBOOK ==="
echo ""

for topic_dir in ~/notebook/*/; do
    topic=$(basename "$topic_dir")

    # Skip if it's not a real directory
    if [ ! -d "$topic_dir" ]; then
        continue
    fi

    echo "[ $topic ]"

    count=0
    for note in "$topic_dir"*.txt; do
        if [ -f "$note" ]; then
            echo "  - $(basename $note)"
            count=$((count + 1))
        fi
    done

    if [ $count -eq 0 ]; then
        echo "  (no notes yet)"
    fi

    echo ""
done
```

```bash
chmod +x ~/notebook/list_notes.sh
./notebook/list_notes.sh
```

---

### Step 6 — Combine Everything Into One Menu Script

Create `notebook.sh`:

```bash
nano ~/notebook/notebook.sh
```

```bash
#!/bin/bash

while true; do
    echo ""
    echo "=============================="
    echo "      MY DIGITAL NOTEBOOK     "
    echo "=============================="
    echo "1) Add a note"
    echo "2) List all notes"
    echo "3) Search notes"
    echo "4) Read a note"
    echo "5) Quit"
    echo ""
    read -p "Choose (1-5): " choice

    case $choice in
        1)
            bash ~/notebook/add_note.sh
            ;;
        2)
            bash ~/notebook/list_notes.sh
            ;;
        3)
            bash ~/notebook/search_notes.sh
            ;;
        4)
            echo "Topic name:"
            read topic
            echo "Note filename:"
            read fname
            path=~/notebook/$topic/$fname
            if [ -f "$path" ]; then
                echo ""
                echo "--- $fname ---"
                cat "$path"
            else
                echo "Note not found: $path"
            fi
            ;;
        5)
            echo "Goodbye!"
            break
            ;;
        *)
            echo "Please enter a number from 1 to 5."
            ;;
    esac
done
```

```bash
chmod +x ~/notebook/notebook.sh
./notebook/notebook.sh
```

---

### Checklist — Did You Complete Everything?

- [ ] Created a `notebook` directory with three sub-directories
- [ ] Used `echo >` to write notes into files
- [ ] Used `cat` to read a note back
- [ ] Wrote `add_note.sh` and added a note with it
- [ ] Wrote `search_notes.sh` and found a word in your notes
- [ ] Wrote `list_notes.sh` and saw your note tree
- [ ] Wrote `notebook.sh` as a complete menu program
- [ ] Used `chmod +x` on every script before running it

### Bonus Challenges

1. Add a **"Delete a note"** option to `notebook.sh` that removes a file using `rm`
2. Add a **date stamp** to every note automatically using `$(date)` inside `add_note.sh`
3. Add a **backup option** that copies the entire `~/notebook` directory to `~/notebook_backup` using `cp -r`
4. Count how many notes exist in total and display it at the top of the menu
