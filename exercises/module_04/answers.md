# Module 4 Answers — Raspberry Pi Tombstone Project

---

## Section A: Raspberry Pi Basics

1. `sudo apt update && sudo apt upgrade -y`

2. **SSH = Secure Shell.** It lets you control the Pi remotely from another computer over the network — so you don't need to plug in a monitor or keyboard directly to the Pi.

3. `sudo i2cdetect -y 1`

4. You should see **`3c`** — that is the I2C address of the SSD1306 OLED display.

5. The Pi has no slot for a traditional hard drive. MicroSD cards are tiny, cheap, and have no moving parts — perfect for a small board computer.

---

## Section B: Setup Checklist

This is hands-on — there are no "right answers" here, but here are common errors:

**Common problems and fixes:**

- **SSH connection refused:** Make sure SSH was enabled in the Imager settings before flashing. Enable with `sudo raspi-config → Interface Options → SSH`.
- **`3c` not showing in i2cdetect:** Double-check the SDA/SCL wiring. Swap VCC and GND and try again (a common beginner mistake).
- **Ollama download hangs:** The Pi's internet connection may be slow. Let it run — `llama3.2:1b` is ~1.3 GB.

---

## Section C: Display Exercises

**Exercise 1 — Hello Display with Date**
```python
import board
import busio
import adafruit_ssd1306
import datetime
from PIL import Image, ImageDraw

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

today = datetime.date.today().strftime("%b %d, %Y")

draw.text((0, 0),  "YOUR NAME HERE", fill=255)
draw.text((0, 20), today, fill=255)

oled.image(image)
oled.show()
print("Done!")
```

**Exercise 2 — Countdown Display**
```python
import board
import busio
import adafruit_ssd1306
import time
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

def show_centered(oled, text):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    # Approximate centering for default font (6px wide, 8px tall)
    x = (oled.width - len(text) * 6) // 2
    draw.text((x, 24), text, fill=255)
    oled.image(image)
    oled.show()

for i in range(5, 0, -1):
    show_centered(oled, str(i))
    time.sleep(1)

show_centered(oled, "GO!")
time.sleep(2)

oled.fill(0)
oled.show()
```

**Exercise 3 — Two-Line Message**
```python
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw

def show_two_lines(oled, line1, line2):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((4, 10), line1, fill=255)
    draw.text((4, 30), line2, fill=255)
    oled.image(image)
    oled.show()

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

show_two_lines(oled, "Hello Pi!", "I am alive")
```

---

## Section D: Button Exercises

**Exercise 4 — Button Counter**
```python
import board
import busio
import adafruit_ssd1306
import RPi.GPIO as GPIO
import time
from PIL import Image, ImageDraw

BUTTON_PIN = 17

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def show_count(oled, count):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((4, 4), "Button Count:", fill=255)
    draw.text((50, 28), str(count), fill=255)
    oled.image(image)
    oled.show()

def show_win(oled):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((20, 24), "YOU WIN!", fill=255)
    oled.image(image)
    oled.show()

count = 0
show_count(oled, count)

try:
    while count < 10:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            count += 1
            if count == 10:
                show_win(oled)
            else:
                show_count(oled, count)
            time.sleep(0.3)   # Debounce
        time.sleep(0.05)
finally:
    GPIO.cleanup()
```

**Exercise 5 — Button Morse Code**
```python
import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press the button. Short = DOT, Long = DASH. Ctrl+C to quit.")

try:
    while True:
        # Wait for button press (goes LOW)
        while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            time.sleep(0.01)

        press_start = time.time()

        # Wait for button release (goes HIGH again)
        while GPIO.input(BUTTON_PIN) == GPIO.LOW:
            time.sleep(0.01)

        duration = time.time() - press_start

        if duration < 0.5:
            print("DOT  (·)")
        else:
            print("DASH (—)")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nDone.")
```

---

## Section E: AI Epitaph Exercises

**Exercise 7 — Themed Generator**
```python
import ollama

def generate_epitaph(theme="Halloween"):
    prompt = (
        f"Write a short funny {theme} themed tombstone epitaph. "
        "Include a made-up punny name on the first line. "
        "Add a one-line message below it. "
        "Keep total under 55 characters. "
        "Only output the epitaph, no explanation."
    )
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": f"You write short funny {theme} themed tombstone epitaphs. Two lines max. Under 55 characters. Only output the epitaph."
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"].strip()

themes = ["pirate", "space explorer", "video game character", "chef"]

for theme in themes:
    print(f"\n[{theme.upper()}]")
    print(generate_epitaph(theme))
```

---

## Section F: Full Program Exercises

**Exercise 8 — Message Log**
```python
import os
import datetime

LOG_FILE = "logs/epitaphs.log"

def log_epitaph(epitaph):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp}\n")
        f.write(epitaph + "\n")
        f.write("---\n")
```

Add `log_epitaph(epitaph)` inside `fetch_and_display()` in `tombstone.py` after `generate_epitaph()` returns.

**Exercise 10 — Button Hold to Quit**
```python
# Add to the main loop alongside the existing button detection:

HOLD_QUIT_SECONDS = 3.0

def on_button_press(channel):
    nonlocal button_pressed
    press_start = time.time()
    # Wait while still held
    while GPIO.input(channel) == GPIO.LOW:
        if time.time() - press_start >= HOLD_QUIT_SECONDS:
            show_message(oled, "GOODBYE...", title="BYE")
            time.sleep(2)
            oled.fill(0)
            oled.show()
            GPIO.cleanup()
            import sys
            sys.exit(0)
        time.sleep(0.05)
    # Short press — generate new message
    button_pressed = True
```

---

## Section G: Troubleshooting Practice

| Problem | What I would check first |
|---------|--------------------------|
| OLED shows nothing after running test_display.py | Run `i2cdetect -y 1` — is `3c` visible? If not, check the SDA/SCL wires. |
| `i2cdetect -y 1` shows no `3c` | Re-check wiring: VCC to Pin 1 (3.3V), GND to Pin 6, SDA to Pin 3, SCL to Pin 5. Also confirm I2C is enabled in raspi-config. |
| Button press does nothing | Check `BUTTON_PIN = 17` matches your actual wiring. Run `test_button.py` and press the button — does it print anything? |
| Ollama gives an error | Run `ollama list` to confirm the model is downloaded. Run `ollama ps` to see if the server is running. Try `ollama serve` in a separate terminal. |
| Program crashes with `ModuleNotFoundError` | Run `pip3 install <missing-module-name>`. Common ones: `adafruit-circuitpython-ssd1306`, `pillow`, `RPi.GPIO`, `ollama`. |
| Tombstone works but starts very slowly | The Pi is generating AI text — this is normal. `llama3.2:1b` (1 billion parameter model) takes 10–30 seconds on the Pi. Use a smaller model or pre-generate messages. |
| Pi won't boot | The MicroSD card may be corrupted. Re-flash it using Raspberry Pi Imager and start again. |

---

## Bonus 3 — Epitaph Voting (key code)

```python
import RPi.GPIO as GPIO

BUTTON_NEW   = 17   # Pin 11 — generate new epitaph
BUTTON_SAVE  = 27   # Pin 13 — save to favourites

GPIO.setup(BUTTON_NEW,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_SAVE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

FAVOURITES_FILE = "favourites.txt"

def save_favourite(epitaph):
    with open(FAVOURITES_FILE, "a") as f:
        f.write(epitaph + "\n---\n")
    print(f"Saved to {FAVOURITES_FILE}")

# In main loop, detect BUTTON_SAVE and call save_favourite(current_message)
```
