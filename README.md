# AI-EMERGENCY-APP
# Emergency Message Detector

A simple Flask web app that scans a user-submitted message for keywords and returns a relevant safety alert — health emergency, natural disaster, or emotional distress.

## How it works

The app exposes a single route (`/`) that accepts a message via a form (POST) and runs it through a basic keyword-matching function:

| Keywords in message | Response |
|---|---|
| `pain`, `heart`, `chest` | 🚑 Health Emergency — Call Ambulance: 108 |
| `flood`, `earthquake`, `fire` | 🌊 Disaster Alert — Move to a safe place immediately |
| `sad`, `stress`, `depressed` | 🧠 Talk to someone you trust. You are not alone. |
| *(no match)* | ℹ️ Stay safe and monitor the situation |

## Requirements

- Python 3.x
- Flask

Install dependencies:

```bash
pip install flask
```

## Project structure

```
.
├── app.py
└── templates/
    └── index.html
```

> **Note:** This app expects a `templates/index.html` file with a form (`message` field, POST method) that displays the `result` variable. Make sure this file exists in your project before running the app.

## Running the app

```bash
python app.py
```

The app will start in debug mode at `http://127.0.0.1:5000/`.

## ⚠️ Disclaimer

This is a basic keyword-matching demo and **not a substitute for real emergency services or medical/mental health support**. It does not use any form of natural language understanding and can easily miss or misclassify messages. Do not rely on this app in an actual emergency — always contact local emergency services directly.

## License

Add a license of your choice (e.g., MIT) here.
