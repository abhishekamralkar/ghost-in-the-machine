# Module 0 Exercises — How Computers Work

These exercises help you check what you learned in Module 0. Read each question carefully. Try your best before peeking at the answers — getting it wrong and then figuring out why is how your brain actually learns!

Try to answer each question on your own before checking the answers file.

---

## Section A: Fill in the Blank

This section checks that you remember the key vocabulary from the lesson. If you can fill these in without notes, you really know your stuff! If you get stuck, think back to the analogies — the chef, the desk, the backpack.

1. CPU stands for __________________.
2. RAM stands for __________________.
3. RAM is _______ (fast/slow) but _______ (permanent/temporary).
4. Storage is _______ (fast/slow) but _______ (permanent/temporary).
5. The __________________ is the special program that manages all hardware and starts when you turn on a computer.
6. The Raspberry Pi uses a __________________ card instead of a hard drive.
7. A single 0 or 1 is called a ________. Eight of them make a ________.

> **Tip:** Questions 3 and 4 are a pair — if you remember one, the other is the opposite!

---

## Section B: True or False

Read each statement and decide if it is correct. These questions are great for catching common mix-ups. Think carefully — some of these are sneaky!

1. RAM remembers your files after you turn off the computer. ( True / False )
2. The CPU is like the brain of the computer. ( True / False )
3. Linux is an operating system. ( True / False )
4. A Gigabyte is smaller than a Megabyte. ( True / False )
5. Pressing a button on the Raspberry Pi is an example of INPUT. ( True / False )
6. The OLED screen on the tombstone project is an example of INPUT. ( True / False )

> **Tip for #4:** Remember the order: Kilobyte → Megabyte → Gigabyte → Terabyte. Each one is bigger than the last.
> **Tip for #6:** Ask yourself — is the screen sending information IN to the computer, or is it showing information OUT?

---

## Section C: Match the Analogy

This section tests whether you understand WHY we compare computer parts to real-world things. Analogies are a great way to understand new ideas by connecting them to things you already know. Try to explain each match in your head before writing your answer.

Draw a line (or write the letter) matching each computer part to its real-world analogy.

| Computer Part | Analogy |
|--------------|---------|
| A. CPU       | 1. Your desk (spread out homework while working) |
| B. RAM       | 2. The school principal (manages everything) |
| C. Storage   | 3. The chef (reads recipe and follows steps) |
| D. OS        | 4. Your backpack (keeps things even when you go home) |

> **Tip:** Think about what each thing DOES. The chef cooks — the CPU processes. Your desk holds your current work — RAM holds what the computer is working on right now. Your backpack keeps your stuff safe when school ends — storage keeps data even when the power is off.

---

## Section D: Short Answer

These questions ask you to think and explain in your own words. There is no single right answer for some of them — what matters is that your reasoning makes sense. Write at least one full sentence for each.

1. What happens to everything in RAM when you turn off the computer?

   > **Hint:** Think about what "temporary" means. What happens to the whiteboard at school when someone erases it?

2. If a Python file is saved, where is it stored — RAM or storage? Why?

   > **Hint:** The word "saved" is the key clue here.

3. Name TWO things that run Linux (not just a computer).

   > **What to do if you're stuck:** Think about smart devices around you — your router at home, Android phones, smart TVs. Linux is everywhere!

4. In Minecraft terms: what is your **hotbar** like, and what is your **chest** like?

   > **Hint:** Your hotbar is what you're actively using right now. Your chest stores things for later, even when you log off.

5. A song is about 5 MB. How many songs could fit on a 1 GB storage card?
   (Hint: 1 GB = 1024 MB. Divide 1024 by 5.)

   > **Tip:** You can round your answer — 1024 ÷ 5 is close to 200. Does that seem right for a music player?

---

## Section E: Trace the Program

This is a great challenge! You are going to follow the journey of a program from the moment you press Enter to the moment it finishes. This tests whether you understand how the CPU, RAM, storage, and OS all work together. Try to get all 8 steps — it is okay to use your notes.

Trace what happens step by step when you type `python3 hello.py` and press Enter.
Number each step in order (there are 8 steps — try to get all of them).

```
Step 1: ________________________________________________
Step 2: ________________________________________________
Step 3: ________________________________________________
Step 4: ________________________________________________
Step 5: ________________________________________________
Step 6: ________________________________________________
Step 7: ________________________________________________
Step 8: ________________________________________________
```

> **Tip:** Start with "the shell reads what you typed" and end with "the output appears on screen." Think about what each part of the computer does in between: OS, storage, RAM, CPU.
>
> **What to do if you're stuck:** Try to answer just 4 steps first (start, middle-ish, middle-ish, end). Then fill in the gaps.

---

## Section F: Binary Challenge

Binary might look confusing at first, but it is just a different way of counting — using only 0s and 1s instead of 0-9. Computers use binary because electronic switches can only be ON (1) or OFF (0). These questions will help you see how letters and numbers get turned into binary.

Every letter has a number code (called ASCII). Here are a few:
- A = 65, B = 66, C = 67
- a = 97, b = 98, c = 99
- 0 in binary = 00000000, 1 = 00000001, 2 = 00000010, 65 = 01000001

1. How many bytes does the word `"Hello"` take up?

   > **Hint:** Count the letters. Each letter = 1 byte.

2. If each byte stores one character, how many bytes is your full first name?

   > **Tip:** Spaces count as characters too if your name has two parts!

3. CHALLENGE: The letter A in binary is `01000001`. What do you think B would be?
   (Hint: B = 66, which is one more than 65.)

   > **Tip:** In binary, adding 1 to `01000001` gives you `01000010`. Can you see the pattern? The last digit flips from 1 to 0, and the second-to-last flips from 0 to 1.
   >
   > **What to do if you're stuck:** Try counting in binary from 1: 001, 010, 011, 100. See how the digits flip? The same thing happens here.

---

## Bonus Brain Teaser

This is a real-world maths problem about RAM. Engineers think about this kind of thing every day when they design apps and operating systems. Give it a go — use your calculator if you need to!

A computer has 4 GB of RAM. A video game needs 2 GB. A browser needs 1 GB.
A music player needs 500 MB.

- Can you run all three at the same time? Show your math.
- What if you also want to open a code editor that needs 800 MB?

> **Hint:** Add up all the MB values together (remember: 1 GB = 1024 MB, and 4 GB = 4096 MB). Is the total less than or more than 4096 MB?
>
> **What to do if you're stuck:** Convert everything to MB first. Game = 2048 MB, Browser = 1024 MB, Music = 500 MB. Add them up, then compare to 4096 MB.
