# REPLACES signal() with perfect HTML <pre> formatting
import re

def fix_signal_block(path="avalon_bot.py"):
    txt = open(path).read()

    # Remove old signal()
    txt = re.sub(r"def signal\(.*?return .*?```", "", txt, flags=re.S)

    # Append clean new function
    new = """
def signal(uid):
    b = bal(uid)
    if b < MIN_BR:
        return f"⚠️ Bankroll too low.\\nMin: ${MIN_BR}\\nCurrent: ${b:.2f}\\nUse /br250"

    m = member(uid)
    if not m or m['status'] not in ('trial','active'):
        return "ℹ️ No membership.\\nUse /trial."

    # Build table rows
    rows = []
    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        side = "HOLD"
        rows.append(f"{c:<7} {p:<12.4f} {side:<6} ${stake:.2f}")

    body = "\\n".join(rows)

    return (
        "<pre>"
        "🔥 TODAY'S SIGNAL\\n\\n"
        f"Bankroll: ${b:.2f}\\n\\n"
        "COIN     PRICE         SIDE    STAKE\\n"
        "----------------------------------------\\n"
        f"{body}\\n\\n"
        "⚠️ Educational only — not financial advice."
        "</pre>"
    )
"""
    txt += new
    open(path, "w").write(txt)
    print("✔ signal() replaced cleanly")

fix_signal_block()
