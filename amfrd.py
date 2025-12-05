from flask import Flask, request
import random
import datetime

app = Flask(__name__)

# ---------------------------------------------
# AMFRD-LITE SUBTLE PATTERN ENGINE (SINGLE FILE)
# ---------------------------------------------
PATTERNS = [
    "Rising Micro-Cluster Activity",
    "Shift Toward Structured Motifs",
    "High-Signal Compression Window",
    "Emerging Parallel Pattern Streams",
    "Stability Pulse in Trend Layer",
    "Contextual Amplification Drifts",
    "Soft Resonance Alignment",
    "Incremental Spotlight Uptick",
]

def generate_pattern():
    return random.choice(PATTERNS)

def generate_lift():
    return round(random.uniform(2.5, 15.5), 1)

def generate_insight():
    return random.choice([
        "This pattern suggests increased compatibility with public-facing clusters.",
        "Alignment with trend structures may improve organic visibility.",
        "Signals indicate mild momentum buildup across attention pathways.",
        "Resonance layer stability implies favourable engagement windows.",
        "Pattern proximity reveals higher-than-average exposure potential.",
    ])

# ---------------------------------------------
# AUTO-GENERATED HTML (NO FOLDERS, NO FILES)
# ---------------------------------------------
def render_page(title, creator=None):
    pattern = generate_pattern()
    lift = generate_lift()
    insight = generate_insight()
    timestamp = datetime.datetime.utcnow().strftime("%B %d, %Y — %H:%M UTC")

    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                background:#0e0e0e;
                color:#e0e0e0;
                padding:20px;
            }}
            .card {{
                background:#1a1a1a;
                padding:20px;
                border-radius:12px;
                margin-bottom:20px;
                border:1px solid #333;
            }}
            h1 {{
                color:#9b6dff; 
                text-align:center;
            }}
            .highlight {{
                color:#7bffaa; 
                font-weight:bold;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h