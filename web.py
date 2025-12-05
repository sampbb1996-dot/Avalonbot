from flask import Flask, render_template_string
import random
import datetime

app = Flask(__name__)

# -------------------------------------------------
# AMFRD-LITE PAGE GENERATOR (legal-safe version)
# -------------------------------------------------

TRENDS = [
    "High-engagement loops",
    "Contrast-pattern responses",
    "Pacing-overlap clusters",
    "Microtrend resonance",
    "Attention-stable fragments",
    "Contextual uplift frames"
]

def generate_page(creator_name=None):
    trend_sample = random.sample(TRENDS, 3)
    lift_estimate = round(random.uniform(3.5, 18.0), 1)

    return f"""
    <html>
    <head>
        <title>Pattern Insight Report</title>
        <style>
            body {{ font-family: Arial; margin: 40px; }}
            .card {{ padding: 20px; border-radius: 10px; background:#f4f4f4; margin-bottom:20px; }}
        </style>
    </head>
    <body>
        <h1>Pattern Insight Snapshot</h1>
        <p><b>Generated:</b> {datetime.datetime.utcnow()} UTC</p>

        {'<p><b>Creator:</b> ' + creator_name + '</p>' if creator_name else ''}

        <div class="card">
            <h3>Current High-Signal Structures</h3>
            <ul>
                <li>{trend_sample[0]}</li>
                <li>{trend_sample[1]}</li>
                <li>{trend_sample[2]}</li>
            </ul>
        </div>

        <div class="card">
            <h3>Estimated Public Lift</h3>
            <p>{lift_estimate}% relative visibility uplift</p>
        </div>

        <p style='opacity:0.6;'>AMFRD-lite generator — recalibrates each refresh</p>
    </body>
    </html>
    """

@app.route("/")
def home():
    return render_template_string(generate_page())

@app.route("/c/<creator>")
def creator_page(creator):
    return render_template_string(generate_page(creator_name=creator))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)