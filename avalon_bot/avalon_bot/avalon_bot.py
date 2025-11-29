#!/usr/bin/env python3
import json, time, datetime as dt, requests
from telebot import TeleBot

TOKEN="8336621797:AAHwe950NzES4ZNJkFzPBdyytYhJwxuX70w"
CHAT="-1003346097255"

MIN_BR = 250
TRIAL_DAYS = 7

BALFILE="balances.json"
MEMFILE="members.json"

COINS=["BTC","ETH","DOGE","SOL","XRP","LTC","AVAX"]
PCT={"BTC":0.20,"ETH":0.20,"DOGE":0.10,"SOL":0.15,"XRP":0.10,"LTC":0.10,"AVAX":0.15}

bot = TeleBot(TOKEN, parse_mode="HTML")

def load(p,d):
    try: return json.load(open(p))
    except: return d

def save(p,d):
    json.dump(d,open(p,"w"))

BAL = load(BALFILE,{})
MEM = load(MEMFILE,{})

def bal(uid): return float(BAL.get(str(uid),0))
def set_bal(uid,a): BAL[str(uid)] = float(a); save(BALFILE,BAL)

def member(uid):
    uid=str(uid)
    m=MEM.get(uid)
    if not m: return None
    if m["expires"] < time.time():
        m["status"]="expired"; save(MEMFILE,MEM)
    return m

def set_member(uid,status,days):
    now=time.time()
    MEM[str(uid)]={"status":status,"started":now,"expires":now+days*86400}
    save(MEMFILE,MEM)

def price(c):
    r=requests.get("https://api.binance.com/api/v3/ticker/price",
                   params={"symbol":f"{c}USDT"},timeout=10)
    return float(r.json()["price"])

def signal(uid):
    b = bal(uid)
    if b < MIN_BR:
        return f"⚠️ Bankroll too low.<br>Min: ${MIN_BR}<br>Current: ${b:.2f}<br>Use /br250"

    m = member(uid)
    if not m or m["status"] not in ("trial","active"):
        return "ℹ️ No membership.<br>Use /trial."

    rows = []
    for c in COINS:
        p = price(c)
        stake = b * PCT[c]
        side = "HOLD"
        rows.append(f"{c:<7} {p:<12.4f} {side:<5} ${stake:.2f}")

    body = "\n".join(rows)

    return (
        "<pre>"
        "🔥 TODAY'S SIGNAL\n\n"
        f"Bankroll: ${b:.2f}\n\n"
        "COIN     PRICE         SIDE    STAKE\n"
        "----------------------------------------\n"
        f"{body}\n\n"
        "⚠️ Educational only — not financial advice."
        "</pre>"
    )

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,
    f"👋 Welcome to Avalon\n\n"
    f"Minimum bankroll: ${MIN_BR}\n"
    f"Free Trial: {TRIAL_DAYS} days\n\n"
    "/trial – start trial\n"
    "/status – membership status\n"
    "/br250 – set bankroll\n"
    "/signal – get signal")

@bot.message_handler(commands=['trial'])
def trial(m):
    uid = m.from_user.id
    if member(uid):
        return bot.send_message(m.chat.id,"Already active.")
    set_member(uid, "trial", TRIAL_DAYS)
    bot.send_message(m.chat.id, f"🧪 Trial started. {TRIAL_DAYS} days active.")

@bot.message_handler(commands=['status'])
def status(m):
    me = member(m.from_user.id)
    if not me:
        return bot.send_message(m.chat.id,"No membership.")
    exp = dt.datetime.utcfromtimestamp(me["expires"]).strftime("%Y-%m-%d %H:%M UTC")
    bot.send_message(m.chat.id,f"Status: {me['status']}\nExpires: {exp}")

@bot.message_handler(func=lambda x: x.text and x.text.startswith("/br"))
def br(m):
    try: amt=float(m.text.replace("/br",""))
    except: return bot.send_message(m.chat.id,"Use: /br250")
    if amt < MIN_BR:
        return bot.send_message(m.chat.id,f"Min bankroll is ${MIN_BR}.")
    set_bal(m.from_user.id,amt)
    bot.send_message(m.chat.id,f"Bankroll set: ${amt:.2f}")

@bot.message_handler(commands=['signal'])
def sig(m):
    bot.send_message(m.chat.id, signal(m.from_user.id))

print("Avalon bot running...")
bot.infinity_polling()
