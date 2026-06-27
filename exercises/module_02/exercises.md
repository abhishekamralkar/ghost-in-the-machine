# Module 5 Exercises — Git & GitHub

> **Welcome to version control!** This module's exercises are mostly done in the terminal, not in a code editor. You'll be running `git` commands, creating repositories, and eventually publishing your work on the internet. Take it one step at a time — Git feels confusing at first but clicks fast once you do it a few times.

---

## Section A: Local Git Warm-Up

These exercises use only Git on your own computer — no GitHub yet. If you did the Git section in Module 1, some of this will feel familiar. That's good! Repetition builds muscle memory.

> **The golden rule:** `git status` is your friend. Run it constantly — before and after every command — to see exactly what Git knows about your files.

**Exercise 1 — Create and Track a Project**

1. Create a new folder called `git-practice` in your home directory
2. Inside it, create a file called `hello.txt` with some text in it
3. Initialise a Git repository in this folder
4. Check the status — what colour is `hello.txt`?
5. Stage `hello.txt` and commit it with the message: `"first commit: add hello.txt"`
6. Run `git log --oneline` — you should see your commit

> **Hint:** The four steps you'll repeat forever: `git init` → `git add` → `git commit -m "message"` → `git log`. If `git status` shows red, your file isn't staged yet. If it shows green, you're ready to commit.
>
> **What success looks like:** `git log --oneline` shows one line: your commit ID and message.

---

**Exercise 2 — Make Changes and See the History**

Still in `git-practice`:

1. Add a second line to `hello.txt`
2. Run `git diff` — what does it show?
3. Stage and commit with the message: `"add second line to hello.txt"`
4. Create a brand new file called `notes.txt` with any content
5. Stage and commit: `"add notes.txt"`
6. Run `git log --oneline` — you should see 3 commits now

Now try:
- `git show HEAD` — what does HEAD mean?
- `git show HEAD~1` — what does the `~1` mean?

> **Hint:** `git diff` shows lines that were ADDED (green with `+`) and REMOVED (red with `-`). `HEAD` always means "the most recent commit". `HEAD~1` means "one commit before the most recent". `HEAD~2` would be two commits back.
>
> **What to notice:** Git saves the ENTIRE state of every file at every commit. You can always go back.

---

**Exercise 3 — Undo a Mistake**

1. Open `hello.txt` and delete ALL the text. Save it (pretend you did this by accident)
2. Run `git status` — what does Git say?
3. Run `git diff` — you can see exactly what was deleted
4. Use `git restore hello.txt` to get your text back
5. Open `hello.txt` — it's restored!

> **Hint:** `git restore <filename>` throws away all unsaved changes to that file and puts it back to how it was in the last commit. This only works if you haven't committed the mistake yet.
>
> **Stuck?** Run `git status` first. If the file shows in red under "Changes not staged for commit", `git restore` will fix it.

---

**Exercise 4 — Branches**

1. Create a new branch called `experiment`
2. Switch to it
3. Create a new file called `experiment.txt` with the text: `"This is my experiment"`
4. Commit it with the message: `"add experiment file"`
5. Switch back to `main` — run `ls`. Is `experiment.txt` there?
6. Switch back to `experiment` — run `ls`. Is it there now?

> **Hint:** Use `git switch -c experiment` to create AND switch in one command. The file appears and disappears because it only exists on the `experiment` branch — that's the whole point of branches! Each branch is its own parallel world.
>
> **What success looks like:** `ls` on `main` shows `hello.txt` and `notes.txt`. `ls` on `experiment` shows all three files including `experiment.txt`.

---

**Exercise 5 — Merge and Clean Up**

Continuing from Exercise 4:

1. Switch back to `main`
2. Merge the `experiment` branch into `main`
3. Run `ls` — `experiment.txt` should now be on `main` too!
4. Delete the `experiment` branch (it's done its job)
5. Run `git log --oneline --graph --all` — can you see where the branch split and merged?

> **Hint:** You must be on `main` before you merge. The command is `git merge experiment`. After a successful merge, delete the branch with `git branch -d experiment`.
>
> **What the graph looks like:**
> ```
> *   (HEAD -> main) Merge branch 'experiment'
> |\
> | * add experiment file
> |/
> * add notes.txt
> ```

---

## Section B: Setting Up GitHub

**Exercise 6 — Create Your GitHub Account**

If you don't already have one:
1. Go to [https://github.com](https://github.com) and sign up
2. Verify your email
3. Add a profile picture and a one-line bio
4. Write down your GitHub username — you'll need it in every exercise after this

> **Hint:** Choose a username that you'd be happy showing to a future employer or teacher. GitHub usernames are public. Good format: `firstname-lastname` or a creative but appropriate nickname.

---

**Exercise 7 — Set Up SSH Keys**

This is a one-time setup that connects your computer to GitHub securely.

1. Generate an SSH key pair:
   ```bash
   ssh-keygen -t ed25519 -C "your@email.com"
   ```
   Press Enter three times to accept defaults

2. View your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. Add it to GitHub: **Settings → SSH and GPG keys → New SSH key**

4. Test the connection:
   ```bash
   ssh -T git@github.com
   ```

> **Hint:** You should see: `Hi your-username! You've successfully authenticated`. If you see `Permission denied`, double-check that you pasted the full key (it starts with `ssh-ed25519` and ends with your email).
>
> **What success looks like:** The test command prints your GitHub username. That's it — you're connected. You only have to do this setup once per computer.

---

## Section C: Pushing to GitHub

**Exercise 8 — Push Your First Repository**

1. On GitHub, create a new repository called `git-practice`
   - Leave "Add README" unticked (you already have local files)
   - Copy the SSH URL (looks like `git@github.com:USERNAME/git-practice.git`)

2. In your local `git-practice` folder, connect it to GitHub:
   ```bash
   git remote add origin git@github.com:YOUR-USERNAME/git-practice.git
   git push -u origin main
   ```

3. Go to your GitHub repository page and refresh — your files are there!

> **Hint:** `git remote add origin <url>` tells your local Git "this is where GitHub lives". You only run this once. After that, `git push` is enough. The `-u origin main` flag on the first push sets up the tracking so future pushes just need `git push`.
>
> **What success looks like:** You can see `hello.txt`, `notes.txt`, and `experiment.txt` on your GitHub repository page in the browser.

---

**Exercise 9 — The Push/Pull Cycle**

This simulates working across two computers (or with a teammate).

**Part 1 — Edit on GitHub:**
1. On GitHub, click `hello.txt`, then click the pencil icon to edit it
2. Add a new line: `"Edited directly on GitHub"`
3. Click **Commit changes**

**Part 2 — Pull to your computer:**
1. In your terminal (still in `git-practice`):
   ```bash
   git pull
   ```
2. Open `hello.txt` — the new line should be there!

**Part 3 — Edit locally and push back:**
1. Add another new line to `hello.txt`: `"Edited on my computer"`
2. Stage, commit, and push:
   ```bash
   git add hello.txt
   git commit -m "add line from local computer"
   git push
   ```
3. Refresh GitHub — your new line is there

> **Hint:** `git pull` fetches any new commits from GitHub and applies them to your local files. This is how you keep in sync when working from multiple places.
>
> **What success looks like:** After `git pull`, `git log --oneline` shows the GitHub commit AND your local commits in the right order.

---

## Section D: Collaboration Features

**Exercise 10 — Fork and Explore**

1. Go to `github.com/octocat/Hello-World` (GitHub's official test repository)
2. Click **Fork** → **Create fork**
3. Clone YOUR fork to your computer:
   ```bash
   git clone git@github.com:YOUR-USERNAME/Hello-World.git
   cd Hello-World
   ```
4. Run `git log --oneline` — you can see the history of the original project
5. Run `ls` — what files are in it?

> **Hint:** A fork creates a full copy of someone else's repository in YOUR GitHub account. You can make any changes to your fork without affecting the original. This is how open source contribution works.

---

**Exercise 11 — Open a Pull Request**

Continuing from Exercise 10 (in your `Hello-World` fork):

1. Create a new branch:
   ```bash
   git switch -c my-first-pr
   ```

2. Edit `README` — add a line at the bottom: `"Improved by YOUR-NAME"`

3. Commit and push the branch:
   ```bash
   git add README
   git commit -m "add my name to README"
   git push origin my-first-pr
   ```

4. Go to your fork on GitHub — you'll see a yellow banner saying **"Compare & pull request"** — click it

5. Write a description: "I added my name to show I completed the PR exercise"

6. Click **Create pull request**

> **Hint:** You can't merge this PR into `octocat/Hello-World` — you don't have permission. But you CAN click **Merge pull request** in YOUR OWN fork's pull requests to merge your branch into your fork's main. That's what matters for practice!
>
> **What success looks like:** A pull request exists on GitHub showing the diff of your change. The green "Open" badge is showing.

---

**Exercise 12 — Write a Great README**

Create a new GitHub repository called `summer-2026` and write a README.md that includes:

- A title and 1-sentence description of the project
- A section called "What I Built" listing your 5 modules as bullet points
- A section called "What I Learned" with 3 things
- At least one code snippet using backtick fences
- One link to something you found interesting

Push it to GitHub. The README will display automatically on the repository page.

> **Hint:** Markdown preview: In VS Code, open `README.md` and press `Ctrl+Shift+V` to see a preview of how it will look. Or just push and view it on GitHub — it renders automatically there.
>
> **What success looks like:** Your GitHub repo page shows a nicely formatted README with headings, bullet points, and a code block — not just raw markdown symbols.

---

## Section E: GitHub Pages

**Exercise 13 — Publish a Live Website**

Turn your `summer-2026` repository into a free website:

1. In your `summer-2026` folder locally, create `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Summer 2026 Projects</title>
</head>
<body>
  <h1>My Summer 2026 Projects</h1>
  <p>I spent this summer learning Linux, Python, AI, and Raspberry Pi.</p>
  <ul>
    <li>Linux & Terminal</li>
    <li>Python Games</li>
    <li>AI with Ollama</li>
    <li>Raspberry Pi Tombstone Display</li>
    <li>Git & GitHub</li>
  </ul>
</body>
</html>
```

2. Commit and push it

3. On GitHub: **Settings → Pages → Source: Deploy from branch → main → / (root) → Save**

4. Wait 2 minutes then visit: `https://YOUR-USERNAME.github.io/summer-2026`

> **Hint:** After enabling Pages, GitHub shows you the URL. It might take 1–2 minutes to go live. If you see a 404 error, wait a minute and try again — it's still building.
>
> **What success looks like:** You visit the URL and see your webpage in a browser. Share the link with someone!

---

## Section F: Understanding Git

Answer these questions in your own words. Think about each one before writing.

> **This section matters!** Knowing *why* Git works the way it does makes you a much better developer. Professional developers make mistakes in Git all the time — understanding the concepts is what lets you fix them.

1. What is the difference between `git add` and `git commit`? Why are there two separate steps?

2. What does `HEAD` mean in Git? And what does `HEAD~1` mean?

3. Explain in your own words what a branch is and why you would use one instead of just editing the main code directly.

4. What is the difference between `git pull` and `git clone`? When would you use each one?

5. If a friend makes a change on GitHub and you make a different change on your computer at the same time, what happens when you try to push? How do you fix it?

6. Why do commit messages matter? What makes a GOOD commit message vs a BAD one?

> **Hint for Q6:** Think about this: if a bug appeared in your project three months from now, you'd look through the commit history to find when it was introduced. Would "stuff" or "fixed thing" help you find it? What would a useful message look like?

---

## Bonus Challenges

**Bonus 1 — Git Archaeology**

Go to a popular open source project on GitHub (suggestions: `github.com/python/cpython`, `github.com/torvalds/linux`, `github.com/microsoft/vscode`).

Find the answers to these questions using the GitHub interface:
- How many commits does the project have?
- Who made the most recent commit and what did they change?
- How many open pull requests are there right now?
- Find a commit from more than 5 years ago — what was the project like then?

> **Hint:** Click the commit count (shown near the top of the repo page) to see the full history. Click any commit to see the exact diff — green lines added, red lines removed.

**Bonus 2 — Resolve a Merge Conflict on Purpose**

Set up a conflict yourself and resolve it:

1. In `git-practice`, create a branch called `conflict-test`
2. On `main`, change the first line of `hello.txt` to: `"Hello from main!"`
3. Commit it
4. Switch to `conflict-test`, change the SAME first line to: `"Hello from my branch!"`
5. Commit it
6. Switch to `main` and try `git merge conflict-test`
7. Open the file, resolve the conflict, save, then `git add` and `git commit`

> **Hint:** Git marks the conflict like this:
> ```
> <<<<<<< HEAD
> Hello from main!
> =======
> Hello from my branch!
> >>>>>>> conflict-test
> ```
> Delete the `<<<<`, `====`, `>>>>` lines and keep whichever version (or both!) you want. Then save the file.

**Bonus 3 — Contribute to Open Source**

Find a real open source project that accepts beginner contributions:
- Look for repositories with a `good first issue` label (search GitHub for it)
- Read the project's CONTRIBUTING.md file
- Fork the repo, fix one small thing (even a typo in the README counts!), and open a real pull request

> **Note:** Most big projects review PRs carefully. Your first PR might not be merged, and that's completely normal. The point is to go through the whole process. Write a polite description and be patient.
