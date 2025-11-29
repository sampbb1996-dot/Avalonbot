#!/usr/bin/env python3
import json, time, requests
from telebot import TeleBot

TOKEN="8336621797:AAHwe950NzES4ZNJkFzPBdyytYhJwxuX70w"
CHAT="-1003346097255"

MIN_BR=250
TRIAL_DAYS=7

COINS=["BTC","ETH","DOGE","SOL","XRP","LTC","AVAX"]
PCT={"BTC":0.20,"ETH":0.20,"DOGE":0.10,"SOL":0.15,"XRP":0.10,"LTC":0.10,"AVAX":0.15}

BALFILE="balances.json"
MEMFILE="members.json"

bot=TeleBot(TOKEN,parse_mode="HTML")

def load(p, d):
    try: return json.load(open(p))
    except: return d

def save(p, d):
    json.dump(d, open(p, "w"))

BAL = load(BALFILE, {})
MEM = load(MEMFILE, {})

def bal(uid):
    return float(BAL.get(str(uid), 0))

def set_bal(uid, amt):
    BAL[str(uid)] = float(amt)
    save(BALFILE, BAL)

def member(uid):
    uid=str(uid)
    m=MEM.get(uid)
    if not m: return None
    if m["expires"] < time.time():
        m["status"] = "expired"
        save(MEMFILE, MEM)
    return m

def set_member(uid, status, days):
    now=time.time()
    MEM[str(uid)] = {
        "status":status,
        "started":now,
        "expires":now + days*86400
    }
    save(MEMFILE, MEM)

def price(c):
    r = requests.get(
        "https://api.binance.com/api/v3/ticker/price",
        params={"symbol":f"{c}USDT"}, timeout=10
    )
    return float(r.json()["price"])



    m = member(uid)
    if not m or m["status"] not in ("trial","active"):
        return "ℹ️ No membership.\nUse /trial."

    out = []
    out.append("```")
    out.append("🔥 TODAY'S SIGNAL")
    out.append("")
    out.append(f"Bankroll: ${b:.2f}")
    out.append("")
    out.append("COIN     PRICE         SIDE     STAKE")
    out.append("----------------------------------------")

    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        side = "HOLD"
        out.append(f"{c:<7} {p:<12.4f} {side:<7} ${stake:.2f}")

    out.append("")
    out.append("⚠️ Educational only — not financial advice.")
    out.append("```")
    return "\n".join(out)


            f"⚠️ Bankroll too low.\n"
            f"Min: ${MIN_BR}\n"
            f"Current: ${b:.2f}\n"
            f"Use /br250 to set bankroll."
        )

    m = member(uid)
    if not m or m["status"] not in ("trial", "active"):
        return "ℹ️ No membership.\nUse /trial to begin your free trial."

    out = []
    out.append("```")
    out.append("🔥 TODAY'S SIGNAL")
    out.append("")
    out.append(f"Bankroll: ${b:.2f}")
    out.append("")
    out.append("COIN     PRICE         SIDE     STAKE")
    out.append("----------------------------------------")

    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        out.append(f"{c:<7} {p:<12.4f}  HOLD    ${stake:.2f}")

    out.append("")
    out.append("⚠️ Educational only — not financial advice.")
    out.append("```")

    return "\n".join(out)


            f"⚠️ Bankroll too low.\n"
            f"Min: ${MIN_BR}\n"
            f"Current: ${b:.2f}\n"
            f"Use /br250 to set bankroll."
        )

    m = member(uid)
    if not m or m["status"] not in ("trial", "active"):
        return "ℹ️ No membership.\nUse /trial to begin your free trial."

    out = []
    out.append("```")
    out.append("🔥 TODAY'S SIGNAL")
    out.append("")
    out.append(f"Bankroll: ${b:.2f}")
    out.append("")
    out.append("COIN     PRICE         SIDE     STAKE")
    out.append("----------------------------------------")

    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        out.append(f"{c:<7} {p:<12.4f}  HOLD    ${stake:.2f}")

    out.append("")
    out.append("⚠️ Educational only — not financial advice.")
    out.append("```")

    return "\n".join(out)


def signal(uid):
    b = bal(uid)
    if b < MIN_BR:
        return f"⚠️ Bankroll too low.\nMin: ${MIN_BR}\nCurrent: ${b:.2f}\nUse /br250"

    m = member(uid)
    if not m or m["status"] not in ("trial","active"):
        return "ℹ️ No membership.\nUse /trial."

    out = []
    out.append("```")
    out.append("🔥 TODAY'S SIGNAL")
    out.append("")
    out.append(f"Bankroll: ${b:.2f}")
    out.append("")
    out.append("COIN     PRICE         SIDE     STAKE")
    out.append("----------------------------------------")

    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        out.append(f"{c:<7} {p:<12.4f} HOLD     ${stake:.2f}")

    out.append("⚠️ Educational only — not financial advice.")
    out.append("```")

    return "\n".join(out)