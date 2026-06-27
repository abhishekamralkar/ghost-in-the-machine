# Module 4 Exercises — Raspberry Pi Tombstone Project

These exercises are meant to be done ON the Raspberry Pi via SSH.
Connect first: `ssh pi@tombstone.local`

Great work making it to Module 4! This is where things get really exciting — you are going to program a real computer (the Raspberry Pi) and make it show messages on a tiny screen. Take it one step at a time, and don't worry if something breaks. Breaking things and fixing them is how real engineers learn!

---

## Section A: Raspberry Pi Basics

Before you touch any wires or code, it helps to understand how the Raspberry Pi works. These questions will make sure you know the basics. Read back through your notes or the curriculum if you need a reminder — there are no tricks here!

Answer these questions before you start wiring anything.

1. What command do you use to update all software on the Pi?

2. What does SSH stand for, and why is it useful for this project?

3. After running `sudo raspi-config` to enable I2C, what command tells you if the OLED display is connected correctly?

4. What address should you see in the output when the OLED is properly connected?

5. Why does the Pi use a MicroSD card instead of a hard drive?

---

## Section B: Setup Checklist

Hardware setup has more steps than regular coding, and that is totally normal. Go through this checklist slowly — one item at a time. If you get an error, write it down in the notes box at the bottom. That habit will save you a lot of time later!

> **Tip:** If SSH says "Connection refused", the Pi might still be booting. Wait 30 seconds and try again.

> **Tip:** If `i2cdetect -y 1` gives an error about permissions, make sure you enabled I2C in `raspi-config` AND rebooted the Pi afterwards.

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

> **What success looks like for the I2C check:** After running `i2cdetect -y 1`, you will see a grid of dashes and numbers. Look for `3c` somewhere in the grid — that is your OLED display saying hello! If the whole grid is dashes, the display is not connected correctly. Check your wires: SDA goes to GPIO 2 (Pin 3), SCL goes to GPIO 3 (Pin 5), VCC to 3.3V, and GND to any ground pin.

My notes on any problems I hit:
```
Problem:
Fix:
```

---

## Section C: Display Exercises

Now the fun starts! These exercises teach you how to talk to the OLED screen using Python. The screen is tiny (128 x 64 pixels) so you have to think carefully about what you show on it. Each exercise builds on the last one, so do them in order.

> **Before you start:** Make sure your virtual environment is active. You should see `(venv)` at the start of your terminal prompt. If not, run: `source ~/tombstone/venv/bin/activate`

---

**Exercise 1 — Hello Display**

This exercise checks that your display works and that you can show custom text on it. Seeing YOUR name appear on the tiny screen for the first time is a great feeling!

Modify `test_display.py` to show YOUR name instead of "HELLO!".
Also add a second line that shows today's date.

Hint: use Python's `datetime` module:
```python
import datetime
today = datetime.date.today().strftime("%b %d, %Y")
```

> **Tip:** The OLED screen is small, so keep text short. If a line is too long it will get cut off at the right edge. Try to keep each line under 16 characters.

> **What success looks like:** The OLED screen lights up and shows your name on the first line and today's date (like "Jun 26, 2026") on the second line. If nothing shows up at all, run `i2cdetect -y 1` to make sure the display is still detected, then check that your venv is active.

---

**Exercise 2 — Count Down on Screen**

Countdowns are everywhere — rockets, games, microwave ovens. Here you are building one yourself! This exercise teaches you how to update the screen in a loop and how to use `time.sleep()` to add pauses.

Write a program `countdown_display.py` that counts down from 5 to 0 on the OLED screen.
- Show each number large in the centre of the screen
- Wait 1 second between each number
- Show "GO!" on the final frame

> **Tip:** To clear the screen before showing each new number, call `oled.fill(0)` and then `oled.show()` before drawing the new number. Otherwise the old number will still show underneath the new one.

> **Tip:** To draw text in a larger size, look at how to use `ImageFont` with a bigger font file, or use the default font and just position the number in the middle by calculating where x and y should go.

> **What success looks like:** The OLED counts down 5 → 4 → 3 → 2 → 1 → 0 with a one-second pause between each number, then shows "GO!" on the screen and stops.

---

**Exercise 3 — Two-Line Message**

Writing reusable functions is one of the most important skills in programming. Instead of copying the same display code every time, you write it once as a function and call it whenever you need it. This exercise practises exactly that.

Write a function `show_two_lines(oled, line1, line2)` that displays two lines of text on the OLED.
Test it with:
- Line 1: "Hello Pi!"
- Line 2: "I am alive"

> **Tip:** In the Adafruit SSD1306 library, text is drawn with `draw.text((x, y), "your text", fill=255)`. For the first line, use `y=0`. For the second line, use `y=16` (or `y=32` if you want more space between lines).

> **What success looks like:** Both lines appear on the OLED display at the same time. "Hello Pi!" is near the top and "I am alive" is below it. If only one line shows, double-check that you are calling `oled.show()` AFTER drawing both lines — not between them.

---

## Section D: Button Exercises

Buttons make your project interactive! Instead of just displaying things, the user can now control what happens. These exercises teach you how to read a physical button using GPIO (General Purpose Input/Output) pins. Be patient — GPIO can be tricky at first.

> **Before you start:** Make sure your button is wired correctly. One leg goes to GPIO 17 (Pin 11) and the other goes to GND (Pin 9). If you are not sure, ask for help before running the code — wiring to the wrong pin will not break anything, but the button just won't work.

> **What to do if you're stuck with the button:** Run this quick test in Python to check if the Pi can see the button press:
> ```python
> import RPi.GPIO as GPIO, time
> GPIO.setmode(GPIO.BCM)
> GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
> while True:
>     print(GPIO.input(17))
>     time.sleep(0.1)
> ```
> When you press the button you should see `0` printed. When you release it, you should see `1`. If you only ever see `1`, the button is not wired correctly.

---

**Exercise 4 — Button Counter**

This is the first exercise where the screen and the button work together. Every button press changes what you see on the screen in real time — that is the magic of interactive hardware!

Write `button_counter.py` that:
- Shows a count (starting at 0) on the OLED
- Every time the button is pressed, the count goes up by 1
- The new count is displayed immediately
- When the count reaches 10, show "YOU WIN!" and stop

> **Tip:** Use `GPIO.wait_for_edge(17, GPIO.FALLING)` to wait for a button press. A FALLING edge means the signal goes from HIGH (1) to LOW (0), which is when the button is pressed (because the pull-up resistor keeps it HIGH when not pressed).

> **Tip:** Add a small sleep after detecting a press (like `time.sleep(0.2)`) to avoid counting the same press multiple times. This is called "debouncing".

> **What success looks like:** The OLED shows "0" at the start. Each button press makes the number go up and the screen updates right away. After 10 presses the screen shows "YOU WIN!" and the program stops cleanly.

---

**Exercise 5 — Button Morse Code**

Morse code uses short and long signals to send messages. This exercise teaches you to measure TIME — how long something lasts. That is a really useful skill for any project that reacts to user input.

Write `morse_detector.py` that:
- Detects how long the button is held (short = dot, long = dash)
- Prints "DOT" or "DASH" to the terminal based on press duration
- Short press = held less than 0.5 seconds = "DOT"
- Long press = held 0.5 seconds or more = "DASH"

Hint: record `time.time()` when the button goes LOW, and when it goes HIGH again calculate the difference.

> **Tip:** You need to detect TWO edges: one when the button is pressed (FALLING) and one when it is released (RISING). Record the time at both edges, then subtract to get the duration.

> **Tip:** If your program prints double DOTs for a single press, it is probably bouncing. Add `GPIO.add_event_detect` with a `bouncetime=200` parameter to ignore quick repeated signals.

> **What success looks like:** When you tap the button quickly the terminal prints "DOT". When you hold it down for more than half a second it prints "DASH". Try spelling your initials in Morse code!

---

## Section E: AI Epitaph Exercises

This is where the project comes together! You are going to use Ollama (a local AI) to generate creative text, then display it on your screen. The AI runs right on the Pi — no internet needed. These exercises teach you how to talk to an AI from Python and how to shape its responses with good prompts.

> **Before you start:** Make sure Ollama is running and the model is downloaded. Test it first by typing `ollama run llama3.2:1b` in the terminal. If you see a `>` prompt, it is ready. Type `/bye` to exit. If Ollama is not running, start it with `ollama serve` in a separate terminal window.

---

**Exercise 6 — Test Your Prompts**

The words you give to an AI (called a "prompt") have a huge effect on what it writes back. This exercise teaches you that skill — called "prompt engineering" — by letting you compare different prompts side by side. Professional AI engineers do this every day!

Modify `test_ai.py` to try THREE different prompts and compare the results:

Prompt A (original): `"Write a short funny Halloween tombstone epitaph. Made-up name. One or two lines."`

Prompt B: `"Write a Halloween tombstone message for a programmer who wrote too many bugs. Be punny."`

Prompt C: `"Write a very dramatic and tragic tombstone epitaph in old-fashioned Shakespearean English. Keep it short."`

Run each prompt 3 times and see how different the results are. Write down your favourite from each.

> **Tip:** The AI gives a slightly different answer every time — that is normal and intentional. It is called "temperature" and makes the AI more creative. If you want more consistent results, you can add `"options": {"temperature": 0.1}` to the `ollama.generate()` call.

> **What success looks like:** Each prompt produces a different style of epitaph. Prompt A is goofy, Prompt B has programming jokes, Prompt C sounds ancient and dramatic. You can see how the wording of your prompt shapes the AI's whole personality!

---

**Exercise 7 — Themed Generator**

Adding a parameter to a function makes it much more flexible — one function can do many different things depending on what you pass in. This exercise teaches that idea using AI themes. You write the function once, then call it with different themes to get totally different results.

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

> **Tip:** The `theme="Halloween"` part is a default value. It means if someone calls `generate_epitaph()` without passing a theme, it will use "Halloween" automatically. This is good coding practice — it makes your function easier to use.

> **What success looks like:** Calling `generate_epitaph("pirate")` gives you something with "arr" and treasure, while `generate_epitaph("space explorer")` gives you something about galaxies. Each theme produces a completely different flavour of epitaph!

---

## Section F: Full Program Exercises

You now know all the pieces: the display, the button, and the AI. These exercises combine everything into a polished, complete program. Think of this as your "final boss" level — harder, but very satisfying when it works!

---

**Exercise 8 — Add a Message Log**

Saving data to a file is one of the most useful things a program can do. Log files let you look back at what happened — coders and engineers use them for everything. This exercise teaches you how to write to a file in Python.

Modify `tombstone.py` to save every generated epitaph to a log file `logs/epitaphs.log`.
Each entry should include:
- The epitaph text
- The date and time it was generated
- A separator line `"---"`

Hint: open the file in append mode `"a"` and write to it after each generation.

> **Tip:** First make sure the `logs/` folder exists. You can create it in your code with:
> ```python
> import os
> os.makedirs("logs", exist_ok=True)
> ```
> The `exist_ok=True` part means it won't crash if the folder already exists.

> **What success looks like:** After pressing the button a few times, run `cat ~/tombstone/logs/epitaphs.log` in the terminal and you will see all your generated epitaphs listed with timestamps. Each one is separated by `---`.

---

**Exercise 9 — Startup Screen Customisation**

First impressions matter! A great startup screen makes your project feel like a real product. This exercise is also a chance to add your own creative touch — make it yours!

Modify `show_startup()` to display YOUR name and a custom message.
For example:
```
AI TOMBSTONE
by [your name]
[a spooky emoji or message]
Press button!
```

> **Tip:** The OLED only shows basic ASCII characters by default — emoji might not display unless you load a special font that supports them. Try a spooky word instead, like "BOO!" or "BEWARE".

> **Tip:** Add a `time.sleep(2)` at the end of `show_startup()` so the user has time to read the screen before the main program takes over.

> **What success looks like:** Every time the tombstone program starts, the OLED shows your custom splash screen for about 2 seconds, then transitions into the main "Press button!" waiting state.

---

**Exercise 10 — Button Hold to Quit**

Clean shutdown is important for the Raspberry Pi — just pulling the power can sometimes corrupt the MicroSD card. This exercise teaches you how to detect a LONG button press and use it to shut down gracefully. Real hardware products do exactly this!

Add a "hold to quit" feature:
- If the user holds the button for more than 3 seconds, the program shuts down cleanly
- Show "GOODBYE..." on the display for 2 seconds before quitting
- Make sure `GPIO.cleanup()` is called

> **Tip:** You can check for a hold while also watching for short presses by tracking the time at press and checking the duration at release — similar to what you did in Exercise 5. If the duration is more than 3 seconds, trigger the shutdown. If less, treat it as a normal epitaph request.

> **What success looks like:** A quick button tap generates a new epitaph as normal. But holding the button down for 3+ seconds shows "GOODBYE..." on the OLED, waits 2 seconds, then exits the program cleanly without any Python error messages.

---

## Section G: Troubleshooting Practice

Every engineer hits problems — the skill is knowing how to debug them. This section trains that skill. Try to fill in the table yourself first before looking anything up. There are no wrong answers here — just your best guess based on what you have learned.

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

> **Hint for the first row:** If the OLED shows nothing, check in this order: (1) Is I2C enabled? (2) Does `i2cdetect -y 1` show `3c`? (3) Is the venv active? (4) Did you call `oled.show()` after drawing?

> **Hint for ModuleNotFoundError:** This almost always means the venv is not active, or you installed the library outside the venv. Run `source ~/tombstone/venv/bin/activate` and try again.

---

## Bonus Challenges

You finished the main exercises — that is awesome! These bonus challenges are for when you want to go further. Each one teaches a new skill that goes beyond what the main exercises covered.

1. **Dual language mode:** Randomly pick between English and Spanish for the epitaph. Ask Ollama to write it in the chosen language.
   > **New skill:** Using Python's `random` module to make decisions, and how to write multi-language prompts for AI.

2. **LED flash:** Wire an LED to GPIO 23. Make it flash 3 times every time a new epitaph is generated.
   > **New skill:** Controlling an output device (LED) with GPIO. This is the opposite of reading a button — instead of listening for a signal, you are SENDING one.

3. **Epitaph voting:** Add TWO buttons — one to generate a new epitaph, one to "save" the current one to a `favourites.txt` file. At the end, print the saved favourites.
   > **New skill:** Managing multiple GPIO inputs at the same time, and combining file-writing with user interaction to build a simple "save favourite" feature.

4. **Web display:** Use Python's `http.server` module to serve the current epitaph as a web page, so any device on the same Wi-Fi can see it by visiting the Pi's IP address.
   > **New skill:** Running a basic web server in Python. This is how real web services work — your Pi becomes a tiny server and any browser on the same network can connect to it!

5. **Custom boot screen:** Make the startup screen display differently each time using the AI — ask Ollama to generate a spooky one-liner intro message.
   > **New skill:** Using AI output to control the UI, so the program feels alive and different every single time it starts up.
