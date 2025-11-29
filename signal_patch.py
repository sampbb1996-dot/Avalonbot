from pathlib import Path

p = Path("avalon_bot.py")
code = p.read_text().splitlines()
out = []
skipping = False

for line in code:
    if line.strip().startswith("def signal("):
        skipping = True
        out.append("def signal(uid):")
        out.append("    b = bal(uid)")
        out.append("    if b < MIN_BR:")
        out.append('        return f"⚠️ Bankroll too low.\\nMin: ${MIN_BR}\\nCurrent: ${b:.2f}\\nUse /br250"')
        out.append("")
        out.append("    m = member(uid)")
        out.append('    if not m or m["status"] not in ("trial","active"):')
        out.append('        return "ℹ️ No membership.\\nUse /trial."')
        out.append("")
        out.append("    out = []")
        out.append('    out.append("```")')
        out.append('    out.append("🔥 TODAY\'S SIGNAL")')
        out.append("    out.append(\"\")")
        out.append('    out.append(f"Bankroll: ${b:.2f}")')
        out.append("    out.append(\"\")")
        out.append('    out.append("COIN     PRICE         SIDE     STAKE")')
        out.append('    out.append("----------------------------------------")')
        out.append("")
        out.append("    for c in COINS:")
        out.append("        p = price(c)")
        out.append("        stake = b * PCT[c]")
        out.append('        out.append(f\"{c:<7} {p:<12.4f} HOLD     ${stake:.2f}\")')
        out.append("")
        out.append('    out.append("⚠️ Educational only — not financial advice.")')
        out.append('    out.append("```")')
        out.append("")
        out.append("    return \"\\n\".join(out)")
        continue

    if skipping:
        if line.strip() == "":
            continue
        # skip old signal() until blank
        if line.startswith("def ") and "signal" not in line:
            skipping = False

    if not skipping:
        out.append(line)

p.write_text("\n".join(out))
