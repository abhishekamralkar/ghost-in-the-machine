# Module 5 Answers — Git & GitHub

> **Reminder:** Try each exercise yourself before reading the answer. Git is a tool you learn by doing — reading answers without trying first won't build the muscle memory you need.

---

## Section A: Local Git Warm-Up

### Exercise 1 — Answer

```bash
mkdir ~/git-practice
cd ~/git-practice
echo "Hello, Git!" > hello.txt
git init
git status          # hello.txt shows in RED = untracked
git add hello.txt
git status          # hello.txt shows in GREEN = staged
git commit -m "first commit: add hello.txt"
git log --oneline
```

**Expected output of `git log --oneline`:**
```
a1b2c3d (HEAD -> main) first commit: add hello.txt
```

The red/green colour in `git status` tells you whether a file is staged (green = ready to commit) or not yet staged (red = git sees it but isn't saving it).

---

### Exercise 2 — Answer

```bash
echo "A second line of text" >> hello.txt
git diff
```

`git diff` shows:
```diff
-Hello, Git!
+Hello, Git!
+A second line of text
```

Lines with `+` are new. Lines with `-` were removed (none here).

```bash
git add hello.txt
git commit -m "add second line to hello.txt"

echo "My notes go here" > notes.txt
git add notes.txt
git commit -m "add notes.txt"

git log --oneline
```

**Expected:**
```
9f4e2b1 (HEAD -> main) add notes.txt
7c3a1d0 add second line to hello.txt
a1b2c3d first commit: add hello.txt
```

- `git show HEAD` — shows the MOST RECENT commit (the `notes.txt` one)
- `git show HEAD~1` — shows ONE commit BEFORE the most recent (the "second line" commit)
- `HEAD~1` means "go back 1 step from the current position"

---

### Exercise 3 — Answer

```bash
# Delete the content (pretend this was an accident)
echo "" > hello.txt    # overwrites file with nothing

git status
# Shows: modified: hello.txt (in red)

git diff
# Shows all your text deleted (in red with -)

git restore hello.txt

# Open the file — everything is back
cat hello.txt
```

`git restore` works because Git still has the last committed version of the file. It just overwrites your broken local copy with the safe saved version.

> **Important:** `git restore` only works if you haven't committed the mistake. If you already committed the bad version, use `git revert` instead.

---

### Exercise 4 — Answer

```bash
git switch -c experiment
echo "This is my experiment" > experiment.txt
git add experiment.txt
git commit -m "add experiment file"

git switch main
ls
# Output: hello.txt  notes.txt   (experiment.txt is GONE from main)

git switch experiment
ls
# Output: experiment.txt  hello.txt  notes.txt   (it's back!)
```

`experiment.txt` appears and disappears because each branch keeps its own set of files. Switching branches literally changes the files in your folder. Git is the one swapping them in and out.

---

### Exercise 5 — Answer

```bash
git switch main
git merge experiment
# Output: Fast-forward ... experiment.txt | 1 + ...

ls
# Output: experiment.txt  hello.txt  notes.txt  (all three on main now!)

git branch -d experiment
# Output: Deleted branch experiment (was 9f4e2b1).

git log --oneline --graph --all
```

**Expected graph:**
```
* 9f4e2b1 (HEAD -> main) add experiment file
* 7c3a1d0 add notes.txt
* a1b2c3d first commit: add hello.txt
```

Note: When Git can do a "fast-forward" merge (your branch was directly ahead of main with no conflicts), it doesn't create a merge commit — it just moves the main pointer forward. That's why the graph looks like a straight line, not a fork.

---

## Section B: Setting Up GitHub

### Exercise 6 — No code answer

Just follow the steps. Checklist:
- [ ] Account created
- [ ] Email verified
- [ ] Profile picture added
- [ ] Username noted down

---

### Exercise 7 — Answer

```bash
# Generate the key
ssh-keygen -t ed25519 -C "your@email.com"
# Press Enter three times

# See the public key to copy
cat ~/.ssh/id_ed25519.pub
# Copy everything from "ssh-ed25519" to your email address

# Test connection after adding key to GitHub
ssh -T git@github.com
```

**Expected output:**
```
Hi your-username! You've successfully authenticated, but GitHub
does not provide shell access.
```

Your SSH directory now has two files:
```bash
ls ~/.ssh/
# id_ed25519      ← PRIVATE key — never share this
# id_ed25519.pub  ← PUBLIC key — safe to share, goes on GitHub
```

The private key stays on your computer. The public key goes on GitHub. Together they prove "yes, this computer belongs to this GitHub user" — like a lock and key.

---

## Section C: Pushing to GitHub

### Exercise 8 — Answer

```bash
cd ~/git-practice

# Connect to GitHub (replace YOUR-USERNAME with your actual username)
git remote add origin git@github.com:YOUR-USERNAME/git-practice.git

# First push (sets up the upstream tracking)
git push -u origin main
```

**Expected output:**
```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.23 KiB | 1.23 MiB/s, done.
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

From now on, in this repo, `git push` (no extra flags) is enough.

Verify the connection:
```bash
git remote -v
# origin  git@github.com:YOUR-USERNAME/git-practice.git (fetch)
# origin  git@github.com:YOUR-USERNAME/git-practice.git (push)
```

---

### Exercise 9 — Answer

**Part 1 — Edit on GitHub:** Done via the browser (no terminal commands needed).

**Part 2 — Pull to your computer:**
```bash
git pull
# Output: Updating a1b2c3d..9f4e2b1
#         Fast-forward
#          hello.txt | 1 +
#          1 file changed, 1 insertion(+)

cat hello.txt
# Shows the new line you added on GitHub
```

**Part 3 — Edit locally and push:**
```bash
echo "Edited on my computer" >> hello.txt
git add hello.txt
git commit -m "add line from local computer"
git push
```

**After both changes, `git log --oneline` shows:**
```
3a7f9c2 (HEAD -> main, origin/main) add line from local computer
b2d4e81 Edit directly on GitHub
9f4e2b1 add notes.txt
...
```

This is the normal daily workflow for any developer working on a real project.

---

## Section D: Collaboration Features

### Exercise 10 — Answer

```bash
git clone git@github.com:YOUR-USERNAME/Hello-World.git
cd Hello-World
git log --oneline
ls
```

`ls` shows: `README`

`git log --oneline` shows the full commit history from the original repo, going back years. This history was copied to your fork exactly.

---

### Exercise 11 — Answer

```bash
git switch -c my-first-pr
echo "" >> README
echo "Improved by YOUR-NAME" >> README
git add README
git commit -m "add my name to README"
git push origin my-first-pr
```

Go to GitHub → your fork → you'll see: **"my-first-pr had recent pushes — Compare & pull request"**

Click it. Fill in the description. Click **Create pull request**.

To merge it into your own fork (not into `octocat`'s original):
1. Click **Pull requests** tab in YOUR fork
2. Click your PR
3. Click **Merge pull request** → **Confirm merge**

Your `main` branch now contains your change.

---

### Exercise 12 — Answer

Example README.md:

```markdown
# Summer 2026 Projects

Five coding projects I built during summer 2026 — from Linux basics to AI hardware.

## What I Built

- **Linux Terminal** — Learned to navigate the filesystem, write shell scripts, and use Git
- **Python Games** — Built a text-based RPG with battles, inventory, and random loot
- **AI Chatbot** — Ran a local AI using Ollama and gave it custom personalities
- **Raspberry Pi Tombstone Display** — Wired up an OLED screen and button, powered by AI
- **People in Space Indicator** — Fetched live astronaut data from a real API

## What I Learned

1. How computers actually work: CPU, RAM, storage, and the OS
2. Python is one of the world's most useful programming languages — and it's readable
3. AI models are just programs you can control with code, not magic

## Example Code

```python
response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Write me a spooky epitaph"}]
)
print(response["message"]["content"])
```

## Interesting Reading

- [Raspberry Pi Projects](https://projects.raspberrypi.org) — where the hardware ideas came from
```

---

## Section E: GitHub Pages

### Exercise 13 — Answer

After creating `index.html` and pushing:

```bash
git add index.html
git commit -m "add portfolio website"
git push
```

GitHub Pages settings:
- Settings → Pages → Source: **Deploy from a branch** → Branch: **main** → Folder: **/ (root)** → Save

Your URL will be: `https://YOUR-USERNAME.github.io/summer-2026`

If you want to make the page look nicer, add CSS inside the `<style>` tag in the `<head>`. For example:

```html
<head>
  <title>My Summer 2026 Projects</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 700px;
      margin: 60px auto;
      padding: 0 20px;
      background: #f9f9f9;
      color: #333;
    }
    h1 { color: #2d8a4e; }
    li  { margin: 6px 0; }
  </style>
</head>
```

---

## Section F: Understanding Git

**Q1 — `git add` vs `git commit`**

`git add` is the STAGING step — you're picking which changes you want to include in the next snapshot. `git commit` is the SAVING step — it creates the permanent snapshot.

Two steps exist so you can be selective. If you changed 10 files but only 3 are ready, you `git add` just those 3 and commit. The other 7 wait for the next commit. This lets you make small, focused commits instead of one giant "changed everything" commit.

---

**Q2 — HEAD and HEAD~1**

`HEAD` is a pointer to the commit you are currently on — usually the most recent commit on your branch. Think of it as "where you are right now in history."

`HEAD~1` means "one commit before HEAD". `HEAD~2` means two commits back. It's a way of saying "go back N steps" without having to type the actual commit ID.

---

**Q3 — What is a branch?**

A branch is a separate copy of your code history that you can make changes on without affecting the main copy.

You'd use one when you want to try something risky, add a big new feature, or experiment — without breaking the code that already works. If the experiment works, you merge the branch back. If it breaks, you delete the branch and nothing is lost on `main`.

---

**Q4 — `git pull` vs `git clone`**

`git clone` is for starting fresh — it downloads a repository from GitHub to your computer for the first time. You only do it once per project.

`git pull` is for keeping in sync — it downloads any NEW commits that were added to GitHub since you last pulled. You run it every time you sit down to work.

---

**Q5 — Simultaneous changes / push rejected**

Git will reject your push with a message like: `error: failed to push some refs`. This is Git saying "GitHub has commits you don't have yet — get those first."

Fix it with:
```bash
git pull        # download GitHub's changes and merge them with yours
git push        # now push your combined changes up
```

If the same line was changed in both versions, you'll get a merge conflict. Open the file, resolve it (choose which version to keep), `git add` and `git commit`, then `git push`.

---

**Q6 — Why commit messages matter**

Commit messages are notes to your future self (and your teammates). Three months from now when something breaks, you'll search through the history trying to find when the bug was introduced. A message like `"stuff"` tells you nothing. A message like `"fix score counter resetting on player death"` lets you find the bug in seconds.

**Bad commit messages:**
- `"stuff"`
- `"fix"`
- `"wip"`
- `"asdfg"`

**Good commit messages:**
- `"add inventory system to RPG game"`
- `"fix button debounce causing double-presses"`
- `"add README with project description and setup steps"`

The rule: write the message as if you're explaining to your future self what you changed and why.

---

## Bonus Challenges

### Bonus 1 — Git Archaeology: Sample Answers

Going to `github.com/microsoft/vscode` (at the time of writing):
- Over 100,000 commits
- Multiple contributors active daily
- Hundreds of open pull requests at any time
- Commits from 2015 show a much simpler editor with far fewer features

Finding old commits: click the commit count → scroll through history → click any commit to see the diff.

---

### Bonus 2 — Resolve a Merge Conflict: Answer

```bash
cd ~/git-practice

# --- Set up the conflict ---

# On main: change first line
git switch main
# Edit hello.txt, change line 1 to: "Hello from main!"
git add hello.txt
git commit -m "change greeting on main"

# On conflict-test: change the SAME first line differently
git switch -c conflict-test
# Edit hello.txt, change line 1 to: "Hello from my branch!"
git add hello.txt
git commit -m "change greeting on conflict-test"

# --- Trigger the conflict ---
git switch main
git merge conflict-test
# OUTPUT: CONFLICT (content): Merge conflict in hello.txt
#         Automatic merge failed; fix conflicts and then commit the result.
```

**Open `hello.txt` — you'll see:**
```
<<<<<<< HEAD
Hello from main!
=======
Hello from my branch!
>>>>>>> conflict-test
```

**Edit it to keep what you want (e.g. keep both lines):**
```
Hello from main!
Hello from my branch!
```

**Finish the merge:**
```bash
git add hello.txt
git commit -m "merge conflict-test: keep both greetings"
git log --oneline --graph --all
```

**Expected graph:**
```
*   (HEAD -> main) merge conflict-test: keep both greetings
|\
| * (conflict-test) change greeting on conflict-test
* | change greeting on main
|/
* add notes.txt
```

Merge conflicts look scary but they're just Git asking "I can't decide — you choose." Once you've resolved a few, they feel routine.

---

### Bonus 3 — Contribute to Open Source

There's no single "answer" here — every project is different. Tips for finding good first issues:

1. Search GitHub: `label:"good first issue" language:python`
2. Check the project's `CONTRIBUTING.md` — it tells you exactly how they want PRs formatted
3. Start with documentation fixes — fixing a typo or improving a README explanation is a completely valid first contribution
4. Be patient — maintainers are volunteers and might take weeks to review

A good PR description:
```
## What this PR does
Fixed a typo in the README where "recieve" should be "receive".

## Why
Noticed this while reading the docs. Small fix but it improves the project.
```

You just completed the full open source contribution workflow. That's exactly how improvements to Python, Linux, and VS Code happen — thousands of people making small improvements just like this one.
