# -------------------------------------------------------
# AMFRD ENGINE — SINGLE FILE VERSION
# -------------------------------------------------------

import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

# -------------------------------------------------------
# INTERNAL AMFRD STATE
# -------------------------------------------------------

AMFRD_STATE = {
    "current_patterns": [],
    "last_update": time.time()
}

# -------------------------------------------------------
# PATTERN GENERATOR (SIMPLIFIED)
# -------------------------------------------------------

def generate_patterns():
    """Generate abstract 'influence structures' without using names."""
    base_shapes = [
        "Ascending Micro-Loop",
        "Folded Attention Curve",
        "Tri-Vector Pull",
        "Phase-Shifting Cluster",
        "Nested Drift Window",
        "Echo-Weighted Step",
        "Soft Symmetry Pair",
        "Adaptive Pulse Layer"
    ]

    patterns = random.sample(base_shapes, 3)
    weights = [round(random.uniform(0.2, 1.0), 2) for _ in range(3)]

    return [{"pattern": p, "weight": w} for p, w in zip(patterns, weights)]

# -------------------------------------------------------
# ENGINE REFRESH
# -------------------------------------------------------

def refresh_engine():
    """AMFRD updates its internal 'world model' every few seconds."""
    AMFRD_STATE["current_patterns"] = generate_patterns()
    AMFRD_STATE["last_update"] = time.time()

refresh_engine()

# -------------------------------------------------------
# GET CURRENT AMFRD SNAPSHOT
# -------------------------------------------------------

def get_snapshot():
    """Return clean public-safe snapshot of AMFRD internal state."""
    now = time.time()
    age = now - AMFRD_STATE["last_update"]

    # Auto refresh if older than 10 seconds
    if age > 10:
        refresh_engine()

    return {
        "status": "ok",
        "last_update": AMFRD_STATE["last_update"],
        "patterns": AMFRD_STATE["current_patterns"],
        "cycle_age_seconds": round(age, 2)
    }

# -------------------------------------------------------
# FLASK ROUTES
# -------------------------------------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "AMFRD Influence Engine Running",
        "instructions": "Visit /snapshot to view current model patterns."
    })

@app.route("/snapshot")
def snapshot():
    return jsonify(get_snapshot())

# -------------------------------------------------------
# FLASK LAUNCHER — INCLUDED DIRECTLY IN THIS FILE
# -------------------------------------------------------

if __name__ == "__main__":
    # Runs the server when you do: python3 amfrd.py
    app.run(host="0.0.0.0", port=5000)