# Module 0: How Computers Work — Before We Start

## Why Does This Matter?

Before you can command a computer, you need to understand what it actually is.
A computer is not magic — it's a very fast, very obedient machine made of specific parts.
Once you understand the parts, everything else (Linux, Python, AI) will make much more sense.

---

## The Four Main Parts

### 1. CPU — The Brain

**CPU** stands for **Central Processing Unit**.

The CPU is the part that actually *thinks* — it executes instructions, does math,
makes decisions, and runs every program on your computer.

**Real-world analogy:** The CPU is like a chef in a kitchen. It reads the recipe
(your program), follows each step in order, and produces the result.

- Modern CPUs can execute **billions of instructions per second**
- Your phone has a CPU. Your Raspberry Pi has a CPU.
- When your computer feels "slow," the CPU is usually too busy

```
You type a command
       ↓
  CPU reads it
       ↓
  CPU executes it
       ↓
Result appears on screen
```

---

### 2. RAM — The Notepad

**RAM** stands for **Random Access Memory**.

RAM is where the computer keeps things it is **currently working on**.
It's fast to read and write, but it forgets everything when you turn the computer off.

**Real-world analogy:** RAM is like your desk. When you're doing homework,
you spread your books and papers across the desk. When you're done and pack up,
the desk is empty again — nothing was saved permanently.

- More RAM = you can have more programs open at the same time
- Raspberry Pi 4 comes with 1GB, 2GB, or 4GB of RAM
- When a program crashes with "out of memory," RAM is full

---

### 3. Storage — The Backpack

**Storage** (hard drive, SSD, or MicroSD card) is where files are **permanently saved**.
It keeps your data even when the power is off.

**Real-world analogy:** Storage is like your backpack or bookshelf.
Your homework goes in the backpack, and it's still there tomorrow morning.

- Much slower than RAM, but permanent
- The Raspberry Pi uses a **MicroSD card** as its storage
- When you save a Python file, it goes onto storage

---

### 4. Operating System — The Manager

The **Operating System (OS)** is a special program that runs first when you turn on
the computer. It manages everything else — it decides which programs get CPU time,
controls files on storage, and lets you interact with the hardware.

**Real-world analogy:** The OS is like the principal of a school.
The principal doesn't teach classes (that's programs), but manages the building,
schedules classrooms (CPU), and keeps the library organized (storage).

- **Linux** is an operating system (the one you're learning)
- Windows and macOS are also operating systems
- The Raspberry Pi runs **Raspberry Pi OS**, which is based on Linux

---

## How They All Work Together

```
┌─────────────────────────────────────────────────────┐
│                  YOUR COMPUTER                       │
│                                                      │
│   ┌──────────┐    ┌──────────┐    ┌──────────────┐  │
│   │   CPU    │◄──►│   RAM    │◄──►│   Storage    │  │
│   │ (thinks) │    │(working) │    │  (permanent) │  │
│   └──────────┘    └──────────┘    └──────────────┘  │
│         ▲                                            │
│         │                                            │
│   ┌─────┴──────────────────────────┐                 │
│   │     Operating System (Linux)   │                 │
│   └────────────────────────────────┘                 │
│         ▲                                            │
│         │                                            │
│   ┌─────┴──────────────────────────┐                 │
│   │    Your Programs (Python, etc) │                 │
│   └────────────────────────────────┘                 │
└─────────────────────────────────────────────────────┘
```

---

## What Happens When You Run a Python Program?

Let's trace exactly what happens when you type `python3 hello.py`:

```
1. You type the command in the terminal
        ↓
2. Linux (OS) receives your command
        ↓
3. Linux loads python3 from storage into RAM
        ↓
4. Linux loads your hello.py file from storage into RAM
        ↓
5. The CPU starts reading Python instructions one by one
        ↓
6. CPU executes print("Hello!") → sends text to terminal
        ↓
7. Program ends → RAM is freed up
        ↓
8. Terminal is ready for your next command
```

All of that happens in a fraction of a second.

---

## Input and Output

Computers receive information (**input**) and produce results (**output**).

| Input devices | Output devices |
|--------------|---------------|
| Keyboard | Monitor / screen |
| Mouse | Speaker |
| Microphone | Printer |
| Camera | LED / display |
| GPIO button (Raspberry Pi) | OLED screen (Raspberry Pi) |
| Temperature sensor | Buzzer |

In your tombstone project:
- The **button** is input → you press it to request a new message
- The **OLED display** is output → it shows the generated text

---

## Bits and Bytes — The Language of Computers

Computers only understand **0s and 1s** (called **binary**).
Everything — text, images, music, programs — is stored as billions of 0s and 1s.

| Unit | Size | Example |
|------|------|---------|
| **Bit** | A single 0 or 1 | The smallest unit |
| **Byte** | 8 bits | One character of text |
| **Kilobyte (KB)** | 1,024 bytes | A short text file |
| **Megabyte (MB)** | 1,024 KB | A song |
| **Gigabyte (GB)** | 1,024 MB | A movie |

```
The letter "A" in binary = 01000001

When you type "Hello":
H = 01001000
e = 01100101
l = 01101100
l = 01101100
o = 01101111
```

Your AI model (llama3.2) is about 2 **Gigabytes** — 2 billion bytes of 0s and 1s
that encode everything the AI "knows."

---

## The Terminal — Talking Directly to the OS

When you open a terminal, you get a direct line to the operating system.
Instead of clicking buttons, you type commands. Linux obeys immediately.

```
You (human)
    ↓ type commands
Terminal
    ↓ passes to
Shell (bash/zsh)
    ↓ interprets
Linux Kernel (the core of the OS)
    ↓ controls
Hardware (CPU, RAM, storage, screen)
```

The **shell** (usually `bash` on Linux) is the program that reads your commands
and tells the kernel what to do. You'll learn bash commands in Module 1.

---

## Quick Quiz — Test Yourself

1. What does CPU stand for, and what does it do?
2. What is the difference between RAM and storage?
3. If you write a Python file and then turn off the computer, where is the file saved?
4. Name one input device and one output device on a Raspberry Pi.
5. How many bits are in one byte?

**Answers:** 1) Central Processing Unit — it executes instructions. 2) RAM is fast but temporary; storage is slow but permanent. 3) On the MicroSD card (storage). 4) Button = input, OLED display = output. 5) Eight.

---

## What's Next?

Now that you understand what a computer is, you're ready to start commanding it.
Move on to **Module 1: Linux** to learn how to talk to your computer through the terminal.
