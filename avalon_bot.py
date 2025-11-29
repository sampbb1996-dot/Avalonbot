#!/usr/bin/env python3
import json, time, datetime as dt, requests
from telebot import TeleBot

TOKEN="8336621797:AAHwe950NzES4ZNJkFzPBdyytYhJwxuX70w"
CHAT="-1003346097255"

MIN_BR=250
MEM_PRICE=20
TRIAL=7

BALFILE="balances.json"
MEMFILE="members.json"

COINS=["BTC","ETH","DOGE","SOL","XRP","LTC","AVAX"]
PCT={"BTC":.20,"ETH":.20,"DOGE":.10,"SOL":.15,"XRP":.10,"LTC":.10,"AVAX":.15}

bot=TeleBot(TOKEN,parse_mode="HTML")

def load(p,d):
    try: return json.load(open(p))
    except: return d

def save(p,d):
    json.dump(d,open(p,"w"))

BAL=load(BALFILE,{})
MEM=load(MEMFILE,{})

def bal(uid): return float(BAL.get(str(uid),0))
def set_bal(uid,a):
    BAL[str(uid)]=float(a); save(BALFILE,BAL)

def member(uid):
    uid=str(uid)
    m=MEM.get(uid)
    if not m: return None
    if m["expires"] < time.time():
        m["status"]="expired"; save(MEMFILE,MEM)
def signal(uid):
    b = bal(uid)
    if b < MIN_BR:
        return f"⚠️ Bankroll too low.\nMin: ${MIN_BR}\nCurrent: ${b:.2f}\nUse /br250"

    m = member(uid)
    if not m or m["status"] not in ("trial", "active"):
        return "ℹ️ No membership.\nUse /trial."

    header = (
        "```\n"
        "🔥 TODAY'S SIGNAL\n\n"
        f"Bankroll: ${b:.2f}\n\n"
        "COIN     PRICE         SIDE     STAKE\n"
        "----------------------------------------\n"
    )

    rows = []
    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        side = "HOLD"
        rows.append(f"{c:<7} {p:<12.4f} {side:<7} ${stake:.2f}")

    footer = "\n⚠️ Educational only — not financial advice.\n```"
    return header + "\n".join(rows) + footer


def signal(uid):
    b = bal(uid)
    if b < MIN_BR:
        return f"⚠️ Bankroll too low.\nMin: ${MIN_BR}\nCurrent: ${b:.2f}\nUse /br250"

    m = member(uid)
    if not m or m["status"] not in ("trial", "active"):
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
