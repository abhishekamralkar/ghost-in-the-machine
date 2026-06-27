# Module 3 Exercises — AI with Ollama

Make sure Ollama is running before starting.

Open **two** terminal windows:
- **Terminal 1:** Start the Ollama server:
  ```bash
  ollama serve
  ```
  You'll see log messages — leave this running. `ollama serve` is the background process
  that your Python programs talk to. Without it, Python can't reach the AI.
- **Terminal 2:** Write and run your Python programs here.

> **Welcome to AI programming!** In this module you're going to make a real AI respond to your questions — using Python code *you* write. That's something most grown-ups haven't even tried. Take it one exercise at a time and enjoy it!

---

## Section A: Terminal AI Warm-Up

Do these directly in the terminal (no Python yet). This section gets you comfortable talking to the AI before you use it from Python. Think of it as meeting the AI for the first time!

1. Start a chat with the AI:
   ```bash
   ollama run llama3.2
   ```
   Ask it these questions and write down what it says (summarise in one sentence each):
   - "What is the difference between RAM and storage?"
   - "Tell me a joke about Python the programming language"
   - "Explain what a for loop is like I'm 9 years old"

   > **Hint:** When you're done chatting, type `/bye` or press **Ctrl + D** to exit the chat and go back to the normal terminal prompt.

2. Use the one-liner form. Run each and note the answer:
   ```bash
   ollama run llama3.2 "What is the largest planet in the solar system?"
   ollama run llama3.2 "Give me 3 fun facts about octopuses"
   ollama run llama3.2 "Write a haiku about debugging code"
   ```

   > **Hint:** The one-liner form is great for quick questions. Notice how much faster it is than starting a full chat session. Later in Python we'll use a similar approach.

3. List your downloaded models: `ollama list`
   - What models do you have?
   - How large is each one?

   > **Hint:** Model size is shown in gigabytes (GB). Bigger models are usually smarter but slower. `llama3.2` is a good size for learning — it's fast enough to respond quickly on most computers.

---

## Section B: First Python + AI Programs

Now the real fun begins! You're going to write Python code that talks to the AI. The key function you'll use is `ollama.chat()`. It sends a message and gives back a response — just like chatting, but from inside your program.

> **The pattern to remember:** Every `ollama.chat()` call needs a `model` name and a `messages` list. Each message has a `role` ("user" or "assistant" or "system") and `content` (the actual text). You'll use this pattern in almost every exercise!

**Exercise 4 — Hello AI**

Create `ex04_hello_ai.py`. Ask the AI one question and print the response.
The question should be: `"What is your favourite thing about being an AI?"`

```python
import ollama

# Your code here
```

> **Hint:** The basic structure looks like this:
> ```python
> response = ollama.chat(
>     model="llama3.2",
>     messages=[{"role": "user", "content": "your question here"}]
> )
> print(response["message"]["content"])
> ```
> Copy this pattern and swap in the right question. The response comes back as a dictionary — you need `["message"]["content"]` to get the actual text out of it.

**Exercise 5 — Three Questions**

Create `ex05_three_questions.py`. Ask the AI three different questions in a row and print each answer with a label.

Questions:
- "What is photosynthesis?"
- "What is the fastest animal on Earth?"
- "What causes thunder?"

Expected output format:
```
Question 1: What is photosynthesis?
Answer: [AI response here]

Question 2: ...
```

> **Hint:** You can use the same `ollama.chat()` pattern from Exercise 4 three times in a row — once for each question. Or, for a tidier solution, put all three questions in a list and use a `for` loop with `enumerate()` to number them automatically.
>
> **Stuck?** Get one question working first, print it, then add the next two one at a time.

**Exercise 6 — System Prompt Practice**

Create `ex06_system_prompt.py`. Use a system prompt to make the AI respond like a **pirate**.
Ask it: "What is a variable in Python?"

Then change the system prompt to make it respond like a **5-year-old child** who just learned about the topic.
Ask the same question.

Print both responses and compare how different they are!

> **Hint:** A system prompt is a message with `"role": "system"` that goes *before* your question in the messages list. It tells the AI how to behave for the whole conversation:
> ```python
> messages=[
>     {"role": "system", "content": "You are a pirate. Speak like one!"},
>     {"role": "user", "content": "What is a variable in Python?"}
> ]
> ```
>
> **What to notice:** The system prompt is very powerful — the same question gets wildly different answers depending on the personality you set. This is one of the key techniques in real AI programming!

---

## Section C: Interactive Programs

These exercises build programs that have real back-and-forth conversations with the user. You'll use loops so the program keeps running, and you'll learn how to give the AI *memory* of what was said earlier.

**Exercise 7 — Ask Anything Loop**

Create `ex07_ask_loop.py`. A program that:
- Keeps asking the user to type a question
- Sends it to the AI and prints the answer
- Stops when the user types `quit`
- Counts how many questions were asked and prints the total at the end

> **Concepts to use:** `while True` loop, `input()`, `break` to exit when the user types `quit`, a counter variable that increases by 1 each round.
>
> **Hint:** Start with `while True:` and get the user's input inside the loop. Check if it equals `"quit"` right away and `break` if so. Otherwise send it to the AI and print the response. Increment your counter after each successful question.
>
> **Stuck?** Get the basic loop working first (without the AI) — just print "You asked: [question]" in a loop, then add the AI call once the loop logic works.

**Exercise 8 — Subject Tutor**

Create `ex08_tutor.py`. Build a tutor chatbot for a school subject of your choice.
The tutor should:
- Have a system prompt that makes it an expert in ONE subject (e.g. space, dinosaurs, history)
- Keep the full conversation history so it remembers what was said
- Give answers that are short and fun for a 9-year-old
- Say goodbye nicely when the user types `exit`

> **Hint:** The secret to giving the AI memory is to keep a list of all messages and add to it each round. Each time you call `ollama.chat()`, pass the whole list — not just the latest message:
> ```python
> messages = [{"role": "system", "content": "You are a fun dinosaur expert..."}]
>
> # Each round:
> messages.append({"role": "user", "content": user_input})
> response = ollama.chat(model="llama3.2", messages=messages)
> reply = response["message"]["content"]
> messages.append({"role": "assistant", "content": reply})
> ```
>
> **Stuck?** Start with Exercise 7's code (the loop) and add the conversation history list on top of it.

**Exercise 9 — Streaming Practice**

Create `ex09_streaming.py`. Use `stream=True` to get the AI to write:
- A short poem about your favourite animal
- A step-by-step recipe for making a sandwich
- A short story about a robot who wants to be a chef

Print each with a title header and watch the words appear live!

> **Hint:** When you use `stream=True`, the response comes back piece by piece instead of all at once. You loop through the chunks and print each one as it arrives:
> ```python
> stream = ollama.chat(model="llama3.2", messages=[...], stream=True)
> for chunk in stream:
>     print(chunk["message"]["content"], end="", flush=True)
> print()  # newline at the end
> ```
> The `end=""` stops Python from adding a newline after each tiny chunk, and `flush=True` makes it appear immediately.

---

## Section D: Creative Challenges

Time to get creative! These exercises push you to combine everything you've learned. There's no single "right" answer — experiment and see what interesting things you can make the AI do.

**Exercise 10 — Personality Showdown**

Create `ex10_personality.py`. Ask the same question to THREE different AI personalities and print all three answers.

Question: "What should I do if I'm bored?"

Personalities to try:
- An excited game show host
- A grumpy old wizard
- A friendly robot from the future

> **Hint:** Use a system prompt (the `"role": "system"` message) to set each personality. Call `ollama.chat()` three separate times, each with a different system prompt. It's the same question every time — only the system prompt changes!
>
> **Stuck?** Copy your working code from Exercise 6 and adjust the personalities and question.

**Exercise 11 — AI Fact Checker**

Create `ex11_factcheck.py`. The program should:
- Show the user a "fact" (you write 3 fake facts and 2 real ones in a list)
- Ask the AI if the fact is true or false
- Print the AI's verdict

Example facts to use:
- "The Eiffel Tower is in London." (FALSE)
- "Sharks are mammals." (FALSE)
- "Octopuses have three hearts." (TRUE)
- "The Sun is a star." (TRUE)
- "Cats can fly." (FALSE)

Note: The AI might not always be right. That's the point — always verify important facts yourself!

> **Hint:** Store your facts in a Python list. Use a `for` loop to go through each one. For each fact, ask the AI something like: `f"Is this true or false, and why? '{fact}'"`. Print the fact and the AI's answer together so you can compare.
>
> **Try this:** Tell the AI in a system prompt to answer with just "TRUE" or "FALSE" followed by one sentence explanation. Does that make the output easier to read?

**Exercise 12 — Story Continuer**

Create `ex12_story.py`. A collaborative story where:
- You write the first sentence
- The AI writes the next two sentences
- You write another sentence
- The AI writes two more
- This repeats for 5 rounds total
- At the end, print the whole story

Hint: keep a `story` string and add to it each round. Pass the whole story as context each time.

> **Hint:** Each round, pass the current story to the AI and ask it to continue with exactly two sentences. Then `input()` the user's next sentence and add it on. Add each addition to your `story` string so it grows across all 5 rounds.
>
> **Stuck?** Start with just 2 rounds to make sure the logic works, then increase to 5.
>
> **Concepts to use:** `for` loop for the 5 rounds, string concatenation with `+=`, `input()` for user sentences, `ollama.chat()` with the story-so-far as context.

---

## Section E: Understanding AI

Answer these questions in your own words (no need to ask the AI — think it through yourself):

> **This section is important!** Knowing how to use AI is one skill. Knowing *when* to trust it (and when not to) is an even more important skill. Take time to think through these properly.

1. What is a "system prompt" and why is it powerful?

2. If the AI says "The Eiffel Tower is 500 metres tall" but the real answer is 330 metres, what happened? What should you do?

3. Why is it good that Ollama runs locally (on your computer) instead of sending questions to the internet?

4. If you start a new chat with the AI, does it remember your conversation from yesterday? Why or why not?

5. Give one example of a GOOD use of AI for a school project and one example of a BAD use. Explain why each is good or bad.

> **Stuck on question 4?** Think about what you learned in Exercise 8 about conversation history. Where does that history live — in the AI itself, or in your Python program?

---

## Bonus Challenges

**Bonus 1 — Random Personality**
Create `bonus_random_persona.py`. Build a list of 5 different AI personalities.
Each time the program starts, randomly pick one (using `random.choice`).
The user doesn't know which personality they're talking to — can they guess?

> **Hint:** Store each personality as a string in a list. Use `import random` and `random.choice(personalities)` to pick one at the start, then use it as your system prompt. Don't tell the user which one was chosen until they guess!

**Bonus 2 — Quiz Generator**
Extend the quiz project from Module 3 to:
- Let the user choose the topic before the quiz starts
- Keep score across multiple rounds
- At the end, ask the AI to give personalised study tips based on the topics the user got wrong

> **Hint:** Keep a list of the questions the user got wrong. At the end, send that list to the AI and ask for study advice. The AI will give much better advice if you tell it exactly which questions were missed.

**Bonus 3 — AI Dungeon Master**
Connect the AI to your RPG battle game:
- Before each battle, ask the AI to write a dramatic scene-setting intro (2 sentences)
- After each attack, ask the AI to narrate what happened (1 sentence)
- When the battle ends, ask the AI to write an epic win or loss speech

> **Hint:** Keep the AI narration calls simple and short — ask the AI to respond in *exactly* 1 or 2 sentences in your prompt. This keeps the game moving fast and the story exciting!
