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

From your main computer's terminal:

```bash
ssh pi@tombstone.local
```

- `pi` — the username you set up on the Pi
- `tombstone.local` — the hostname you chose (the Pi announces itself on your Wi-Fi)

Enter your password when prompted. You're now controlling the Pi remotely!

> **Tip:** If `tombstone.local` doesn't work, find the Pi's IP address from your
> router's admin page and use `ssh pi@192.168.x.x` instead.

---

### Lesson 8.3 — Update the Pi

```bash
sudo apt update && sudo apt upgrade -y
```

This makes sure all software is current. It may take a few minutes.

---

### Lesson 8.4 — Enable I2C (for the OLED display)

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

---

### Lesson 8.5 — Install Required Software

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

> **Every time you SSH into the Pi** to work on this project, remember to activate
> the venv first: `source ~/tombstone/venv/bin/activate`

---

## Week 9: Building the Tombstone Software

### Lesson 9.1 — Test the OLED Display

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

---

### Lesson 9.2 — Test the Button

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

---

### Lesson 9.3 — Test Ollama AI Message Generation

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

---

## Week 10: The Full Tombstone Program

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

---

## Running the Program

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

```bash
# See if it's running (look for tombstone.py in the list)
ps aux | grep tombstone.py

# Stop it by finding and killing the process
kill $(pgrep -f tombstone.py)
```

> `pgrep -f tombstone.py` finds the process ID automatically so you don't have
> to remember the number. `kill` sends a signal to stop that process.

---

## Making It Start Automatically on Boot

Right now you have to SSH in and run `python3 tombstone.py` by hand every time.
To make the display start **automatically** the moment you plug the Pi in, you
register it as a **systemd service**.

**What is systemd?**
systemd is Linux's startup manager — it controls which programs run when the Pi boots.
You create a small file that says "run this program on startup, and restart it if it crashes."

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

Now every time you plug in the Pi, the tombstone display starts automatically!

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
