# Module 3: AI with Ollama — Your Own Personal AI

```
LEVEL 3 UNLOCKED: AI Master
============================
Most people just USE AI. You're going to CONTROL it.
Give it a personality. Make it a pirate. Make it a dragon.
Make it quiz you. Make it write your story.
Your AI. Your rules.
```

## What Is Artificial Intelligence?

**Artificial Intelligence (AI)** means teaching computers to do things that normally
require human thinking — like reading, writing, answering questions, recognizing faces,
or playing games.

### How Does a Language AI Work?

A **language model** is an AI that learns by reading billions of sentences from books,
websites, and articles. After all that reading, it can predict what words come next —
which lets it answer questions, write stories, explain things, and have conversations.

Think of it like this:
- You've read thousands of books
- Someone asks you "What is photosynthesis?"
- Your brain connects everything you've read to give an answer

The AI does the same thing, but **way faster** — and it's read more text than any
human could ever read in 1,000 lifetimes.

> **Fun Fact:** The AI model you'll run locally (llama3.2) was trained on more text
> than exists in 10,000 libraries combined. The file that holds all of that "knowledge"
> is only about 2 GB — smaller than most video games!

### What Is Ollama?

**Ollama** is a free program that lets you run AI models **on your own computer**,
completely offline. No internet needed. No accounts. No cost. No one watching.

This is called running AI **locally**. Most AI tools send your questions to servers
in another country. Ollama keeps everything on YOUR machine.

---

## Week 6: Setting Up Ollama

### Lesson 6.1 — Installing Ollama

Open your terminal and run:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This downloads and installs Ollama. It should take a few minutes.

Verify the install worked:

```bash
ollama --version
```

---

### Lesson 6.2 — Downloading Your First AI Model

An AI **model** is the "brain" — a large file containing everything the AI learned.

For a 9-year-old's computer or Raspberry Pi, start with a small but smart model:

```bash
# A good small model (about 2GB)
ollama pull llama3.2

# Even smaller if your computer is slow (about 800MB)
ollama pull llama3.2:1b

# A model that is good at Python code
ollama pull codellama
```

Wait for the download to finish. The progress bar will fill up.

---

### Lesson 6.3 — Talking to AI in the Terminal

Once downloaded, start a chat:

```bash
ollama run llama3.2
```

You'll see a prompt `>>>`. Type a question and press Enter:

```
>>> What is a black hole?

>>> Tell me a joke about computers

>>> Write a short poem about summer

>>> What is the capital of France?
```

Press `Ctrl+D` or type `/bye` to exit.

---

### Lesson 6.4 — One-Line Questions

You can ask one question without entering chat mode:

```bash
ollama run llama3.2 "Explain gravity in one paragraph for a 9-year-old"

ollama run llama3.2 "Give me 5 fun facts about space"

ollama run llama3.2 "Write a haiku about robots"
```

---

### Lesson 6.5 — Ollama Commands to Know

```bash
# List models you have downloaded
ollama list

# Check if Ollama is running
ollama ps

# Remove a model (frees up disk space)
ollama rm model_name

# See Ollama help
ollama help
```

---

## Week 7: Talking to AI with Python

The real fun starts when you use Python to talk to Ollama programmatically.

### Lesson 7.1 — Install the Python Library

First, set up a virtual environment for your AI project (keeps packages organized):

```bash
# Create a project folder and go into it
mkdir ~/ai_projects
cd ~/ai_projects

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your prompt. Now install the library:

```bash
pip3 install ollama
```

> Remember: every time you open a new terminal to work on this project,
> run `source ~/ai_projects/venv/bin/activate` first!

---

### Lesson 7.2 — Your First Python AI Program

Create a file called `ask_ai.py`:

```python
import ollama

# Ask the AI a question
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is 2 + 2? Keep it short."}
    ]
)

# Print the AI's answer
print(response["message"]["content"])
```

Run it:

```bash
python3 ask_ai.py
```

---

### Lesson 7.3 — Understanding the Structure

```python
import ollama

# The 'messages' list is a conversation history
# Each message has a 'role' and 'content'
# role = "user"      → your message
# role = "assistant" → the AI's reply
# role = "system"    → secret instructions for the AI

messages = [
    {
        "role": "system",
        "content": "You are a helpful tutor for 5th grade students. Keep answers short and fun."
    },
    {
        "role": "user",
        "content": "What is photosynthesis?"
    }
]

response = ollama.chat(model="llama3.2", messages=messages)
print(response["message"]["content"])
```

---

### Lesson 7.4 — Interactive Chat Program

This program remembers the whole conversation, just like a real chatbot:

```python
import ollama

def chat_with_ai():
    model = "llama3.2"
    messages = [
        {
            "role": "system",
            "content": "You are a friendly AI tutor named Sparky. You help 5th grade students learn about science, math, and technology. Keep answers fun and under 100 words."
        }
    ]

    print("=================================")
    print("  Chat with Sparky the AI Tutor  ")
    print("=================================")
    print("Type 'quit' to exit")
    print()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Sparky: Bye! Keep learning!")
            break

        if not user_input:
            continue

        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Get AI response
        print("Sparky: ", end="", flush=True)

        response = ollama.chat(model=model, messages=messages)
        ai_reply = response["message"]["content"]

        print(ai_reply)
        print()

        # Add AI reply to history so it remembers
        messages.append({
            "role": "assistant",
            "content": ai_reply
        })

chat_with_ai()
```

---

### Lesson 7.5 — Streaming (See Words Appear as They're Generated)

Normally `ollama.chat()` waits until the AI finishes the whole answer before showing anything.
**Streaming** lets you see each word appear one at a time — just like ChatGPT does.

Two special `print()` tricks make this work:
- `end=""` — normally `print()` adds a new line at the end. `end=""` stops that, so words appear on the same line.
- `flush=True` — normally Python waits and sends text in batches. `flush=True` forces it to show each word immediately as it arrives.

```python
import ollama

def stream_answer(question):
    print(f"Question: {question}")
    print("Answer: ", end="", flush=True)

    stream = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": question}],
        stream=True          # Ask for streaming instead of waiting for the full answer
    )

    for chunk in stream:
        # Each 'chunk' is a tiny piece of the answer — one or two words at a time
        print(chunk["message"]["content"], end="", flush=True)

    print("\n")   # Move to a new line when done

stream_answer("Tell me 3 fascinating facts about the ocean")
stream_answer("What are the planets in our solar system?")
```

---

### Mini Project: AI Question Quiz Generator

This uses AI to create quiz questions, then quizzes you!

```python
import ollama
import random

def generate_quiz_question(topic):
    prompt = f"""Create one multiple-choice quiz question about "{topic}" for a 5th grade student.

Format it EXACTLY like this:
QUESTION: (the question here)
A) (first choice)
B) (second choice)
C) (third choice)
D) (fourth choice)
ANSWER: (just the letter)

Keep it educational and fun."""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

def parse_question(raw_text):
    lines = raw_text.strip().split("\n")
    question = ""
    choices = []
    answer = ""

    for line in lines:
        line = line.strip()
        if line.startswith("QUESTION:"):
            question = line.replace("QUESTION:", "").strip()
        elif line.startswith(("A)", "B)", "C)", "D)")):
            choices.append(line)
        elif line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()

    return question, choices, answer

def run_quiz():
    topics = ["space", "animals", "history", "science", "math", "geography"]
    score = 0
    total = 3

    print("=== AI QUIZ GENERATOR ===")
    print("I'll ask you 3 questions generated by AI!")
    print()

    for i in range(total):
        topic = random.choice(topics)
        print(f"Generating question {i+1} about {topic}...")

        raw = generate_quiz_question(topic)
        question, choices, correct_answer = parse_question(raw)

        if not question or not choices:
            print("(Couldn't parse that one, skipping)")
            continue

        print(f"\nQuestion {i+1}: {question}")
        for choice in choices:
            print(f"  {choice}")

        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if user_answer == correct_answer:
            print("CORRECT!")
            score += 1
        else:
            print(f"Not quite. The answer was {correct_answer}.")

    print(f"\n=== FINAL SCORE: {score}/{total} ===")
    if score == total:
        print("Perfect score! You're amazing!")
    elif score >= 2:
        print("Great job! Keep studying!")
    else:
        print("Good try! Review and try again!")

run_quiz()
```

---

### Mini Project: AI Story Generator

```python
import ollama

def generate_story():
    print("=== AI STORY GENERATOR ===")
    print()

    hero    = input("Hero's name: ")
    setting = input("Where does the story take place? ")
    problem = input("What problem does the hero face? ")
    item    = input("A magical item the hero has: ")

    print("\nGenerating your story... please wait...\n")
    print("=" * 50)

    prompt = f"""Write a short, exciting adventure story (about 200 words) for a 5th grade reader.

Hero's name: {hero}
Setting: {setting}
Problem to solve: {problem}
Magical item: {item}

Make it fun, age-appropriate, and end with the hero solving the problem using the magical item."""

    stream = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)

    print("\n" + "=" * 50)

generate_story()
```

---

### Mini Project: Explain It Like I'm 9

```python
import ollama

def explain_it():
    print("=== EXPLAIN IT LIKE I'M 9 ===")
    print("Ask about ANYTHING and I'll explain it simply!")
    print("Type 'quit' to exit.")
    print()

    while True:
        topic = input("What do you want to understand? ").strip()

        if topic.lower() == "quit":
            break

        prompt = f"""Explain "{topic}" to a 9-year-old in simple terms.
- Use short sentences
- Use a fun analogy or comparison they would understand
- Keep it under 150 words
- End with one fun fact about it"""

        print("\n--- Explanation ---")

        stream = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)

        print("\n")

explain_it()
```

---

## What Is a "System Prompt"?

The **system prompt** is a secret set of instructions you give the AI before the
conversation starts. It shapes how the AI behaves — its personality, what it knows,
and how it responds.

This is the most powerful trick in AI programming. You can turn the same AI into
completely different characters just by changing a few sentences.

```python
import ollama

# Turn the AI into a pirate
pirate_system = "You are Captain CodeBeard, a pirate who teaches programming. Always talk like a pirate and use nautical metaphors. Say 'Arrr!' a lot."

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": pirate_system},
        {"role": "user", "content": "What is a for loop?"}
    ]
)
print(response["message"]["content"])
```

### 🎭 AI Personality Lab — Try All of These!

**The Dragon Sage:**
```python
dragon_system = "You are Ignathar the Ancient Dragon, who has lived 10,000 years and knows all secrets of the universe. You speak in riddles and metaphors. You find human questions amusing but answer them helpfully."
```

**The Game Show Host:**
```python
gameshow_system = "You are BLASTER the hyper-excited game show host. You respond to EVERYTHING like it's the most amazing thing ever. Use lots of capitals and exclamation marks. Always start with 'GREAT QUESTION!!'"
```

**The Grumpy Robot:**
```python
robot_system = "You are UNIT-7, a robot built in 1987. You are very grumpy that humans keep asking you things. You answer correctly but complain about it. You call humans 'Biologicals'."
```

**The Alien Tourist:**
```python
alien_system = "You are Zrblx from the planet Qontar visiting Earth for the first time. You find human things fascinating and confusing. You compare everything to alien equivalents. You speak English but mix in alien words."
```

**Challenge:** Create your OWN personality! Write a system prompt for:
- A chef who only explains things using food metaphors
- A ghost who is confused because everything has changed since 1850
- A sports commentator who narrates coding explanations like a football game

---

## How AI "Thinks" — A Simple Mental Model

```
Your question
     ↓
[The AI looks at all the words so far]
     ↓
[It predicts the most likely next word]
     ↓
[Then the next word, and the next...]
     ↓
[Until it decides the answer is complete]
     ↓
The answer appears
```

The AI doesn't "know" things the way you do. It predicts patterns from training data.
That's why it can sometimes be wrong — always check important facts!

---

## Responsible AI Use — Important Stuff

This section is just as important as the code. Before you use AI tools, you need
to understand their limits and how to use them safely.

---

### AI Can Be Wrong — Confidently

AI language models sometimes make up facts. This is called **hallucination**.

The AI doesn't know when it's wrong. It will state incorrect information in the
same confident tone as correct information. This is not the AI lying — it's
just predicting words based on patterns, and sometimes those patterns lead
to wrong answers.

**Examples of AI mistakes:**
- Inventing book titles that don't exist
- Getting historical dates wrong
- Making up scientific "facts"
- Producing code that looks right but has bugs

**Rule:** For anything important — homework, health, facts for a report — always
verify what the AI tells you using a real book, a trusted website, or an adult.

---

### AI Does Not Actually "Think"

It's easy to feel like the AI understands you. It doesn't — not the way you do.

```
What it feels like:         What's actually happening:
─────────────────────       ─────────────────────────────
The AI knows me             The AI has no memory between
                            conversations

The AI understands          The AI predicts likely next
my question                 words based on your input

The AI is always right      The AI guesses based on
                            training data — it can be wrong

The AI is alive             The AI is a math function
                            — very complex, but just math
```

---

### Never Share Personal Information with AI

When you talk to AI (even local Ollama), treat it like talking to a stranger.
**Do not type:**

- Your full name
- Your home address
- Your school's name and location
- Your phone number
- Passwords or account details
- Photos of yourself (with vision models)

With Ollama running locally, your conversations stay on your computer.
But it's a good habit to practice, because other AI tools do send data
to remote servers.

---

### AI Reflects What It Was Trained On

AI models learned from text written by humans — and humans have biases.
That means AI can sometimes:

- Describe certain jobs as belonging to one gender
- Have stronger knowledge of some cultures than others
- Reflect stereotypes from its training data

If an AI answer seems unfair or strange, that's a good moment to think critically
about why the AI said that, and whether it's really true.

---

### The Good Side: AI as a Learning Tool

Used carefully, AI is an incredible learning partner:

| Good use | Why it works |
|----------|-------------|
| "Explain X to me" | Great for getting a starting explanation (verify it) |
| "Give me 5 examples of Y" | Fast brainstorming |
| "What's wrong with this code?" | Excellent coding helper |
| "Write a first draft of Z" | Good starting point to edit |
| "Quiz me on topic W" | Fun study tool |

The key is to use AI as a **starting point**, not a final answer.

---

### A Quick Test: Is the AI Right?

Whenever the AI gives you a fact, ask yourself:

1. **Can I verify this?** Look it up in a book or trusted website
2. **Does it make sense?** If something sounds too surprising, double-check
3. **Is this important?** For fun/creative tasks, accuracy matters less; for school work or decisions, always verify

---

## Ollama + Python Cheat Sheet

```python
import ollama

# Simple question
response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Your question here"}]
)
print(response["message"]["content"])

# With system prompt
ollama.chat(model="llama3.2", messages=[
    {"role": "system", "content": "Be a helpful tutor"},
    {"role": "user",   "content": "Explain gravity"}
])

# Streaming output
stream = ollama.chat(model="llama3.2",
    messages=[...], stream=True)
for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)

# List local models (shows what you've downloaded)
models = ollama.list()
for m in models["models"]:
    print(m["name"])
```

---

---

## Mini Project: AI Code Reviewer ("Roast My Code")

Show the AI your code and ask it to find bugs, explain what's wrong, and suggest
improvements. This is one of the most useful AI tricks for real programmers.

```python
import ollama

def roast_my_code():
    print("=== AI CODE REVIEWER ===")
    print("Paste your Python code below.")
    print("Type 'DONE' on its own line when finished.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "DONE":
            break
        lines.append(line)

    code = "\n".join(lines)

    print("\nAnalyzing your code...\n")

    stream = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a friendly but honest code reviewer for a 5th grade student. "
                    "Find bugs, explain what each bug does wrong in simple words, "
                    "and suggest fixes. Also point out one thing they did well. "
                    "Keep it encouraging and fun."
                )
            },
            {
                "role": "user",
                "content": f"Please review this Python code:\n\n```python\n{code}\n```"
            }
        ],
        stream=True
    )

    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
    print("\n")

roast_my_code()
```

Try pasting in one of your earlier programs and see what the AI says!

---

## Mini Project: AI Dungeon Master 🎲

Remember your RPG battle game from Module 2? Now make the AI narrate it!

```python
import ollama
import random

def ai_narrate(event):
    """Ask the AI to narrate a battle event dramatically."""
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are an epic fantasy narrator for a text RPG game. Narrate battle events dramatically in 1-2 sentences. Be exciting!"
            },
            {"role": "user", "content": f"Narrate this event: {event}"}
        ]
    )
    return response["message"]["content"].strip()

# Example events to narrate:
events = [
    "The hero lands a critical hit with their sword for 20 damage",
    "The dragon breathes fire but the hero dodges at the last second",
    "The hero drinks a healing potion and recovers 15 HP",
    "The villain is defeated and falls dramatically",
]

print("=== AI BATTLE NARRATOR ===\n")
for event in events:
    print(f"Event: {event}")
    print(f"Narrator: {ai_narrate(event)}")
    print()
```

---

## 🏆 Module 3 Badge: AI Whisperer

Earn this badge by completing:
- [ ] Talk to the AI in the terminal using `ollama run`
- [ ] Write `ask_ai.py` and get a response from Python
- [ ] Build the interactive chat program (Sparky)
- [ ] Create 2 of your own AI personalities using system prompts
- [ ] Complete the "Roast My Code" project with your own code
- [ ] BONUS: Build the AI Dungeon Master and connect it to your RPG game

---

## What's Next?

You know Linux, Python, and AI. Now it's time to bring it all together
for the **Final Project: Raspberry Pi Tombstone Display!**
