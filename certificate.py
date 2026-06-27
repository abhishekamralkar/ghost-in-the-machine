"""
Summer 2026 Certificate of Completion Generator
Run this after finishing all modules and exercises!
"""

import datetime
import os
import random
import webbrowser

# ── Badge definitions ──────────────────────────────────────────────────────────

BADGES = [
    ("00", "Know Your Machine",  "🖥️",  "CPU, RAM, Storage & How Computers Work"),
    ("01", "Terminal Ninja",     "🐧",  "Linux, The Terminal & Shell Scripts"),
    ("02", "Open Source Hero",   "🌍",  "Git, GitHub, Branches & Pull Requests"),
    ("03", "Code Wizard",        "🐍",  "Python Programming & Games"),
    ("04", "AI Whisperer",       "🤖",  "Running & Controlling Local AI"),
    ("05", "Robot Builder",      "💀",  "Raspberry Pi, OLED Display & Hardware"),
]

# ── Messages ──────────────────────────────────────────────────────────────────

MESSAGES_ALL = [
    (
        "You started this summer not knowing what a terminal was.",
        "Now you wire up computers, boss around AIs, and push code to the internet.",
        "That is not normal for a kid your age. That is extraordinary."
    ),
    (
        "Most grown-ups have never done what you just did.",
        "You built real hardware, wrote real code, and shipped it.",
        "The world needs more people like you — keep going."
    ),
    (
        "Every expert was once a beginner who refused to quit.",
        "This summer you proved you are exactly that kind of person.",
        "The next thing you build will be even cooler. We can't wait to see it."
    ),
    (
        "Linux. Git. Python. AI. Raspberry Pi. Hardware. APIs.",
        "In one summer. At your age.",
        "That is genuinely impressive — brag about it, because you earned it."
    ),
    (
        "You didn't just learn to code. You learned how to learn.",
        "That skill will carry you further than any single language or tool.",
        "Now go build something that doesn't exist yet."
    ),
]

MESSAGES_PARTIAL = [
    (
        "Every module you finished is a real skill you actually have now.",
        "Not pretend-skill. Not 'I watched a video once' skill. Real skill.",
        "Come back for the rest whenever you're ready — it'll still be here."
    ),
    (
        "You did more this summer than most kids your age will ever try.",
        "Each badge represents hours of real work and real thinking.",
        "That counts. A lot."
    ),
    (
        "The modules you completed are already more than most adults know.",
        "Pick up the rest when you're ready — the hard part is starting, and you already did that.",
        "Be proud of what you've built."
    ),
]

def pick_message(all_done):
    pool = MESSAGES_ALL if all_done else MESSAGES_PARTIAL
    return random.choice(pool)

# ── Terminal helpers ───────────────────────────────────────────────────────────

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def print_banner():
    print("""
  ██████╗███████╗██████╗ ████████╗██╗███████╗██╗ ██████╗ █████╗ ████████╗███████╗
 ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
 ██║     █████╗  ██████╔╝   ██║   ██║█████╗  ██║██║     ███████║   ██║   █████╗
 ██║     ██╔══╝  ██╔══██╗   ██║   ██║██╔══╝  ██║██║     ██╔══██║   ██║   ██╔══╝
 ╚██████╗███████╗██║  ██║   ██║   ██║██║     ██║╚██████╗██║  ██║   ██║   ███████╗
  ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

               ★  CERTIFICATE OF COMPLETION GENERATOR  ★
    """)

def print_ascii_certificate(name, date_str, earned_badges, message):
    width = 70
    border = "═" * (width - 2)

    print()
    print("╔" + border + "╗")
    print("║" + " " * (width - 2) + "║")
    print("║" + "★  CERTIFICATE OF COMPLETION  ★".center(width - 2) + "║")
    print("║" + "Summer 2026 Coding Internship".center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("╠" + border + "╣")
    print("║" + " " * (width - 2) + "║")
    print("║" + "This certifies that".center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("║" + name.upper().center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("║" + "has successfully completed all modules of the".center(width - 2) + "║")
    print("║" + "Kids Summer Coding Internship 2026".center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("╠" + border + "╣")
    print("║" + " " * (width - 2) + "║")
    print("║" + "BADGES EARNED:".center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    for num, title, emoji, desc in earned_badges:
        badge_line = f"  {emoji}  Module {num}: {title}"
        print("║" + badge_line.ljust(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("╠" + border + "╣")
    print("║" + " " * (width - 2) + "║")
    for line in message:
        print("║" + line.center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("╠" + border + "╣")
    print("║" + " " * (width - 2) + "║")
    print("║" + f"Completed: {date_str}".center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("╚" + border + "╝")
    print()

# ── HTML certificate ───────────────────────────────────────────────────────────

def generate_html(name, date_str, earned_badges, total_badges, message):
    all_done = len(earned_badges) == total_badges
    grand_champion = "⭐ Grand Champion — All Modules Completed!" if all_done else ""
    message_lines = "".join(f"<p>{line}</p>" for line in message)

    badge_rows = ""
    for num, title, emoji, desc in earned_badges:
        badge_rows += f"""
        <div class="badge">
          <span class="badge-emoji">{emoji}</span>
          <div class="badge-info">
            <strong>Module {num}: {title}</strong>
            <span>{desc}</span>
          </div>
        </div>"""

    champion_block = ""
    if all_done:
        champion_block = """
        <div class="champion">
          ⭐ Grand Champion — All Modules Completed! ⭐
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Certificate of Completion — {name}</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Lato:wght@300;400;700&display=swap');

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background: #1a1a2e;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 40px 20px;
      font-family: 'Lato', sans-serif;
    }}

    .page {{
      background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #0f3460 100%);
      border: 3px solid #e2b84b;
      border-radius: 8px;
      max-width: 800px;
      width: 100%;
      padding: 60px 70px;
      position: relative;
      box-shadow: 0 0 60px rgba(226, 184, 75, 0.3), inset 0 0 60px rgba(0,0,0,0.3);
    }}

    /* Corner decorations */
    .page::before, .page::after {{
      content: '✦';
      position: absolute;
      font-size: 2rem;
      color: #e2b84b;
    }}
    .page::before {{ top: 16px; left: 20px; }}
    .page::after  {{ bottom: 16px; right: 20px; }}
    .corner-br::before {{ content: '✦'; position: absolute; bottom: 16px; left: 20px; font-size: 2rem; color: #e2b84b; }}
    .corner-tr::before {{ content: '✦'; position: absolute; top: 16px; right: 20px; font-size: 2rem; color: #e2b84b; }}

    /* Inner border */
    .inner {{
      border: 1px solid rgba(226, 184, 75, 0.4);
      border-radius: 4px;
      padding: 40px 50px;
    }}

    .header-line {{
      text-align: center;
      font-size: 0.75rem;
      letter-spacing: 6px;
      text-transform: uppercase;
      color: #e2b84b;
      margin-bottom: 12px;
    }}

    .title {{
      font-family: 'Cinzel', serif;
      font-size: 2.6rem;
      font-weight: 900;
      color: #e2b84b;
      text-align: center;
      line-height: 1.2;
      text-shadow: 0 0 30px rgba(226, 184, 75, 0.5);
    }}

    .subtitle {{
      font-family: 'Cinzel', serif;
      font-size: 1rem;
      color: rgba(226, 184, 75, 0.7);
      text-align: center;
      letter-spacing: 3px;
      margin-top: 6px;
    }}

    .divider {{
      border: none;
      border-top: 1px solid rgba(226, 184, 75, 0.4);
      margin: 28px 0;
    }}

    .certifies {{
      text-align: center;
      color: #a0b4c8;
      font-size: 0.95rem;
      font-style: italic;
      margin-bottom: 10px;
    }}

    .recipient {{
      font-family: 'Cinzel', serif;
      font-size: 2.4rem;
      font-weight: 700;
      color: #ffffff;
      text-align: center;
      text-shadow: 0 0 20px rgba(255,255,255,0.3);
      margin: 6px 0 10px;
    }}

    .description {{
      text-align: center;
      color: #a0b4c8;
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    .badges-title {{
      font-family: 'Cinzel', serif;
      font-size: 0.85rem;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: #e2b84b;
      text-align: center;
      margin: 28px 0 16px;
    }}

    .badges {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }}

    .badge {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(226, 184, 75, 0.2);
      border-radius: 6px;
      padding: 10px 14px;
    }}

    .badge-emoji {{ font-size: 1.5rem; flex-shrink: 0; }}

    .badge-info {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .badge-info strong {{
      color: #e2e2e2;
      font-size: 0.82rem;
    }}

    .badge-info span {{
      color: #6a8099;
      font-size: 0.72rem;
    }}

    .champion {{
      text-align: center;
      font-family: 'Cinzel', serif;
      font-size: 1rem;
      font-weight: 700;
      color: #e2b84b;
      background: rgba(226, 184, 75, 0.08);
      border: 1px solid rgba(226, 184, 75, 0.4);
      border-radius: 6px;
      padding: 12px;
      margin-top: 20px;
      text-shadow: 0 0 20px rgba(226, 184, 75, 0.6);
    }}

    .footer {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-top: 36px;
    }}

    .footer-block {{
      text-align: center;
    }}

    .footer-label {{
      color: #6a8099;
      font-size: 0.7rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-top: 6px;
    }}

    .footer-value {{
      color: #a0b4c8;
      font-size: 0.9rem;
      border-bottom: 1px solid rgba(226, 184, 75, 0.4);
      padding-bottom: 4px;
      min-width: 160px;
    }}

    .seal {{
      font-size: 3.5rem;
      text-align: center;
      line-height: 1;
    }}

    .message {{
      margin-top: 24px;
      padding: 20px 24px;
      background: rgba(255, 255, 255, 0.03);
      border-left: 3px solid #e2b84b;
      border-radius: 0 6px 6px 0;
    }}

    .message p {{
      color: #c0d0df;
      font-size: 0.88rem;
      line-height: 1.75;
      margin: 0;
    }}

    .message p + p {{
      margin-top: 6px;
    }}

    .message p:last-child {{
      color: #e2b84b;
      font-style: italic;
      font-weight: 700;
      margin-top: 10px;
    }}

    .quote {{
      text-align: center;
      color: #4a6070;
      font-size: 0.78rem;
      font-style: italic;
      margin-top: 24px;
      letter-spacing: 1px;
    }}

    @media print {{
      body {{ background: white; padding: 0; }}
      .page {{
        box-shadow: none;
        border-color: #b8942a;
        background: white;
        max-width: 100%;
      }}
      .title, .subtitle, .badges-title, .champion, .footer-label {{ color: #b8942a !important; }}
      .message {{ border-left-color: #b8942a; background: #f5f0e8; }}
      .message p {{ color: #333 !important; }}
      .message p:last-child {{ color: #b8942a !important; }}
      .recipient {{ color: #1a1a2e !important; text-shadow: none; }}
      .description, .certifies {{ color: #444 !important; }}
      .badge-info strong {{ color: #222 !important; }}
      .badge-info span {{ color: #666 !important; }}
      .footer-value {{ color: #333 !important; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="corner-br"></div>
    <div class="corner-tr"></div>
    <div class="inner">

      <p class="header-line">Kids Summer Coding Internship &nbsp;·&nbsp; 2026</p>
      <h1 class="title">Certificate of Completion</h1>
      <p class="subtitle">Ghost in the Machine</p>

      <hr class="divider">

      <p class="certifies">This certifies that</p>
      <p class="recipient">{name}</p>
      <p class="description">
        has successfully completed all modules of the<br>
        <strong style="color:#c8d8e8;">Kids Summer Coding Internship 2026</strong><br>
        demonstrating mastery of Linux, Git, Python, AI, and Raspberry Pi hardware.
      </p>

      <p class="badges-title">Badges Earned</p>
      <div class="badges">{badge_rows}
      </div>
      {champion_block}

      <div class="message">{message_lines}</div>

      <hr class="divider">

      <div class="footer">
        <div class="footer-block">
          <div class="footer-value">{date_str}</div>
          <div class="footer-label">Date Completed</div>
        </div>
        <div class="seal">🏆</div>
        <div class="footer-block">
          <div class="footer-value" style="min-width:180px;">&nbsp;</div>
          <div class="footer-label">Signed by My Awesome Parent</div>
        </div>
      </div>

      <p class="quote">
        "Keep building. Keep breaking things. Keep learning."
      </p>

    </div>
  </div>
</body>
</html>"""
    return html

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    clear()
    print_banner()

    print("  Answer a few questions and your certificate will be ready!\n")

    # Get name
    while True:
        name = input("  What is your name? ").strip()
        if name:
            break
        print("  (Please enter your name!)")

    print()

    # Ask which badges were earned
    print("  Which modules did you complete? (press Enter to skip any)\n")
    earned = []
    for num, title, emoji, desc in BADGES:
        answer = input(f"  {emoji}  Module {num}: {title}? [Y/n] ").strip().lower()
        if answer != "n":
            earned.append((num, title, emoji, desc))

    if not earned:
        print("\n  No badges selected — come back when you've finished at least one module!")
        return

    print()

    # Completion date
    today = datetime.date.today().strftime("%B %d, %Y")
    date_input = input(f"  Completion date? (press Enter for today: {today}) ").strip()
    date_str = date_input if date_input else today

    # Pick message
    all_done = len(earned) == len(BADGES)
    message = pick_message(all_done)

    # Print ASCII preview
    clear()
    print_banner()
    print_ascii_certificate(name, date_str, earned, message)

    # Generate HTML
    html = generate_html(name, date_str, earned, len(BADGES), message)
    safe_name = name.replace(" ", "_").lower()
    filename = f"certificate_{safe_name}.html"
    filepath = os.path.abspath(filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  Certificate saved to: {filepath}")
    print()

    # Try to open in browser
    try:
        webbrowser.open(f"file://{filepath}")
        print("  Opening in your browser... use Ctrl+P to print or save as PDF!")
    except Exception:
        print(f"  Open this file in your browser: {filepath}")

    print()
    print("  " + "★" * 34)
    print(f"  Congratulations, {name}! You did it! 🎉")
    print("  " + "★" * 34)
    print()

if __name__ == "__main__":
    main()
