# Module 5: Git & GitHub — Saving Your Work and Sharing It With the World

```
LEVEL 5 UNLOCKED: Open Source Hero
=====================================
You've been saving files on your computer.
But what if your hard drive breaks? What if a friend wants your code?
What if you want to show the world what you built this summer?
Git and GitHub solve all of that.
```

## What You Already Know

In Module 1 you learned the basics of **Git** — a tool that saves snapshots of your code:

```
git init        → start tracking a project
git add .       → stage your changes
git commit -m   → save a snapshot
git log         → see your history
git diff        → see what changed
git restore     → undo changes
```

This module goes further. You'll learn **branches**, **GitHub** (the website where millions of developers share code), and how to **collaborate** — working on the same project as other people without breaking each other's work.

---

## What Is GitHub?

**GitHub** is a website that stores your Git repositories in the cloud.

Think of it this way:
- **Git** is like saving your game to a memory card
- **GitHub** is like uploading your save file to the cloud so you can access it from any device, share it with friends, or go back to any save point

GitHub is where almost all of the world's open source code lives. Linux, Python, VS Code, and millions of other programs are all on GitHub. When you put your code there, you join that community.

```
Your computer                        GitHub (the internet)
┌────────────────┐                  ┌──────────────────────┐
│  your project  │  ──git push──►   │  your project        │
│  (local repo)  │  ◄──git pull──   │  (remote repo)       │
└────────────────┘                  └──────────────────────┘
```

> **Fun Fact:** GitHub hosts over 420 million repositories. The Python programming
> language itself is developed on GitHub — anyone in the world can suggest improvements!

---

## Week 11: Git Branches and History

### Lesson 11.1 — What Is a Branch?

Right now all your commits go in a straight line — one after another. That's fine when you're working alone. But what if you want to try something risky without breaking your working code? That's what **branches** are for.

A **branch** is a separate copy of your code that you can experiment on. Your main code stays safe on the `main` branch. You create a new branch, try your idea, and if it works you merge it back. If it breaks, you just delete the branch and nothing is lost.

Think of it like a video game where you can save at a checkpoint, go explore a dangerous path, and if you die you reload the checkpoint. The dangerous path is a branch. The checkpoint is `main`.

```
main:       A ── B ── C ──────────────── F (merge)
                       \                /
new-feature:            D ── E ────────
```

**Create a branch:**

```bash
# See which branch you are on (the * shows current branch)
git branch

# Create a new branch called "new-feature"
git branch new-feature

# Switch to it
git switch new-feature

# Shortcut: create AND switch in one command
git switch -c new-feature
```

**What you should see:**
```
Switched to a new branch 'new-feature'
```

Your prompt in some terminals will show the branch name. In VS Code, the branch name appears in the bottom-left corner of the window.

**Make changes and commit on your branch:**

```bash
# Edit some files, then:
git add .
git commit -m "try new feature on its own branch"

# See all branches and which one you're on
git branch
```

**Switch back to main:**

```bash
git switch main
```

Notice that the changes you made on `new-feature` are gone from your files — they're still on that branch, but `main` hasn't seen them yet.

> **Try this!** Create a branch called `experiment`, add a new file, commit it, then switch back to `main`. Run `ls` — your new file is gone! Switch back to `experiment` and run `ls` again — it's back. Branches are like parallel universes.

---

### Lesson 11.2 — Merging Branches

Once your new feature works, you **merge** it back into `main` to combine the two histories.

You must be on the branch you want to merge INTO (usually `main`):

```bash
# Switch to main first
git switch main

# Merge the new-feature branch into main
git merge new-feature
```

**What you should see:**
```
Updating c3f1a2b..9e4d7f1
Fast-forward
 new_feature.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)
```

**Delete the branch after merging** (it's done its job):

```bash
git branch -d new-feature
```

**What if two branches changed the same line?** That's called a **merge conflict**. Git can't decide which version to keep, so it asks you:

```
<<<<<<< HEAD (main)
print("Hello from main!")
=======
print("Hello from my feature!")
>>>>>>> new-feature
```

You open the file, pick which version you want (or combine them), delete the `<<<<`, `====`, `>>>>` lines, save, then `git add` and `git commit`. Conflicts are normal — every developer deals with them.

> **Try this!** Create two branches from `main`. On each branch, edit the SAME line of the same file differently. Merge the first branch into main, then try to merge the second — you'll see a conflict. Resolve it yourself. This is exactly what professional developers do every day.

---

### Lesson 11.3 — Reading History Like a Pro

Git's history is a superpower. You can see exactly what changed, when, and why.

```bash
# Full history
git log

# One line per commit (great overview)
git log --oneline

# Show a visual branch graph
git log --oneline --graph --all

# Show what changed in a specific commit
git show a1b2c3d

# See who changed each line of a file (and when)
git blame my_file.py

# Search through all past commits for a word
git log --all --grep="bug fix"
```

**What you should see** for `git log --oneline --graph --all`:
```
* 9e4d7f1 (HEAD -> main) merge new feature
|\
| * 7c2b1a0 (new-feature) try new feature
|/
* c3f1a2b add hello.py
* a8d4e91 first commit
```

The `*` marks each commit, the lines show where branches split and merged.

---

### Lesson 11.4 — Going Back in Time

Git lets you travel back to any past version of your code.

```bash
# See the file as it was in a specific commit
git show a1b2c3d:my_file.py

# Undo the last commit but keep the changes in your files
git reset --soft HEAD~1

# Completely undo the last commit AND discard the changes
git reset --hard HEAD~1

# Create a new commit that undoes a past commit (safer)
git revert a1b2c3d

# Temporarily travel to a past commit to look around
git checkout a1b2c3d
git switch -         # Go back to where you were
```

> **Rule:** `git reset --hard` throws away work permanently. Always double-check before using it. `git revert` is safer because it creates a new commit instead of erasing history.

> **Try this!** Make three commits in a row with different messages. Then run `git log --oneline` and note the commit IDs. Use `git show <id>` to look at each one. You're time-travelling through your own code history!

---

## Week 12: GitHub — Sharing Your Code With the World

### Lesson 12.1 — Creating a GitHub Account

**Step 1:** Go to [https://github.com](https://github.com) and click **Sign up**.

**Tips for kids:**
- Use a username you'll be proud of — it shows up on all your public projects
- You can use your parent's email address
- Choose a free account

**Step 2:** Verify your email address.

**Step 3:** Set up your profile. Add a photo and a short bio — this is your developer identity!

---

### Lesson 12.2 — Setting Up SSH Keys (Connect Your Computer to GitHub)

GitHub needs to verify it's really you before accepting your code. The most reliable way is an **SSH key** — a pair of digital keys where one lives on your computer and one lives on GitHub. They match like a lock and key.

**Step 1:** Generate an SSH key pair on your computer:

```bash
ssh-keygen -t ed25519 -C "your@email.com"
```

Press **Enter** three times to accept the defaults (no passphrase for now).

**What you should see:**
```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/you/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Your identification has been saved in /home/you/.ssh/id_ed25519
Your public key has been saved in /home/you/.ssh/id_ed25519.pub
```

**Step 2:** Copy your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output — it starts with `ssh-ed25519` and ends with your email.

**Step 3:** Add it to GitHub:
1. Go to **GitHub → Settings → SSH and GPG keys**
2. Click **New SSH key**
3. Give it a name (e.g. "My Linux computer")
4. Paste the key and click **Add SSH key**

**Step 4:** Test the connection:

```bash
ssh -T git@github.com
```

**What you should see:**
```
Hi your-username! You've successfully authenticated, but GitHub
does not provide shell access.
```

That message means it worked! GitHub recognised your key.

> **Try this!** Run `ls ~/.ssh/` — you'll see `id_ed25519` (your private key, never share this) and `id_ed25519.pub` (your public key, safe to share). These two files together prove your identity to GitHub.

---

### Lesson 12.3 — Creating Your First Repository on GitHub

A **repository** on GitHub is like a project folder that lives in the cloud.

**Step 1:** On GitHub, click the **+** button (top right) → **New repository**

**Fill in:**
- **Repository name:** `my-summer-projects` (no spaces — use hyphens)
- **Description:** "My coding projects from Summer 2026"
- **Visibility:** Public (so the world can see your work!) or Private
- **Do NOT** tick "Add a README file" — you'll push your existing local project

**Step 2:** Click **Create repository**. GitHub shows you a page with setup commands.

**Step 3:** Connect your local project to GitHub:

```bash
# Go into your local project
cd ~/projects

# Make sure git is already initialised (if not, run git init first)
git init
git add .
git commit -m "first commit"

# Tell git where GitHub is (copy the SSH URL from GitHub — looks like git@github.com:username/repo.git)
git remote add origin git@github.com:YOUR-USERNAME/my-summer-projects.git

# Push your code up to GitHub
git push -u origin main
```

**What you should see:**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.23 KiB | 1.23 MiB/s, done.
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Now go to your GitHub repository page and **refresh** — your files are there! 🎉

> **Try this!** Click on a file in GitHub. You can see the contents right in the browser. Click the **clock icon** (history) to see all the commits. Click a commit to see exactly what changed — green lines were added, red lines were removed. This is how code review works at real companies.

---

### Lesson 12.4 — Push, Pull, and Clone

These three commands are how you keep your local computer and GitHub in sync.

**`git push`** — send your new commits up to GitHub:

```bash
# After committing locally:
git push
```

**`git pull`** — download any new commits from GitHub (useful if you work on multiple computers, or a teammate added something):

```bash
git pull
```

**`git clone`** — download an entire repository from GitHub to your computer for the first time:

```bash
# Download someone else's project (or your own on a new machine)
git clone git@github.com:username/repo-name.git

# This creates a folder called repo-name with everything inside
cd repo-name
```

**The everyday workflow:**

```
Start of session:    git pull             ← get latest changes
Make changes:        (edit files)
Save snapshot:       git add . && git commit -m "what I did"
Share your work:     git push             ← send to GitHub
```

> **Try this!** On GitHub, click the **pencil icon** on any file to edit it directly in the browser. Make a small change and click **Commit changes**. Now go back to your terminal and run `git pull` — watch your local file update automatically. You just pulled a change from the cloud!

---

### Lesson 12.5 — Forking and Pull Requests

This is how open source collaboration works. Millions of developers improve each other's projects this way.

**Fork** = make your own copy of someone else's repository on GitHub (so you can make changes without affecting the original)

**Pull Request (PR)** = say "hey, I made some improvements on my fork — want to pull them into your project?"

```
Original project (not yours)
        │
        │  Fork (click Fork on GitHub)
        ▼
Your copy on GitHub   ←──── git clone ────  Your computer
        │                                        │
        │                                   (make changes)
        │                                   git add + commit
        │                                   git push
        │
        │  Open Pull Request on GitHub
        ▼
Original project owner reviews your changes and merges (or not)
```

**Try it — fork a real project:**

1. Go to any GitHub repository (try: `github.com/octocat/Hello-World`)
2. Click **Fork** (top right) → **Create fork**
3. Now you have your own copy at `github.com/YOUR-USERNAME/Hello-World`
4. Clone YOUR fork to your computer:
   ```bash
   git clone git@github.com:YOUR-USERNAME/Hello-World.git
   cd Hello-World
   ```
5. Create a branch, make a change, commit and push:
   ```bash
   git switch -c my-improvement
   echo "My improvement" >> README.md
   git add README.md
   git commit -m "add my improvement to README"
   git push origin my-improvement
   ```
6. Go to GitHub — it shows a banner: **"Compare & pull request"** — click it!
7. Write a description and click **Create pull request**

You just opened your first pull request. This is exactly how thousands of developers contribute to Python, Linux, and VS Code every day.

> **Try this!** Look at pull requests on a popular open source project. Go to `github.com/python/cpython/pulls` to see pull requests on the actual Python programming language. These are real people suggesting improvements to the language you just learned!

---

### Lesson 12.6 — Writing a Great README

Every GitHub project needs a **README.md** — the first thing visitors see. It's written in **Markdown** (the same format as these curriculum files!).

A great README has:

```markdown
# Project Name

A short description of what the project does and why it's cool.

## How to Run It

```bash
python3 my_project.py
```

## What It Does

- Feature 1
- Feature 2
- Feature 3

## What I Learned

I built this project to learn about X and Y.
```

**Markdown quick reference:**

| You type | You get |
|----------|---------|
| `# Title` | Big heading |
| `## Section` | Medium heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `` `code` `` | `inline code` |
| `- item` | bullet point |
| `[text](url)` | clickable link |

**Create a README for your summer projects:**

```bash
cd ~/projects
nano README.md
```

Write a description of what you built this summer, then:

```bash
git add README.md
git commit -m "add README"
git push
```

Your README will now display automatically on your GitHub repository page!

> **Try this!** Add a badge to your README. Badges are small icons that show information about your project. GitHub automatically renders them:
> `![Python](https://img.shields.io/badge/python-3.11-blue)`
> Paste this into your README and push — a little blue Python badge will appear!

---

### Lesson 12.7 — GitHub Pages: Publish a Website for Free

GitHub Pages turns any repository into a free website — no hosting fees, no server setup.

**Step 1:** In your repository on GitHub, go to **Settings → Pages**

**Step 2:** Under "Source", choose **Deploy from a branch** → `main` → `/ (root)` → **Save**

**Step 3:** Create a simple `index.html` in your repo:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Summer Projects</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }
    h1   { color: #2d8a4e; }
  </style>
</head>
<body>
  <h1>My Summer 2026 Projects 🚀</h1>
  <p>I spent summer 2026 learning Linux, Python, AI, and Raspberry Pi.</p>
  <h2>What I Built</h2>
  <ul>
    <li>Dragon's Inventory System (Linux shell scripts)</li>
    <li>Text RPG Battle Game (Python)</li>
    <li>AI Chatbot with custom personalities (Ollama)</li>
    <li>Raspberry Pi AI Tombstone Display (hardware + AI)</li>
    <li>People in Space Indicator (live API data)</li>
  </ul>
</body>
</html>
```

Push it:

```bash
git add index.html
git commit -m "add portfolio website"
git push
```

**Step 4:** Wait 1–2 minutes, then visit:
`https://YOUR-USERNAME.github.io/my-summer-projects`

You have a live website on the internet showing off your summer work!

> **Try this!** Share the link with a friend or family member. You just published something to the real internet. Most developers have a GitHub Pages portfolio — you now have one too.

---

## Git & GitHub Cheat Sheet

```bash
# ── Local Git ──────────────────────────────────────────────────
git init                          # Start tracking a directory
git status                        # See what's changed
git add .                         # Stage everything
git add filename                  # Stage one file
git commit -m "message"           # Save a snapshot
git log --oneline                 # See history
git log --oneline --graph --all   # See branches visually
git diff                          # See unstaged changes
git diff --staged                 # See staged changes
git restore filename              # Undo changes to a file
git show a1b2c3d                  # See a specific commit

# ── Branches ───────────────────────────────────────────────────
git branch                        # List branches
git switch -c new-branch          # Create and switch to branch
git switch main                   # Switch to main
git merge new-branch              # Merge branch into current
git branch -d new-branch          # Delete merged branch

# ── GitHub (Remote) ────────────────────────────────────────────
git remote add origin <url>       # Connect to GitHub
git push -u origin main           # First push (sets upstream)
git push                          # Push new commits
git pull                          # Get changes from GitHub
git clone <url>                   # Download a repo from GitHub

# ── Going Back in Time ─────────────────────────────────────────
git reset --soft HEAD~1           # Undo last commit, keep files
git reset --hard HEAD~1           # Undo last commit, lose files
git revert a1b2c3d                # Safely undo a past commit
```

---

## Big Project: Publish Your Summer Work 🌍

Put everything you built this summer onto GitHub so you have a portfolio to show forever.

**Step 1:** Create a repository called `summer-2026` on GitHub.

**Step 2:** Inside it, create folders for each module:

```bash
mkdir summer-2026
cd summer-2026
git init
mkdir linux python ai tombstone
```

**Step 3:** Copy your best scripts from each module into the right folder.

**Step 4:** Create a README.md that describes each project.

**Step 5:** Push everything to GitHub.

**Step 6:** Enable GitHub Pages and publish your portfolio website.

**Step 7:** Share the link with your family. You earned it.

---

## 🏆 Module 5 Badge: Open Source Hero

Earn this badge by completing:
- [ ] Create a GitHub account and add a profile picture
- [ ] Set up SSH keys and connect your computer to GitHub
- [ ] Push your first repository to GitHub
- [ ] Create a branch, make changes, and merge it back
- [ ] Open a pull request on any public repository
- [ ] Write a README with at least 3 sections
- [ ] Publish your summer portfolio with GitHub Pages

---

## What's Next?

You now know how professional developers work — the same tools used at Google, Apple, and every tech company in the world.

Every open source project you love was built with Git and GitHub. And now you know how to contribute to them.

Keep your GitHub active. Keep committing. Keep pushing. Your commit history is your developer portfolio — and it's growing every day.
