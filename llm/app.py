import sys
import os

from flask import Flask, request, jsonify, render_template

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from llm.weather_insights import ask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    domanda = data.get("domanda", "").strip()

    if not domanda:
        return jsonify({"errore": "Domanda vuota"}), 400
    
    risposta = ask(domanda)

    return jsonify({
        "summary": risposta["summary"],
        "data": risposta["data"]
    })

if __name__ == "__main__":
    app.run(debug=True)

