# Module 3 Answers — AI with Ollama

Note: AI responses vary every time — your output will be different from any example shown here.
These answers show the CODE, not the AI's text.

---

## Section A: Terminal AI Warm-Up

These are open-ended — your answers will differ. The key thing is that you RAN the commands and read the responses.

3. `ollama list` shows something like:
```
NAME              ID            SIZE    MODIFIED
llama3.2:latest   a80c4f17acd5  2.0 GB  2 weeks ago
llama3.2:1b       baf6a787fdff  1.3 GB  2 weeks ago
```

---

## Section B: First Python + AI Programs

**Exercise 4 — Hello AI**
```python
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is your favourite thing about being an AI?"}
    ]
)

print(response["message"]["content"])
```

**Exercise 5 — Three Questions**
```python
import ollama

questions = [
    "What is photosynthesis?",
    "What is the fastest animal on Earth?",
    "What causes thunder?",
]

for i, question in enumerate(questions, 1):
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": question}]
    )
    print(f"Question {i}: {question}")
    print(f"Answer: {response['message']['content']}")
    print()
```

**Exercise 6 — System Prompt Practice**
```python
import ollama

question = "What is a variable in Python?"

# Pirate version
pirate_response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a pirate who teaches programming. Always talk like a pirate. Say 'Arrr!' a lot."},
        {"role": "user", "content": question}
    ]
)

# Child version
child_response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a 5-year-old child who just learned about coding. Explain things in the simplest possible words. Use short sentences. Be excited."},
        {"role": "user", "content": question}
    ]
)

print("=== PIRATE VERSION ===")
print(pirate_response["message"]["content"])
print()
print("=== CHILD VERSION ===")
print(child_response["message"]["content"])
```

---

## Section C: Interactive Programs

**Exercise 7 — Ask Anything Loop**
```python
import ollama

count = 0

print("Ask the AI anything! Type 'quit' to stop.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "quit":
        break

    if not question:
        continue

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": question}]
    )

    print(f"AI: {response['message']['content']}\n")
    count += 1

print(f"\nYou asked {count} question(s). Goodbye!")
```

**Exercise 8 — Subject Tutor**
```python
import ollama

subject = input("What subject do you want to learn about? ").strip()

messages = [
    {
        "role": "system",
        "content": f"You are an expert tutor in {subject}. You teach 9-year-old students. Keep all answers fun, short (under 80 words), and use simple words. Use one analogy per answer."
    }
]

print(f"\nWelcome! I'm your {subject} tutor. Ask me anything!")
print("Type 'exit' to leave.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print(f"Tutor: Great session! Keep learning about {subject}. Goodbye!")
        break

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(model="llama3.2", messages=messages)
    reply = response["message"]["content"]

    print(f"Tutor: {reply}\n")
    messages.append({"role": "assistant", "content": reply})
```

**Exercise 9 — Streaming Practice**
```python
import ollama

def stream_response(prompt, title):
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")

    stream = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)

    print("\n")

stream_response(
    "Write a short poem about a golden retriever",
    "POEM: The Golden Retriever"
)

stream_response(
    "Write step-by-step instructions for making the perfect sandwich, numbered 1 to 6",
    "RECIPE: The Perfect Sandwich"
)

stream_response(
    "Write a short story (100 words) about a robot who wants to be a chef but keeps burning the food",
    "STORY: The Cooking Robot"
)
```

---

## Section D: Creative Challenges

**Exercise 10 — Personality Showdown**
```python
import ollama

question = "What should I do if I'm bored?"

personalities = [
    ("Game Show Host", "You are BLASTER, an over-the-top excited game show host. EVERYTHING IS AMAZING. Use lots of capitals and exclamation marks."),
    ("Grumpy Old Wizard", "You are Grognar, a 900-year-old grumpy wizard. You find the question tiresome but answer anyway. You complain a lot."),
    ("Friendly Robot", "You are ARIA-7, a cheerful robot from the year 2350. You find human boredom fascinating. You give futuristic suggestions."),
]

for name, system_prompt in personalities:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    print(f"\n[{name}]")
    print(response["message"]["content"])
    print("-" * 40)
```

**Exercise 11 — AI Fact Checker**
```python
import ollama

facts = [
    ("The Eiffel Tower is in London.", False),
    ("Sharks are mammals.", False),
    ("Octopuses have three hearts.", True),
    ("The Sun is a star.", True),
    ("Cats can fly.", False),
]

print("=== AI FACT CHECKER ===\n")

correct = 0
for fact, actual_truth in facts:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a fact checker. Answer with TRUE or FALSE only, followed by one short sentence explaining why."
            },
            {"role": "user", "content": f"Is this true or false? {fact}"}
        ]
    )

    ai_answer = response["message"]["content"].strip()
    ai_says_true = ai_answer.upper().startswith("TRUE")

    status = "✓" if ai_says_true == actual_truth else "✗ (AI was wrong!)"

    print(f"Fact: {fact}")
    print(f"AI says: {ai_answer}")
    print(f"Result: {status}\n")
```

**Exercise 12 — Story Continuer**
```python
import ollama

print("=== COLLABORATIVE STORY ===\n")
print("You write the first sentence to start our story.\n")

first_sentence = input("Your opening sentence: ").strip()
story = first_sentence + " "

for round_num in range(1, 6):
    print(f"\n[Round {round_num}] AI is writing...")

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are writing a collaborative story with a child. Continue the story with exactly 2 exciting sentences. Do not end the story yet (except on round 5). Output ONLY the 2 sentences, nothing else."
            },
            {
                "role": "user",
                "content": f"Here is the story so far:\n\n{story}\n\nContinue with 2 sentences."
            }
        ]
    )

    ai_part = response["message"]["content"].strip()
    story += ai_part + " "

    if round_num < 5:
        print("\nYour turn — add one sentence to continue the story:")
        your_part = input("> ").strip()
        story += your_part + " "

print("\n" + "="*50)
print("THE COMPLETE STORY")
print("="*50)
print(story)
```

---

## Section E: Understanding AI

1. **System prompt:** A secret instruction you give the AI before the conversation starts. It tells the AI how to behave — its personality, what it knows, and how to respond. It's powerful because you can turn the same AI into completely different characters just by changing a few sentences.

2. **What happened:** The AI "hallucinated" — it confidently stated a wrong fact. You should verify with a real source (Wikipedia, an encyclopedia, a trusted website). The AI isn't lying; it just predicted the wrong words based on its training.

3. **Why local is good:** Your questions stay private on your own machine. No company sees them. No internet is needed. It also works even without Wi-Fi.

4. **Memory between chats:** No — the AI has NO memory between separate conversations. Each new chat starts fresh. Within one chat it remembers because you pass the conversation history in the `messages` list. But close the program and start again, and it forgets everything.

5. **Good use:** "Ask the AI to explain a hard concept from your textbook in simple words, then check the explanation in your book." This speeds up understanding while you still verify the content.
   **Bad use:** "Copy the AI's answer directly into your homework and submit it as your own work." This is dishonest and means you don't actually learn anything. Also, the AI might be wrong.

---

## Bonus 1 — Random Personality

```python
import ollama
import random

personalities = [
    ("Captain CodeBeard",  "You are a pirate who teaches programming. Always talk like a pirate. Say 'Arrr!' a lot. Use nautical metaphors."),
    ("BLASTER",            "You are an over-the-top excited game show host. EVERYTHING IS AMAZING. Use lots of capitals and exclamation marks!!!"),
    ("Grognar the Wizard", "You are a 900-year-old grumpy wizard. You find questions tiresome but answer anyway. You complain about modern times."),
    ("ARIA-7",             "You are a cheerful robot from the year 2350. You find human questions fascinating. Suggest futuristic solutions."),
    ("Ignathar the Dragon","You are an ancient dragon who has lived 10,000 years. You speak in riddles and metaphors. You find humans amusing."),
]

chosen_name, chosen_prompt = random.choice(personalities)

print("You are talking to a mystery personality. Can you guess who it is?")
print("Type 'quit' to give up and see the reveal.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print(f"\nThe mystery personality was: {chosen_name}!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": chosen_prompt},
            {"role": "user",   "content": user_input}
        ]
    )
    print(f"Mystery AI: {response['message']['content']}\n")
```

---

## Bonus 2 — Quiz Generator (Extended)

```python
import ollama
import random

def generate_question(topic):
    prompt = f"""Create one multiple-choice quiz question about "{topic}" for a 5th grade student.

Format EXACTLY like this:
QUESTION: (the question)
A) (first choice)
B) (second choice)
C) (third choice)
D) (fourth choice)
ANSWER: (just the letter)"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

def parse_question(raw):
    lines = raw.strip().split("\n")
    question, choices, answer = "", [], ""
    for line in lines:
        line = line.strip()
        if line.startswith("QUESTION:"):
            question = line.replace("QUESTION:", "").strip()
        elif line.startswith(("A)", "B)", "C)", "D)")):
            choices.append(line)
        elif line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()
    return question, choices, answer

def get_study_tips(wrong_topics):
    if not wrong_topics:
        return "You got everything right — amazing!"
    topics_str = ", ".join(wrong_topics)
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a friendly tutor for 9-year-old students. Give short, encouraging study tips."
            },
            {
                "role": "user",
                "content": f"The student got questions wrong about: {topics_str}. Give 2-3 short study tips to help them improve."
            }
        ]
    )
    return response["message"]["content"]

# ── Main ──────────────────────────────────────────────────────────────────────

topic = input("What topic should the quiz be about? ").strip()
rounds = int(input("How many rounds? (1-5): ").strip())

score = 0
wrong_topics = []

for i in range(rounds):
    print(f"\nGenerating question {i+1}...")
    raw = generate_question(topic)
    question, choices, correct = parse_question(raw)

    if not question or not choices:
        print("(Couldn't generate that one, skipping)")
        continue

    print(f"\nQ{i+1}: {question}")
    for choice in choices:
        print(f"  {choice}")

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Not quite — the answer was {correct}.")
        wrong_topics.append(topic)

print(f"\n=== FINAL SCORE: {score}/{rounds} ===")
print("\nStudy tips from your AI tutor:")
print(get_study_tips(wrong_topics))
```

---

## Bonus 3 — AI Dungeon Master (key snippets)

```python
import ollama

def dm_narrate(event_description, style="epic fantasy narrator"):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": f"You are an {style} for a text RPG. Narrate events dramatically in 1-2 sentences. Be exciting and vivid."
            },
            {"role": "user", "content": f"Narrate: {event_description}"}
        ]
    )
    return response["message"]["content"].strip()

# Usage examples:
print(dm_narrate("The hero enters a dark dungeon for the first time"))
print(dm_narrate("The hero lands a critical hit on the dragon for 20 damage"))
print(dm_narrate("The hero drinks a healing potion and recovers 15 HP"))
print(dm_narrate("The dragon is defeated and falls to the ground"))
```
