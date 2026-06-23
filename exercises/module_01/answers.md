# Module 1 Answers — Linux & Git

---

## Section A: Command Recall

1. `whoami`
2. `pwd`
3. `ls`
4. `ls -a`
5. `mkdir lab`
6. `cd lab`
7. `cd ..`
8. `touch test.txt`
9. `echo "hello" > test.txt`
10. `cat test.txt`
11. `cp test.txt backup.txt`
12. `mv backup.txt copy.txt`
13. `rm copy.txt`
14. `grep "hello" test.txt`
15. `man ls`

---

## Section B: What Does This Do?

1. `ls -l | grep ".sh"`
   → Lists all files in detail, then filters to show only files ending in `.sh` (shell scripts).

2. `cat notes.txt | wc -l`
   → Prints the contents of `notes.txt` and counts how many lines it has.

3. `find . -name "*.py"`
   → Searches the current directory (and all sub-directories) for any file ending in `.py`.

4. `grep -r "dragon" ~/hoard/`
   → Searches every file inside `~/hoard/` for the word "dragon" and shows which files contain it.

5. `chmod +x myscript.sh`
   → Makes `myscript.sh` executable — you can now run it with `./myscript.sh`.

6. `rm -rf old_folder`
   → Deletes `old_folder` AND everything inside it, permanently. No undo! Use with care.

---

## Section C: Fix the Bug

**Script 1 — Bug:** `$Name` should be `$name` (bash variables are case-sensitive!)
```bash
#!/bin/bash
echo "What is your name?"
read name
echo "Hello $name!"
```

**Script 2 — Bug:** Missing `do` after the `for` line.
```bash
#!/bin/bash
for i in 1 2 3 4 5; do
    echo "Number: $i"
done
```

**Script 3 — Bug:** Missing `; then` after the `if` condition.
```bash
#!/bin/bash
echo "How old are you?"
read age
if [ $age -ge 10 ]; then
    echo "You are 10 or older!"
fi
```

---

## Section D: Write the Script

**Exercise 1 — greet.sh**
```bash
#!/bin/bash

echo "What is your name?"
read name

echo "What is your favourite colour?"
read colour

echo "Hello $name! $colour is a great colour."
```

**Exercise 2 — countdown.sh**
```bash
#!/bin/bash

for i in 10 9 8 7 6 5 4 3 2 1; do
    echo "$i..."
done

echo "BLAST OFF! 🚀"
```

**Exercise 3 — evens.sh**
```bash
#!/bin/bash

for i in 2 4 6 8 10 12 14 16 18 20; do
    echo $i
done
```

Alternative using a step in seq:
```bash
#!/bin/bash
for i in $(seq 2 2 20); do
    echo $i
done
```

**Exercise 4 — check.sh**
```bash
#!/bin/bash

echo "Enter a filename to check:"
read filename

if [ -f "$filename" ]; then
    echo "File found!"
else
    echo "File not found!"
fi
```

---

## Section E: Git Practice

Expected outputs:

2. `git init` prints something like:
   `Initialized empty Git repository in /home/you/git_practice/.git/`

4. `hero.txt` shows in **red** — it means the file is untracked (git sees it but isn't saving it yet).

5. After `git add`, `hero.txt` turns **green** — it's now staged, ready to be committed.

6. `git commit` prints something like:
   ```
   [main (root-commit) a1b2c3d] add hero description
    1 file changed, 1 insertion(+)
    create mode 100644 hero.txt
   ```

8. `git diff` shows the new line you added, with a `+` sign at the start — that's what changed.

10. `git log --oneline` shows 2 lines — one for each commit.

---

## Section F: Pipe Challenge

1. `ls /etc | wc -l`
   → Counts all entries in `/etc`. The number varies by system but is usually 150–200.

2. `cat /etc/os-release | head -3`
   → Shows the first 3 lines of the OS release file (name, version, etc).

3. `ps aux | grep python`
   → Shows any running Python processes. If nothing is running, you'll still see the grep command itself.

---

## Bonus: Dragon Hoard Challenge

**1. count_items.sh**
```bash
#!/bin/bash

count=$(find ~/hoard -name "*.txt" | wc -l)
echo "The dragon owns $count items."
```

**2. biggest_category.sh**
```bash
#!/bin/bash

echo "Counting items per category..."
echo ""

for dir in ~/hoard/*/; do
    category=$(basename "$dir")
    count=$(find "$dir" -name "*.txt" | wc -l)
    echo "$category: $count items"
done
```
(Finding the actual maximum requires more advanced scripting — give yourself a bonus point if you figure it out!)

**3. Modified add_item.sh with date stamp**
```bash
#!/bin/bash

echo "================================"
echo "   DRAGON'S HOARD — ADD ITEM   "
echo "================================"
echo "Which category? (gold / potions / weapons)"
read category

if [ ! -d ~/hoard/$category ]; then
    echo "Category '$category' does not exist. Creating a new one..."
    mkdir ~/hoard/$category
fi

echo "Item name (no spaces, e.g. magic_ring.txt):"
read filename

echo "Describe the item:"
read description

# Add description AND a date stamp
echo "$description" >> ~/hoard/$category/$filename
echo "Found on: $(date)" >> ~/hoard/$category/$filename

echo ""
echo "✓ Added to the hoard: ~/hoard/$category/$filename"
```
