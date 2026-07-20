from flask import Flask, render_template, request

app = Flask(__name__)

def detect_emergency(text):
    text = text.lower()

    if "pain" in text or "heart" in text or "chest" in text:
        return "🚑 Health Emergency! Call Ambulance: 108"

    elif "flood" in text or "earthquake" in text or "fire" in text:
        return "🌊 Disaster Alert! Move to a safe place immediately"

    elif "sad" in text or "stress" in text or "depressed" in text:
        return "🧠 Talk to someone you trust. You are not alone."

    else:
        return "ℹ️ Stay safe and monitor the situation"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form["message"]
        result = detect_emergency(user_input)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)