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

---

## Section A: Terminal AI Warm-Up

Do these directly in the terminal (no Python yet).

1. Start a chat with the AI:
   ```bash
   ollama run llama3.2
   ```
   Ask it these questions and write down what it says (summarise in one sentence each):
   - "What is the difference between RAM and storage?"
   - "Tell me a joke about Python the programming language"
   - "Explain what a for loop is like I'm 9 years old"

2. Use the one-liner form. Run each and note the answer:
   ```bash
   ollama run llama3.2 "What is the largest planet in the solar system?"
   ollama run llama3.2 "Give me 3 fun facts about octopuses"
   ollama run llama3.2 "Write a haiku about debugging code"
   ```

3. List your downloaded models: `ollama list`
   - What models do you have?
   - How large is each one?

---

## Section B: First Python + AI Programs

**Exercise 4 — Hello AI**

Create `ex04_hello_ai.py`. Ask the AI one question and print the response.
The question should be: `"What is your favourite thing about being an AI?"`

```python
import ollama

# Your code here
```

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

**Exercise 6 — System Prompt Practice**

Create `ex06_system_prompt.py`. Use a system prompt to make the AI respond like a **pirate**.
Ask it: "What is a variable in Python?"

Then change the system prompt to make it respond like a **5-year-old child** who just learned about the topic.
Ask the same question.

Print both responses and compare how different they are!

---

## Section C: Interactive Programs

**Exercise 7 — Ask Anything Loop**

Create `ex07_ask_loop.py`. A program that:
- Keeps asking the user to type a question
- Sends it to the AI and prints the answer
- Stops when the user types `quit`
- Counts how many questions were asked and prints the total at the end

**Exercise 8 — Subject Tutor**

Create `ex08_tutor.py`. Build a tutor chatbot for a school subject of your choice.
The tutor should:
- Have a system prompt that makes it an expert in ONE subject (e.g. space, dinosaurs, history)
- Keep the full conversation history so it remembers what was said
- Give answers that are short and fun for a 9-year-old
- Say goodbye nicely when the user types `exit`

**Exercise 9 — Streaming Practice**

Create `ex09_streaming.py`. Use `stream=True` to get the AI to write:
- A short poem about your favourite animal
- A step-by-step recipe for making a sandwich
- A short story about a robot who wants to be a chef

Print each with a title header and watch the words appear live!

---

## Section D: Creative Challenges

**Exercise 10 — Personality Showdown**

Create `ex10_personality.py`. Ask the same question to THREE different AI personalities and print all three answers.

Question: "What should I do if I'm bored?"

Personalities to try:
- An excited game show host
- A grumpy old wizard
- A friendly robot from the future

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

**Exercise 12 — Story Continuer**

Create `ex12_story.py`. A collaborative story where:
- You write the first sentence
- The AI writes the next two sentences
- You write another sentence
- The AI writes two more
- This repeats for 5 rounds total
- At the end, print the whole story

Hint: keep a `story` string and add to it each round. Pass the whole story as context each time.

---

## Section E: Understanding AI

Answer these questions in your own words (no need to ask the AI — think it through yourself):

1. What is a "system prompt" and why is it powerful?

2. If the AI says "The Eiffel Tower is 500 metres tall" but the real answer is 330 metres, what happened? What should you do?

3. Why is it good that Ollama runs locally (on your computer) instead of sending questions to the internet?

4. If you start a new chat with the AI, does it remember your conversation from yesterday? Why or why not?

5. Give one example of a GOOD use of AI for a school project and one example of a BAD use. Explain why each is good or bad.

---

## Bonus Challenges

**Bonus 1 — Random Personality**
Create `bonus_random_persona.py`. Build a list of 5 different AI personalities.
Each time the program starts, randomly pick one (using `random.choice`).
The user doesn't know which personality they're talking to — can they guess?

**Bonus 2 — Quiz Generator**
Extend the quiz project from Module 3 to:
- Let the user choose the topic before the quiz starts
- Keep score across multiple rounds
- At the end, ask the AI to give personalised study tips based on the topics the user got wrong

**Bonus 3 — AI Dungeon Master**
Connect the AI to your RPG battle game:
- Before each battle, ask the AI to write a dramatic scene-setting intro (2 sentences)
- After each attack, ask the AI to narrate what happened (1 sentence)
- When the battle ends, ask the AI to write an epic win or loss speech
