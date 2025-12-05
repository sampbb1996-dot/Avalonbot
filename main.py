from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

# --- AMFRD Subtle Influence Engine (Lite Version) ---
patterns = [
    "Rising Attention Pattern",
    "Cross-Context Echo",
    "Soft Trend Convergence",
    "Micro-Pulse Engagement Lift",
    "Ambient Spotlight Drift",
    "Pattern Resonance Fit",
]

def generate_pattern():
    return random.choice(patterns)

def generate_lift():
    return round(random.uniform(1.5, 7.5), 2)

@app.route("/")
def index():
    return render_template(
        "index.html",
        today=datetime.date.today().strftime("%B %d, %Y"),
        pattern=generate_pattern(),
        lift=generate_lift()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)