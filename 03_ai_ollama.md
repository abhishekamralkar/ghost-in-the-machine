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

Before you can talk to an AI, you need to install the Ollama program that runs it. Think of Ollama like a game launcher — you install it once, and then it can run all kinds of different AI "games" (models) for you. This only takes a few minutes and you never have to pay anything. Once it's installed, your computer becomes its own mini AI server!

Open your terminal and run:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This downloads and installs Ollama. It should take a few minutes.

The `curl` command is like a download manager — it grabs the install script from the internet and runs it automatically. You'll see a bunch of text scroll by as it sets things up.

Verify the install worked:

```bash
ollama --version
```

**What you should see:**
```
ollama version 0.3.x
```
If you see a version number, Ollama is installed and ready to go! If you see an error, ask for help — it probably just needs one more step.

> **Try this!** Run `which ollama` in the terminal. This shows you exactly where on your computer the Ollama program lives. Every program you install has a home — now you know where AI lives on your machine!

---

### Lesson 6.2 — Downloading Your First AI Model

An AI **model** is the "brain" — a large file containing everything the AI learned.

Here's a fun way to think about it: if Ollama is the game launcher, then a model is the actual game. Different models are like different characters with different strengths. Some are super fast but know less. Some know a TON but are slower. You pick the right one for what you need!

```bash
# A good small model (about 2GB)
ollama pull llama3.2

# Even smaller if your computer is slow (about 800MB)
ollama pull llama3.2:1b

# A model that is good at Python code
ollama pull codellama
```

Wait for the download to finish. The progress bar will fill up.

**What you should see** (while downloading):
```
pulling manifest
pulling 966de95ca8a6... 100% ▕████████████████▏ 2.0 GB
pulling 8ab4849b038c... 100% ▕████████████████▏ 1.5 KB
verifying sha256 digest
writing manifest
success
```
That last word — `success` — is what you're waiting for. The download is complete!

> **Try this!** Run `ollama list` after the download finishes. It shows you all the AI brains you have on your computer, how big they are, and when you downloaded them. You're building a collection of AI models!

---

### Lesson 6.3 — Talking to AI in the Terminal

This is the moment you've been waiting for — actually chatting with AI! Right now, no Python, no code — just you and the AI having a conversation in the terminal. It feels like texting a really smart robot. The AI will respond to almost anything: questions, jokes, stories, weird hypotheticals. Try to surprise it!

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

**What you should see** after typing a question:
```
>>> Tell me a joke about computers

Why do programmers prefer dark mode?

Because light attracts bugs! 🐛
```
The AI will type out its answer right below your question. Sometimes it takes a second to "think" — that's normal!

Press `Ctrl+D` or type `/bye` to exit.

> **Try this!** Ask the AI something really weird — like "If dinosaurs had smartphones, what apps would they use?" or "Explain gravity as if you're a confused penguin." The AI will play along! The weirder the question, the more fun the answer.

---

### Lesson 6.4 — One-Line Questions

Sometimes you don't want a full conversation — you just have one quick question and want a quick answer. That's what one-line mode is for. It's like sending a text message to the AI: you fire off your question, it replies, and you're done. This is super handy when you're in the middle of coding and need a fast answer without opening a whole chat session.

You can ask one question without entering chat mode:

```bash
ollama run llama3.2 "Explain gravity in one paragraph for a 9-year-old"

ollama run llama3.2 "Give me 5 fun facts about space"

ollama run llama3.2 "Write a haiku about robots"
```

**What you should see** after the space facts command:
```
Here are 5 fun facts about space:

1. A day on Venus is longer than a year on Venus!
2. Neutron stars are so dense a teaspoon would weigh 10 million tons...
```
The answer appears directly in the terminal and then the command ends. No chat mode needed!

> **Try this!** Put the AI to work for homework help: `ollama run llama3.2 "Give me 3 interesting facts about the American Revolution for a school report"`. Then always double-check the facts in a book or trusted website — AI can be wrong sometimes!

---

### Lesson 6.5 — Ollama Commands to Know

Every great tool has a set of commands to control it. These are your Ollama superpowers — the commands that let you manage your AI models like a pro. Think of it like knowing all the keyboard shortcuts in a game: you don't NEED them, but they make you way faster and more powerful. Knowing these commands means you're not just a user — you're in control.

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

**What you should see** after `ollama list`:
```
NAME              ID              SIZE    MODIFIED
llama3.2:latest   a80c4f17acd5    2.0 GB  2 minutes ago
```
Each row is one AI brain on your computer. The SIZE column shows how much space it takes up.

**What you should see** after `ollama ps` (if Ollama is running):
```
NAME              ID        SIZE      PROCESSOR    UNTIL
llama3.2:latest   abc123    4.1 GB    100% CPU     4 minutes from now
```
If nothing shows up, that just means no model is actively running right now — that's totally fine!

> **Try this!** Pull a second model — try `ollama pull llama3.2:1b` (the tiny version). Then run `ollama list` to see both models. Then try the same question on both: `ollama run llama3.2 "What is DNA?"` and `ollama run llama3.2:1b "What is DNA?"`. Which one gives a better answer? Which one is faster? Bigger isn't always better!

---

## Week 7: Talking to AI with Python

The real fun starts when you use Python to talk to Ollama programmatically.

### Lesson 7.1 — Install the Python Library

Up until now you've been talking to AI through the terminal. Now you're going to write Python code that talks to AI FOR you. This is huge — it means you can build programs that use AI as a tool inside them. You could make a quiz app, a story generator, a homework helper... anything! Before you can do that, you need to set up a special Python workspace called a virtual environment and install the Ollama library.

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

**What you should see** after `pip3 install ollama`:
```
Collecting ollama
  Downloading ollama-0.3.x-py3-none-any.whl (10 kB)
Installing collected packages: ollama
Successfully installed ollama-0.3.x
```
The word `Successfully` is your green light — the library is ready to use in your code!

**What you should see** when `(venv)` is active — your terminal prompt changes:
```
(venv) you@computer:~/ai_projects$
```
That `(venv)` at the start means you're inside the virtual environment. Your installed libraries only live here — they won't mess up anything else on your computer.

> Remember: every time you open a new terminal to work on this project,
> run `source ~/ai_projects/venv/bin/activate` first!

> **Try this!** Run `pip3 list` after installing. It shows every Python package available in your virtual environment. You should see `ollama` in the list. As you build more projects, this list will grow — it's like your Python toolbox!

---

### Lesson 7.2 — Your First Python AI Program

This is a HUGE moment. You're about to write Python code that sends a message to an AI and receives a reply — all without touching the terminal chat! When this works, you've officially crossed into real AI programming territory. This is the same basic skill that powers apps like ChatGPT, Siri, and Alexa — except YOUR program is running locally on YOUR computer.

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

The `messages` list is how you pass your question to the AI. Each message is a small dictionary with two things: `role` (who is talking) and `content` (what they said). The AI's answer comes back in `response["message"]["content"]` — that's where you dig it out to print it.

Run it in your terminal:

```bash
python3 ask_ai.py
```

**What you should see:**
```
2 + 2 equals 4.
```
If you see an answer printed out, it worked! Your Python program just talked to an AI. That's genuinely cool.

> **Try this!** Change the `content` to a different question — like `"Name 3 planets in our solar system"` or `"What rhymes with 'code'?"`. Run it again. The AI answers a new question every time with just one line changed. You're now controlling what the AI thinks about!

---

### Lesson 7.3 — Understanding the Structure

Now that you've sent a basic message, let's look at how conversations are structured. The AI doesn't just see your latest question — it sees the WHOLE conversation as a list of messages. And there's a secret third type of message called a **system prompt** that lets you whisper instructions to the AI that the user never sees. This is where the real power is. It's like programming the AI's personality before the conversation even starts!

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

The system message is invisible to anyone chatting — it's just your secret instructions. Notice how the AI's answer will be shorter and friendlier than usual because you told it to keep things "short and fun" for 5th graders.

**What you should see:**
```
Photosynthesis is basically how plants make their own food using sunlight!
They take in water from the soil, carbon dioxide from the air, and zap it
all together with sunlight to make sugar. The bonus? They release oxygen,
which is the air we breathe. Pretty cool, right?
```
The system prompt is working — shorter, friendlier, and more fun than a textbook answer!

> **Try this!** Change the system prompt to `"You are a grumpy old professor. Answer questions correctly but always complain about how simple the question is."` Keep the same user message. Run it again. See how completely different the answer feels? SAME model, SAME question — totally different personality. That's the power of system prompts!

---

### Lesson 7.4 — Interactive Chat Program

A single question and answer is great, but a real chatbot remembers everything you've said. If you tell it your name in message 1, it should still know your name in message 10. This program does exactly that by storing all messages in a list and sending the whole history every time. Think of it like passing the AI a transcript of your entire conversation every time you speak — it re-reads everything and then replies.

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

**What you should see** when you run it:
```
=================================
  Chat with Sparky the AI Tutor
=================================
Type 'quit' to exit

You: Hi! My name is Alex.
Sparky: Hey Alex! Great to meet you! I'm Sparky, your AI tutor!
        What would you like to learn about today?

You: What's my name?
Sparky: Your name is Alex! You told me just a moment ago. 😊
```
See how Sparky remembered your name? That's the conversation history working — the whole chat list is sent every time!

> **Try this!** Tell Sparky your favourite subject at the start ("I love dinosaurs!"). Then ask several unrelated questions. Later, ask "What's my favourite subject?" — does Sparky remember? This shows you exactly how AI memory works: it's all in that `messages` list. The longer you chat, the more it remembers!

---

### Lesson 7.5 — Streaming (See Words Appear as They're Generated)

Normally `ollama.chat()` waits until the AI finishes the whole answer before showing anything.
**Streaming** lets you see each word appear one at a time — just like ChatGPT does.

Have you ever watched ChatGPT type out its answer word by word? That's streaming! Without streaming, your program just sits frozen until the AI is completely done — which can feel like forever for long answers. With streaming, each tiny piece of the answer appears the instant the AI generates it. It feels alive. It feels like the AI is actually thinking in real time. And honestly? It's way cooler to watch.

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

**What you should see** — words will appear one by one as the AI generates them:
```
Question: Tell me 3 fascinating facts about the ocean
Answer: Here are three fascinating facts about the ocean:

1. The ocean covers about 71% of Earth's surface, but we've only explored...
```
You'll literally watch the words appear as the AI "thinks." If it looks like it's typing in real time — that's exactly what's happening!

> **Try this!** Add a third call to `stream_answer()` with your own question. Notice how different length answers take different amounts of time to stream. Try asking for something really long like `"Write a 10-step guide to becoming a scientist"` — watch it flow in! Then try a short question like `"What is 5 times 5?"` — almost instant. The AI generates words at a pretty steady speed either way.

---

### Mini Project: AI Question Quiz Generator

This is where everything you've learned comes together into something genuinely useful. You're going to write a program that tells the AI what topic to make a question about, waits for the AI to invent a brand new question, parses the AI's response to pull out the question, choices, and answer, and then quizzes you! No two runs of this program will ever be exactly the same — the AI invents fresh questions every time. That's the magic of generative AI.

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

**What you should see:**
```
=== AI QUIZ GENERATOR ===
I'll ask you 3 questions generated by AI!

Generating question 1 about space...

Question 1: What is the largest planet in our solar system?
  A) Earth
  B) Saturn
  C) Jupiter
  D) Neptune

Your answer (A/B/C/D): C
CORRECT!
```
Every time you run this program, the questions will be different! The AI invents them fresh each time. That's what makes it special.

> **Try this!** Add your own topics to the `topics` list! Change it to include `"Harry Potter"`, `"Minecraft"`, `"dinosaurs"`, or `"your favourite subject in school"`. You can make a quiz about literally anything. Try `"video games"` — the AI might surprise you with how much it knows!

---

### Mini Project: AI Story Generator

Stories are one of the things AI is genuinely great at. You're going to build an interactive story generator where YOU choose the hero, the setting, the problem, and the magical item — and the AI weaves them all into an original story just for you. No two stories will ever be the same. This is generative AI at its most fun: you give it the ingredients, and it bakes the cake. If you run it 10 times with the same inputs, you'll get 10 different stories!

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

**What you should see** after filling in the prompts:
```
=== AI STORY GENERATOR ===

Hero's name: Zara
Where does the story take place? An underwater city
What problem does the hero face? A sea monster is blocking the exit
A magical item the hero has: A flute that controls water

Generating your story... please wait...

==================================================
Deep beneath the glittering waves lay Aquara, a city of coral towers
and glowing jellyfish lanterns. Zara, the city's youngest explorer,
raced through the twisting streets as alarms blared...
==================================================
```
Watch the story stream in word by word — it's like watching an author write in real time!

> **Try this!** Run the story generator twice with the EXACT same inputs. You'll get two completely different stories! That's because the AI uses a little bit of randomness every time it generates text. Then try making the story weirder: set the location to "inside a giant cheese" and the magical item to "a rubber duck that talks." The AI will work with whatever you give it!

---

### Mini Project: Explain It Like I'm 9

Have you ever read an explanation of something and it was SO confusing you gave up? This project fixes that. You type in ANY topic — black holes, the stock market, why we dream, how vaccines work — and the AI explains it in simple words with a fun analogy, specifically for someone your age. It's like having a really smart older sibling available 24/7 who never gets annoyed at your questions.

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

**What you should see** when you ask about black holes:
```
=== EXPLAIN IT LIKE I'M 9 ===
Ask about ANYTHING and I'll explain it simply!
Type 'quit' to exit.

What do you want to understand? black holes

--- Explanation ---
A black hole is like a super powerful vacuum cleaner in space. Imagine
if you had a vacuum cleaner so strong it could suck in light itself —
that's basically a black hole! It's a place where gravity got so strong
that nothing, not even light, can escape...

Fun fact: If you fell into a black hole, someone watching from far away
would see you freeze in time at the edge — you'd never seem to fall in!
```
That's a real explanation simple enough to actually understand — and a fact interesting enough to share at dinner!

> **Try this!** Ask it to explain something from your actual schoolwork — something you're confused about. Try topics like `"how does electricity work"`, `"what is inflation"`, or `"why do we have seasons"`. Then check your textbook or ask a parent if the explanation is accurate. Use it as a STARTING POINT for understanding, not the final word!

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

Real programmers use AI to review their code every single day. It's one of the most practical AI skills you can have. Here's how it works: you paste in your Python code, and the AI reads through it like a teacher, finds mistakes, explains what each bug actually does wrong, and suggests how to fix it — all in plain, friendly language. The best part? It also points out something you DID well, so it's not all criticism. Even professional developers use this trick!

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

**What you should see** after pasting some code and typing DONE:
```
Analyzing your code...

Great effort! Here's my review:

🐛 Bug found on line 3: You're missing a colon at the end of your
`if` statement. Python needs that colon to know where the condition ends.

✅ What you did well: Your variable names are really clear and descriptive
— `player_health` is much better than just `h`. Keep that up!
```
The AI goes through your code line by line, explains problems in plain English, and cheers you on too!

Try pasting in one of your earlier programs and see what the AI says!

> **Try this!** Deliberately write code with a bug in it — like forgetting a colon after an `if`, or using the wrong variable name — and paste it in. See if the AI catches it. Then fix the bug and paste it in again. Does the AI give you a clean bill of health? This is a great way to test if you understand the bug yourself before the AI tells you!

---

## Mini Project: AI Dungeon Master 🎲

Remember your RPG battle game from Module 2? Now make the AI narrate it!

You built the game mechanics — health points, attacks, dodge rolls. Now you're going to make the AI write the dramatic story around those mechanics. Every time the hero hits the dragon, instead of just printing "Hit for 20 damage", the AI writes a thrilling sentence about it. It's the difference between a spreadsheet and an epic novel. Same numbers, completely different feeling. This is called **procedural narrative generation** — a real term used in actual video game development!

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

**What you should see:**
```
=== AI BATTLE NARRATOR ===

Event: The hero lands a critical hit with their sword for 20 damage
Narrator: With a battle cry that echoed through the cavern, the hero's
blade found its mark — a devastating blow that sent sparks flying and
left the beast reeling!

Event: The villain is defeated and falls dramatically
Narrator: The dark lord let out one final, earth-shaking roar before
crumpling to the ground, his armour clattering against the cold stone
as silence — glorious, hard-won silence — fell over the battlefield.
```
Same boring game event, completely epic narration. That's the AI doing what it does best!

> **Try this!** Add your OWN events to the `events` list. Make them specific and weird: `"The hero trips over a rock and accidentally defeats the goblin"` or `"The wizard runs out of spell ingredients and has to improvise with a sandwich"`. The AI will narrate ANYTHING dramatically. The funnier the event, the better the narration!

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
