# Module 4 Exercises — Raspberry Pi Tombstone Project

These exercises are meant to be done ON the Raspberry Pi via SSH.
Connect first: `ssh pi@tombstone.local`

---

## Section A: Raspberry Pi Basics

Answer these questions before you start wiring anything.

1. What command do you use to update all software on the Pi?

2. What does SSH stand for, and why is it useful for this project?

3. After running `sudo raspi-config` to enable I2C, what command tells you if the OLED display is connected correctly?

4. What address should you see in the output when the OLED is properly connected?

5. Why does the Pi use a MicroSD card instead of a hard drive?

---

## Section B: Setup Checklist

Complete each step and tick it off. If something doesn't work, write what error you saw and how you fixed it.

- [ ] Flashed Raspberry Pi OS to MicroSD card
- [ ] Pi boots up successfully
- [ ] Connected via SSH from another computer
- [ ] Ran `sudo apt update && sudo apt upgrade -y`
- [ ] Enabled I2C via `raspi-config`
- [ ] Ran `i2cdetect -y 1` and saw `3c` in the grid
- [ ] Created project folder and activated venv: `mkdir ~/tombstone && cd ~/tombstone && python3 -m venv venv && source venv/bin/activate`
- [ ] Installed Python libraries (with venv active): `pip3 install adafruit-circuitpython-ssd1306 pillow RPi.GPIO ollama`
- [ ] Installed Ollama on the Pi
- [ ] Downloaded `llama3.2:1b` model

My notes on any problems I hit:
```
Problem:
Fix:
```

---

## Section C: Display Exercises

**Exercise 1 — Hello Display**

Modify `test_display.py` to show YOUR name instead of "HELLO!".
Also add a second line that shows today's date.

Hint: use Python's `datetime` module:
```python
import datetime
today = datetime.date.today().strftime("%b %d, %Y")
```

**Exercise 2 — Count Down on Screen**

Write a program `countdown_display.py` that counts down from 5 to 0 on the OLED screen.
- Show each number large in the centre of the screen
- Wait 1 second between each number
- Show "GO!" on the final frame

**Exercise 3 — Two-Line Message**

Write a function `show_two_lines(oled, line1, line2)` that displays two lines of text on the OLED.
Test it with:
- Line 1: "Hello Pi!"
- Line 2: "I am alive"

---

## Section D: Button Exercises

**Exercise 4 — Button Counter**

Write `button_counter.py` that:
- Shows a count (starting at 0) on the OLED
- Every time the button is pressed, the count goes up by 1
- The new count is displayed immediately
- When the count reaches 10, show "YOU WIN!" and stop

**Exercise 5 — Button Morse Code**

Write `morse_detector.py` that:
- Detects how long the button is held (short = dot, long = dash)
- Prints "DOT" or "DASH" to the terminal based on press duration
- Short press = held less than 0.5 seconds = "DOT"
- Long press = held 0.5 seconds or more = "DASH"

Hint: record `time.time()` when the button goes LOW, and when it goes HIGH again calculate the difference.

---

## Section E: AI Epitaph Exercises

**Exercise 6 — Test Your Prompts**

Modify `test_ai.py` to try THREE different prompts and compare the results:

Prompt A (original): `"Write a short funny Halloween tombstone epitaph. Made-up name. One or two lines."`

Prompt B: `"Write a Halloween tombstone message for a programmer who wrote too many bugs. Be punny."`

Prompt C: `"Write a very dramatic and tragic tombstone epitaph in old-fashioned Shakespearean English. Keep it short."`

Run each prompt 3 times and see how different the results are. Write down your favourite from each.

**Exercise 7 — Themed Generator**

Modify `generate_epitaph()` to accept a `theme` parameter.
Call it with different themes and display each result.

Themes to try:
- `"pirate"`
- `"space explorer"`
- `"video game character"`
- `"chef"`

Expected function signature:
```python
def generate_epitaph(theme="Halloween"):
    prompt = f"Write a short funny {theme} themed tombstone epitaph..."
```

---

## Section F: Full Program Exercises

**Exercise 8 — Add a Message Log**

Modify `tombstone.py` to save every generated epitaph to a log file `logs/epitaphs.log`.
Each entry should include:
- The epitaph text
- The date and time it was generated
- A separator line `"---"`

Hint: open the file in append mode `"a"` and write to it after each generation.

**Exercise 9 — Startup Screen Customisation**

Modify `show_startup()` to display YOUR name and a custom message.
For example:
```
AI TOMBSTONE
by [your name]
[a spooky emoji or message]
Press button!
```

**Exercise 10 — Button Hold to Quit**

Add a "hold to quit" feature:
- If the user holds the button for more than 3 seconds, the program shuts down cleanly
- Show "GOODBYE..." on the display for 2 seconds before quitting
- Make sure `GPIO.cleanup()` is called

---

## Section G: Troubleshooting Practice

Here are common problems you might hit. For each one, write what you would check first.

| Problem | What I would check first |
|---------|--------------------------|
| OLED shows nothing after running test_display.py | |
| `i2cdetect -y 1` shows no `3c` | |
| Button press does nothing | |
| Ollama gives an error | |
| Program crashes with `ModuleNotFoundError` | |
| Tombstone works but starts very slowly | |
| Pi won't boot | |

---

## Bonus Challenges

1. **Dual language mode:** Randomly pick between English and Spanish for the epitaph. Ask Ollama to write it in the chosen language.

2. **LED flash:** Wire an LED to GPIO 23. Make it flash 3 times every time a new epitaph is generated.

3. **Epitaph voting:** Add TWO buttons — one to generate a new epitaph, one to "save" the current one to a `favourites.txt` file. At the end, print the saved favourites.

4. **Web display:** Use Python's `http.server` module to serve the current epitaph as a web page, so any device on the same Wi-Fi can see it by visiting the Pi's IP address.

5. **Custom boot screen:** Make the startup screen display differently each time using the AI — ask Ollama to generate a spooky one-liner intro message.
