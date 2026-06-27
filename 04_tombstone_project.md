# Module 4: Final Project — AI Tombstone Display with Raspberry Pi

```
LEVEL 4 UNLOCKED: Robot Builder
=================================
This is the final boss. You're not just writing code —
you're building a physical device with real hardware.
A tiny computer. A screen. A button. An AI brain.
All built and programmed by YOU.
```

## Project Overview

### What Are We Building?

A **Raspberry Pi** that:
1. Generates spooky Halloween-style tombstone epitaphs using Ollama AI
2. Displays them on a small OLED screen
3. Cycles through new messages every few seconds automatically
4. Has a button you press to get a new message on demand

This is a REAL device — not a simulation. When you're done, you can put it in a
Halloween display, show your friends, or give it as a gift.

This project uses **everything you learned**:
- Linux: to set up the Pi, SSH into it, manage files, run scripts
- Python: to write the entire program
- AI (Ollama): to generate creative messages on the fly
- Hardware: real wires, a real screen, a real button

---

## What Is a Raspberry Pi?

A **Raspberry Pi** is a tiny, cheap computer about the size of a credit card.
It runs Linux, has Python built in, and has pins (called **GPIO**) you can
connect to lights, buttons, sensors, and displays.

```
┌─────────────────────────────────────┐
│         RASPBERRY PI 4              │
│                                     │
│  [USB]  [USB]  [HDMI]               │
│  ████████████████████  [Ethernet]   │
│       GPIO PINS ↑↑↑↑               │
└─────────────────────────────────────┘
```

The Pi can run Ollama and Python, making it a self-contained AI device!

---

## What Is a Tombstone Epitaph?

An **epitaph** is the funny or poetic message carved on a tombstone.
In Halloween decorations, these are usually spooky puns or jokes. Examples:

> "Here lies Al Coholic — He died as he lived"

> "Barry D. Hatchett — Cut down in his prime"

> "Ima Goner — Gone but not forgotten"

> "Will B. Back — Or will he?"

Our AI will generate hundreds of these automatically!

---

## Hardware Shopping List

| Part | Purpose | Approximate Cost |
|------|---------|-----------------|
| Raspberry Pi 4 (2GB or 4GB) | The brain | $35–55 |
| MicroSD card (32GB) | Storage | $8 |
| Power supply (USB-C, 5V 3A) | Power | $8 |
| SSD1306 OLED display (128×64, I2C) | Display | $5 |
| Tactile push button | Request new message | $1 |
| Breadboard + jumper wires | Connecting parts | $5 |
| Optional: small speaker + buzzer | Spooky sounds | $3 |

**Total: approximately $65–85**

---

## Hardware Wiring Guide

### SSD1306 OLED Display (I2C Connection)

```
OLED Pin    →    Raspberry Pi Pin
─────────────────────────────────
VCC (3.3V)  →    Pin 1  (3.3V)
GND         →    Pin 6  (Ground)
SDA         →    Pin 3  (GPIO 2 / I2C SDA)
SCL         →    Pin 5  (GPIO 3 / I2C SCL)
```

### Push Button

```
Button Pin 1  →  Pin 11 (GPIO 17)
Button Pin 2  →  Pin 9  (Ground)
```

### Visual Wiring Diagram

```
Raspberry Pi
  ┌─────────────────┐
  │  Pin 1  (3.3V)──┼────── OLED VCC
  │  Pin 3  (SDA)───┼────── OLED SDA
  │  Pin 5  (SCL)───┼────── OLED SCL
  │  Pin 6  (GND)───┼────── OLED GND
  │  Pin 9  (GND)───┼──┬─── Button Pin 2
  │  Pin 11 (GP17)──┼──┘─── Button Pin 1
  └─────────────────┘
```

> **Safety:** Always power off the Pi before changing wiring!

---

## Week 8: Setting Up the Raspberry Pi

### Lesson 8.1 — Install Raspberry Pi OS

The Raspberry Pi is just bare hardware when you get it — it needs an operating system before it can do anything, just like a new phone needs iOS or Android. We're going to use a tool called **Raspberry Pi Imager** to burn Linux onto the MicroSD card, which the Pi then boots from. Think of the MicroSD card as the Pi's brain — without it, the Pi doesn't even know what a computer is supposed to do. We'll also sneak in some settings (like your Wi-Fi password and SSH access) before we even plug the card in, so the Pi is ready to go the moment it turns on.

1. Download **Raspberry Pi Imager** on a computer
2. Insert the MicroSD card
3. In the Imager, choose **Raspberry Pi OS Lite (64-bit)**
4. Click the gear icon and set:
   - Hostname: `tombstone`
   - Username: `pi`
   - Password: `halloween2026`
   - Enable SSH
   - Set your Wi-Fi name and password
5. Write the image to the SD card
6. Insert SD into Pi, connect display and button, power on

After the Pi boots (give it about 60 seconds the first time), the green LED on the board will blink a few times and then settle into a slow, steady pattern — that means Linux is running and the Pi is waiting for you.

**What you should see:** The Pi's green activity LED blinks quickly during boot, then calms down. No smoke, no sparks — just a quietly humming little computer. If the LED never lights up at all, double-check that the power supply is plugged in properly.

> **Try this!** The Imager lets you pick different OS versions. After you finish the project, try looking at the other options — there's a full desktop version, a gaming version (RetroPie), and even a media center. The same tiny card holds a completely different computer!

---

### Lesson 8.2 — Connect via SSH

**What is SSH?**
SSH (Secure Shell) lets you control the Raspberry Pi from your main computer — over Wi-Fi.
Instead of plugging in a keyboard and monitor to the Pi, you type commands on your
laptop and they run on the Pi. It's like remote control for a computer!

```
Your laptop                            Raspberry Pi
┌──────────────┐    Wi-Fi / network    ┌──────────────┐
│  Your        │ ──────────────────►   │  Pi runs     │
│  terminal    │ ◄──────────────────   │  your        │
│  (you type)  │   results come back   │  commands    │
└──────────────┘                       └──────────────┘
```

This is exactly how professional engineers at big tech companies control servers — the actual computer might be in a data center on the other side of the world, but they type commands on their laptops just like this. You're doing real sysadmin stuff right now. From your main computer's terminal:

```bash
ssh pi@tombstone.local
```

- `pi` — the username you set up on the Pi
- `tombstone.local` — the hostname you chose (the Pi announces itself on your Wi-Fi)

Enter your password when prompted. You're now controlling the Pi remotely!

**What you should see:** After typing your password you'll get a welcome message from the Pi — something like `Linux tombstone 6.x.x...` followed by a new command prompt that says `pi@tombstone:~$`. Every command you type from here runs ON the Pi, not your laptop.

> **Tip:** If `tombstone.local` doesn't work, find the Pi's IP address from your
> router's admin page and use `ssh pi@192.168.x.x` instead.

> **Try this!** Open TWO terminal windows and SSH into the Pi in both of them at the same time. You can run different commands in each window simultaneously — like watching a log file in one window while editing code in the other. Professionals do this constantly!

---

### Lesson 8.3 — Update the Pi

When an OS is freshly installed, it often has slightly older versions of all its software — kind of like buying a new phone that immediately needs 47 app updates. Running `apt update` checks what new versions exist, and `apt upgrade` actually installs them. This is important because newer versions fix security holes and bugs. The `-y` flag just means "yes, go ahead" so you don't have to type "y" a hundred times.

```bash
sudo apt update && sudo apt upgrade -y
```

This makes sure all software is current. It may take a few minutes.

**What you should see:** A long scrolling list of package names as they download and install. The last line will say something like `0 upgraded, 0 newly installed` when everything is already current, or show a count of packages that were upgraded. No red error messages means everything went fine.

> **Try this!** After the upgrade finishes, run `uname -a` to see the exact version of the Linux kernel running on your Pi. The kernel is the very core of the operating system — the part that talks directly to the hardware. You'll see something like `aarch64` in there, which means it's running on an ARM chip — the same type of chip that's in your phone!

---

### Lesson 8.4 — Enable I2C (for the OLED display)

The OLED display talks to the Pi using a communication system called **I2C** (say "eye-squared-see"). Think of I2C like a two-wire walkie-talkie — one wire carries a clock signal (the beat), and the other carries data (the message). The Pi can talk to multiple devices over those same two wires, which is why wiring is so simple. But this feature is turned off by default on the Pi — we need to flip it on using the Pi's configuration tool.

```bash
sudo raspi-config
```

Navigate to:
`Interface Options → I2C → Enable → Yes → Finish`

Reboot:
```bash
sudo reboot
```

After rebooting, reconnect via SSH. Verify the display is detected:

```bash
sudo i2cdetect -y 1
```

You should see `3c` appear in the grid — that's your OLED display!

**What you should see:** The `i2cdetect` command prints a grid of numbers. Most cells show `--` (nothing there), but one cell should show `3c`. That hex address `0x3c` is the OLED's "name" on the I2C bus — proof that the Pi can see and talk to your display. If you see `--` everywhere, double-check your wiring (power off first!).

> **Try this!** Connect the OLED display but leave out one of the data wires (SDA or SCL), then run `i2cdetect` again. You'll see `--` where `3c` used to be. Now put the wire back and run it again — `3c` reappears! This is a great way to understand why every single wire in the diagram matters.

---

### Lesson 8.5 — Install Required Software

A virtual environment (`venv`) is like a private backpack for your project's Python libraries. Instead of installing everything globally (where different projects might fight over versions), each project gets its own backpack. That way, if one project needs version 1 of a library and another needs version 2, they never interfere. After activating the venv, everything you `pip install` goes into that backpack — not the system Python.

First, create a project folder with a virtual environment so all packages stay tidy:

```bash
# Create the project folder
mkdir ~/tombstone
cd ~/tombstone

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your prompt. Now install everything:

```bash
# Python libraries for the OLED display
pip3 install adafruit-circuitpython-ssd1306 pillow

# Python GPIO library for the button
pip3 install RPi.GPIO

# Python library for Ollama
pip3 install ollama
```

Now install Ollama itself and download the AI model:

```bash
# Install Ollama on the Pi
curl -fsSL https://ollama.com/install.sh | sh

# Download the smallest model (Pi has limited RAM)
ollama pull llama3.2:1b
```

**What you should see:** The `pip3 install` commands scroll through download and install messages, ending with "Successfully installed..." for each package. The `ollama pull` command shows a download progress bar — the model is about 1–2 GB, so this might take several minutes on Wi-Fi. When it finishes you'll see "success" and the model name with its size. That AI model is now stored right on the Pi!

> **Every time you SSH into the Pi** to work on this project, remember to activate
> the venv first: `source ~/tombstone/venv/bin/activate`

> **Try this!** Run `pip3 list` after installing everything to see all the packages in your virtual environment. You'll notice packages you didn't install directly — those are *dependencies*, libraries that the libraries you installed depend on. The whole chain got pulled in automatically!

---

## Week 9: Building the Tombstone Software

### Lesson 9.1 — Test the OLED Display

Before building the full program, we always test each piece separately — this is called **unit testing**, and it's a habit that saves hours of debugging later. If something breaks in the full program, you'll already know each individual piece works, so you can focus on where the pieces connect. This test script draws text onto the tiny 128×64 pixel display — 128 pixels wide and 64 pixels tall, which is tiny by phone standards but perfect for a tombstone! The code creates an in-memory "canvas" (an image), draws on it, then pushes that image to the OLED hardware.

Create `test_display.py`:

```python
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Connect to the display
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Create an image to draw on
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Draw some text
draw.text((0, 0),  "HELLO!", fill=255)
draw.text((0, 20), "I am alive!", fill=255)
draw.text((0, 40), "...or am I?", fill=255)

# Show it on the display
oled.image(image)
oled.show()

print("Check your display!")
```

```bash
python3 test_display.py
```

**What you should see:** Three lines of white glowing text appear on the tiny OLED — "HELLO!" near the top, "I am alive!" in the middle, and "...or am I?" near the bottom. The display stays lit after the script finishes. The terminal prints "Check your display!" to confirm the code ran without errors. If the display stays blank, run `sudo i2cdetect -y 1` to check wiring.

> **Try this!** Edit the script and change what the text says. Try adding a fourth line: `draw.text((0, 52), "BOO!", fill=255)`. Then try changing `fill=255` to `fill=0` on one line — what happens? (Hint: 255 means "white pixel on", 0 means "black pixel off".) You can also try drawing a rectangle: `draw.rectangle([0, 0, 127, 63], outline=255)` to put a spooky border around everything!

---

### Lesson 9.2 — Test the Button

Physical buttons are surprisingly tricky! When you press a button, the metal contacts don't make one clean connection — they "bounce" and make dozens of tiny connections and disconnections in a few milliseconds. Without **debouncing**, your code would see one press as 20 presses. That's why the code uses `pull_up_down=GPIO.PUD_UP` (a pull-up resistor that keeps the signal at HIGH until the button pulls it LOW) and a short `time.sleep(0.2)` after detecting a press. GPIO stands for **General Purpose Input/Output** — these are the physical pins on the Pi you connected your button wire to.

Create `test_button.py`:

```python
import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press the button! (Ctrl+C to quit)")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Button pressed!")
            time.sleep(0.2)   # Debounce
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done")
```

**What you should see:** The terminal prints "Press the button! (Ctrl+C to quit)" and then waits. Each time you physically press the button on the breadboard, a new line appears: "Button pressed!" When you press and hold, you might see it printed once or twice — the debounce `sleep` is preventing it from printing hundreds of times. Press Ctrl+C to stop the script and you'll see "Done" printed cleanly.

> **Try this!** Remove the `time.sleep(0.2)` debounce line and press the button once. See how many times "Button pressed!" appears from a single click? That's button bounce in action! Put the sleep back — now try pressing and holding for 2 seconds versus a quick tap. Can you make it print "Button pressed!" exactly 3 times in a row by pressing exactly 3 times? You're debugging hardware!

---

### Lesson 9.3 — Test Ollama AI Message Generation

Now for the coolest part — asking the AI to be creative for us! This test calls Ollama using Python, exactly like you did in Module 3, but now you're running the AI model right on the Pi itself. No internet needed! The AI model is a file stored on the Pi's SD card, and the Pi's processor runs it locally. We're using `llama3.2:1b` — the "1b" means it has 1 billion parameters (basically 1 billion little knobs that were tuned during training). It's the smallest Llama model, which fits in the Pi's limited 2GB of RAM.

Create `test_ai.py`:

```python
import ollama

def generate_epitaph(name=None):
    if name:
        prompt = f'Write a short, funny Halloween tombstone epitaph for someone named "{name}". One or two lines. Spooky pun if possible.'
    else:
        prompt = "Write a short, funny Halloween tombstone epitaph. Use a made-up punny name. One or two lines. Make it spooky and clever."

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": "You generate short, funny Halloween tombstone epitaphs. Keep them under 60 characters total. Use puns and spooky humor. Only output the epitaph, nothing else."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"].strip()

# Test it
for i in range(3):
    print(f"Epitaph {i+1}: {generate_epitaph()}")
```

**What you should see:** The script pauses for a few seconds while the Pi thinks (you might hear the Pi's processor working harder — it gets warm!), then prints three unique tombstone epitaphs like:

```
Epitaph 1: Here lies Phil McCracken — He drilled too deep
Epitaph 2: R.I.P. Sandy Shore — Washed away too soon
Epitaph 3: Ann Tique — Old before her time
```

Every run produces different results because the AI is creative! If you see an error about the model not being found, run `ollama pull llama3.2:1b` again.

> **Try this!** Call `generate_epitaph("your own name")` and see what the AI comes up with for you specifically! Then try passing in silly made-up names like `"I.M. Dead"` or `"Barry Alive"` and see if the AI plays along with the pun. Also try changing `range(3)` to `range(10)` to get 10 epitaphs at once — how long does it take? That gives you a sense of how fast (or slow) the little Pi can run AI!

---

## Week 10: The Full Tombstone Program

Now all three pieces — display, button, and AI — come together into one program that runs forever. This is what software engineers call **integrating** separate components. The main program uses **threading** (running two things at the same time) so that when the AI is thinking and generating a new epitaph, the display can still respond to button presses without freezing. Think of threading like cooking two dishes at once — you start the pasta boiling, then chop vegetables while you wait, instead of just staring at the pot. The program has a clean structure too: setup functions, display functions, and a main loop — organized just like a real production program.

### The Complete `tombstone.py`

```python
"""
Raspberry Pi AI Tombstone Display
Generates spooky epitaphs with Ollama and shows them on an OLED screen.
"""

import time
import threading
import board
import busio
import adafruit_ssd1306
import RPi.GPIO as GPIO
import ollama
from PIL import Image, ImageDraw, ImageFont

# ── Configuration ──────────────────────────────────────────────────────────────

BUTTON_PIN    = 17       # GPIO pin for the button
DISPLAY_WIDTH = 128      # OLED width in pixels
DISPLAY_HEIGHT = 64      # OLED height in pixels
CYCLE_SECONDS = 10       # Auto-cycle new message every N seconds
MODEL         = "llama3.2:1b"

# ── Display Setup ───────────────────────────────────────────────────────────────

def setup_display():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
    oled.fill(0)
    oled.show()
    return oled

# ── Button Setup ────────────────────────────────────────────────────────────────

def setup_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ── AI Message Generation ───────────────────────────────────────────────────────

def generate_epitaph():
    """Ask the AI for a spooky tombstone message."""
    prompt = (
        "Write a short funny Halloween tombstone epitaph. "
        "Include a made-up punny name on the first line. "
        "Add a one-line message below it. "
        "Keep total under 55 characters. "
        "Only output the epitaph, no explanation."
    )
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You write short spooky Halloween tombstone epitaphs. "
                        "Two lines max. Punny names. Under 55 characters total. "
                        "Output ONLY the epitaph."
                    )
                },
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"R.I.P.\nError: {str(e)[:20]}"

# ── Display Rendering ───────────────────────────────────────────────────────────

def wrap_text(text, max_chars=16):
    """Split text into lines that fit the display."""
    words = text.replace("\n", " \n ").split(" ")
    lines = []
    current_line = ""

    for word in words:
        if word == "\n":
            lines.append(current_line.strip())
            current_line = ""
        elif len(current_line) + len(word) + 1 <= max_chars:
            current_line += ("" if not current_line else " ") + word
        else:
            if current_line:
                lines.append(current_line.strip())
            current_line = word

    if current_line:
        lines.append(current_line.strip())

    return lines[:4]   # Max 4 lines on 64px display

def show_message(oled, text, title="R.I.P."):
    """Render a message on the OLED display."""
    image = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    draw  = ImageDraw.Draw(image)

    # Draw a border
    draw.rectangle([0, 0, DISPLAY_WIDTH - 1, DISPLAY_HEIGHT - 1], outline=255)

    # Draw R.I.P. header
    draw.text((4, 3), title, fill=255)
    draw.line([1, 13, DISPLAY_WIDTH - 2, 13], fill=255)

    # Draw the epitaph text
    lines = wrap_text(text)
    y = 16
    for line in lines:
        draw.text((4, y), line, fill=255)
        y += 12

    oled.image(image)
    oled.show()

def show_loading(oled):
    """Show a 'thinking' animation while AI generates."""
    image = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    draw  = ImageDraw.Draw(image)
    draw.rectangle([0, 0, DISPLAY_WIDTH - 1, DISPLAY_HEIGHT - 1], outline=255)
    draw.text((20, 10), "Consulting", fill=255)
    draw.text((15, 24), "the spirits...", fill=255)
    draw.text((30, 40), "👻 🕷 👻", fill=255)
    oled.image(image)
    oled.show()

def show_startup(oled):
    """Splash screen on boot."""
    image = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    draw  = ImageDraw.Draw(image)
    draw.rectangle([0, 0, DISPLAY_WIDTH - 1, DISPLAY_HEIGHT - 1], outline=255)
    draw.text((10, 8),  "AI TOMBSTONE", fill=255)
    draw.text((20, 22), "GENERATOR", fill=255)
    draw.line([1, 35, DISPLAY_WIDTH - 2, 35], fill=255)
    draw.text((8, 39),  "Press button or", fill=255)
    draw.text((12, 51), "wait for magic!", fill=255)
    oled.image(image)
    oled.show()
    time.sleep(3)

# ── Main Program ────────────────────────────────────────────────────────────────

def main():
    print("Starting AI Tombstone Display...")

    oled   = setup_display()
    setup_button()

    show_startup(oled)

    current_message   = ""
    last_gen_time     = 0
    button_pressed    = False
    generating        = False

    def on_button_press(channel):
        nonlocal button_pressed
        button_pressed = True

    GPIO.add_event_detect(
        BUTTON_PIN,
        GPIO.FALLING,
        callback=on_button_press,
        bouncetime=300
    )

    def fetch_and_display():
        nonlocal current_message, last_gen_time, generating
        generating = True
        show_loading(oled)
        epitaph = generate_epitaph()
        current_message = epitaph
        last_gen_time   = time.time()
        show_message(oled, epitaph)
        print(f"Displaying: {epitaph}")
        generating = False

    # Generate the first message
    fetch_and_display()

    try:
        while True:
            time_since_last = time.time() - last_gen_time

            # Generate new message if button was pressed or time is up
            if (button_pressed or time_since_last >= CYCLE_SECONDS) and not generating:
                button_pressed = False
                t = threading.Thread(target=fetch_and_display)
                t.daemon = True
                t.start()

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nShutting down tombstone display.")
        oled.fill(0)
        oled.show()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```

Each function in this program has one job — `setup_display()` sets up the screen, `generate_epitaph()` asks the AI, `show_message()` draws text, `wrap_text()` handles splitting long messages across lines. When a program is organized this way, fixing bugs is much easier because you know exactly where to look.

**What you should see when you run this:**

1. The terminal prints "Starting AI Tombstone Display..."
2. The OLED shows the splash screen: "AI TOMBSTONE GENERATOR" with a border and "Press button or wait for magic!"
3. After 3 seconds, the display switches to "Consulting the spirits..." (the loading screen)
4. A few seconds later, a real AI-generated tombstone epitaph appears on the OLED — with a border, "R.I.P." header, a dividing line, and the message below it
5. Every 10 seconds, it automatically cycles to a new epitaph
6. Press the button any time to immediately skip to a new one
7. The terminal prints each epitaph as it's generated so you can read a log of everything

> **Try this!** Change `CYCLE_SECONDS = 10` to `CYCLE_SECONDS = 5` for faster cycling, or `CYCLE_SECONDS = 30` for slower. Then try changing the title in `show_message(oled, epitaph)` from the default `"R.I.P."` to something else — like `"BOO!"` or your own name. Every setting at the top of the file is a knob you can turn!

---

## Running the Program

Now let's actually launch this thing! The Pi is a real computer running Linux, so starting a Python program works the same way you've been doing it all summer — but with a few extra tricks to keep it running even when you close your laptop.

```bash
# Run manually (stops when you close the terminal or SSH session)
python3 tombstone.py
```

To keep it running **even after you close SSH**, use `nohup` and `&`:

```bash
# nohup = "no hang up" — keeps running after you disconnect
# &     = runs in the background so you get your terminal prompt back
nohup python3 tombstone.py &
```

You'll see a number printed (like `[1] 1234`) — that's the **process ID (PID)**.

**What you should see:** After the `&` sends the program to the background, you get your command prompt back immediately while the tombstone display keeps running on the OLED. The number in brackets (like `[1] 12345`) is the process ID — every running program on Linux gets a unique number, like a name tag.

```bash
# See if it's running (look for tombstone.py in the list)
ps aux | grep tombstone.py

# Stop it by finding and killing the process
kill $(pgrep -f tombstone.py)
```

> `pgrep -f tombstone.py` finds the process ID automatically so you don't have
> to remember the number. `kill` sends a signal to stop that process.

**What you should see after `ps aux | grep tombstone.py`:** A line of output showing the process with the path to `tombstone.py`. If nothing shows up, the program has already stopped (check for errors in the `nohup.out` log file that was automatically created).

> **Try this!** Run `ps aux | grep python3` (without the filename) to see ALL Python programs running on the Pi. You'll probably also see the Ollama server process listed separately. These are all independent programs running simultaneously — that's what a real operating system does: runs many programs at once!

---

## Making It Start Automatically on Boot

Right now you have to SSH in and run `python3 tombstone.py` by hand every time.
To make the display start **automatically** the moment you plug the Pi in, you
register it as a **systemd service**.

**What is systemd?**
systemd is Linux's startup manager — it controls which programs run when the Pi boots.
You create a small file that says "run this program on startup, and restart it if it crashes."

Think of systemd like a restaurant manager — when the restaurant opens (Pi boots), the manager makes sure all the right staff show up (services start). If a chef walks out (a service crashes), the manager immediately calls in a replacement (`Restart=always`). This means even if your tombstone program crashes because of a weird AI response, it automatically restarts within seconds — no SSH needed.

```bash
# Edit the system service file
sudo nano /etc/systemd/system/tombstone.service
```

Paste this inside:

```ini
[Unit]
Description=AI Tombstone Display
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/tombstone/tombstone.py
WorkingDirectory=/home/pi/tombstone
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Save and exit, then activate:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tombstone
sudo systemctl start tombstone

# Check that it's running
sudo systemctl status tombstone
```

**What you should see:** The `systemctl status tombstone` command shows a green dot and the word "active (running)" if everything worked. You'll also see the last few lines of output from the program. Now unplug the Pi, wait 5 seconds, plug it back in — about 30-60 seconds later the tombstone display should spring to life all on its own!

Now every time you plug in the Pi, the tombstone display starts automatically!

> **Try this!** Run `sudo systemctl stop tombstone` to stop the service. Watch the OLED display go dark. Then run `sudo systemctl start tombstone` and watch it come back to life. Now try `sudo systemctl restart tombstone` — it stops AND starts in one command. These three commands (`stop`, `start`, `restart`) are how DevOps engineers manage services on real production servers that millions of people use!

---

## Bonus Features to Add

### Bonus 1: Personalized Epitaphs

Ask for a name before generating:

```python
def generate_personal_epitaph(first_name, last_name):
    prompt = f'Write a Halloween tombstone epitaph for "{first_name} {last_name}". Use their actual name. Make it punny and spooky. Two lines max, under 55 characters.'

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You write short spooky Halloween tombstone epitaphs. "
                    "Use the person's real name. Two lines max. Under 55 characters total. "
                    "Output ONLY the epitaph."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"].strip()

# To use it — ask the user for their name:
first = input("First name for the tombstone: ").strip()
last  = input("Last name for the tombstone: ").strip()
print(generate_personal_epitaph(first, last))
```

### Bonus 2: Different Themes

```python
import random

THEMES = [
    "spooky Halloween",
    "silly and funny",
    "pirate ghost",
    "medieval wizard",
    "zombie scientist",
    "vampire librarian"
]

# Pick a random theme each time
theme = random.choice(THEMES)
prompt = f"Write a {theme} themed tombstone epitaph with a punny name. Two lines, under 55 characters."
```

### Bonus 3: Sound Effects

Add a small buzzer or speaker for spooky startup sounds:

```python
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def play_spooky_tune():
    notes = [262, 294, 247, 220, 196]  # Frequencies in Hz
    for freq in notes:
        p = GPIO.PWM(BUZZER_PIN, freq)
        p.start(50)
        time.sleep(0.2)
        p.stop()
        time.sleep(0.05)
```

### Bonus 4: Multi-Language Mode

```python
languages = ["English", "Spanish", "French", "Japanese"]
lang = random.choice(languages)
prompt = f"Write a Halloween tombstone epitaph in {lang}..."
```

### Bonus 5: Scroll Long Messages

```python
def scroll_text(oled, text, speed=0.05):
    """Scroll long text across the display."""
    for offset in range(0, len(text) * 6, 1):
        image = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        draw  = ImageDraw.Draw(image)
        draw.text((-offset, 20), text, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(speed)
```

---

## Project File Structure

```
/home/pi/tombstone/
├── tombstone.py          ← Main program
├── test_display.py       ← Display test
├── test_button.py        ← Button test
├── test_ai.py            ← AI test
└── logs/
    └── epitaphs.log      ← Save generated messages
```

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| OLED shows nothing | Wiring wrong or I2C not enabled | Run `i2cdetect -y 1`, check wiring |
| Button doesn't respond | Wrong GPIO pin number | Check `BUTTON_PIN` matches your wiring |
| Ollama error | Model not downloaded | Run `ollama pull llama3.2:1b` |
| Program crashes | Python library missing | Run `pip3 install <library-name>` |
| Starts but freezes | Pi running out of RAM | Use `llama3.2:1b` (smallest model) |
| Nothing on boot | Service not enabled | Run `sudo systemctl enable tombstone` |

---

## What You Built — A Complete Summary

Congratulations! Your tombstone project combines:

| Skill | How You Used It |
|-------|----------------|
| **Linux** | Set up the Pi, SSH, file management, systemd service |
| **Python** | Wrote the entire program: classes, loops, threads, files |
| **AI/Ollama** | Generated creative text with a local language model |
| **Hardware** | Wired and programmed an OLED display and GPIO button |
| **Networking** | Connected to Pi via SSH over Wi-Fi |

---

## Ideas for What to Build Next

1. **Weather Display** — Show the forecast on the OLED using a weather API
2. **Countdown Timer** — Count down to a birthday or event
3. **Plant Watering Alert** — Add a soil moisture sensor, alert when plants need water
4. **Security Camera** — Add a Pi Camera, take photos when motion is detected
5. **LED Matrix Sign** — Upgrade from OLED to a bigger LED matrix display
6. **AI Pet** — Add a microphone and speaker so you can talk to your AI with voice

---

## 🏆 Module 4 Badge: Robot Builder

Earn the final badge by completing:
- [ ] Set up Raspberry Pi OS and connect via SSH
- [ ] Wire the OLED display and see it light up
- [ ] Wire the button and see it register presses
- [ ] Run `test_ai.py` and generate 3 epitaphs
- [ ] Run the full `tombstone.py` with all three parts working together
- [ ] Set it up to start automatically on boot

---

## ⭐ Grand Champion: Bonus Master Badge

Earn ALL of these across the whole summer:
- [ ] Module 0: Explain RAM vs Storage to a real person
- [ ] Module 1: Complete all 4 bonus challenges for the Dragon Hoard
- [ ] Module 2: Complete all 5 RPG bonus challenges
- [ ] Module 3: Complete the AI Dungeon Master bonus
- [ ] Module 4: Add at least 2 of the 5 bonus features to the tombstone

---

## You Did It!

```
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗██╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗██║
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║╚═╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
```

You started this summer not knowing what a terminal was.

Now you have:
- Navigated Linux like a pro
- Written programs in Python that actually DO things
- Controlled an AI with your own code
- **Built a physical device** — a real computer with a real screen and real wires

That is genuinely impressive. Most adults cannot do what you just did.
Real engineers at real companies do this exact kind of work every day.

Keep building. Keep breaking things. Keep learning.

The world needs more people who can make computers do interesting things.
