# 🤖 AI Chatbot using Rasa

## 📌 Description

This project is an AI-based chatbot built using the Rasa framework.
It can understand user queries using Natural Language Processing (NLP) and respond intelligently based on defined intents and rules.

---

## 🚀 Features

* 💬 Handles basic conversations (greetings, goodbye, etc.)
* 🌦️ Provides weather-related responses
* 🔐 Supports password reset queries
* 🤖 Identifies whether the user is talking to a bot
* 🧠 Uses NLP for intent recognition

---

## 🛠️ Tech Stack

* Python 🐍
* Rasa (Conversational AI Framework)
* NLP (Natural Language Processing)

---

## 📂 Project Structure

```
chatbot-using-rasa/
│── actions/
│── data/
│   ├── nlu.yml
│   ├── stories.yml
│   ├── rules.yml
│── domain.yml
│── config.yml
│── endpoints.yml
│── credentials.yml
│── README.md
```

---

## ▶️ How to Run the Project

### 1. Install dependencies

```bash
pip install rasa
```

### 2. Train the model

```bash
rasa train
```

### 3. Run chatbot

```bash
rasa shell
```

### 4. Run action server (if using custom actions)

```bash
rasa run actions
```

---

## 📸 Example Use Cases

* User: "Hi" → Bot: "Hello 👋"
* User: "What's the weather?" → Bot: "Weather is sunny ☀️"
* User: "Reset my password" → Bot: "Password reset link sent 🔐"

---

## 👤 Author

**Mukund Lokhande**

---

## ⭐ Future Improvements

* Add API integration (real-time weather)
* Deploy chatbot on web interface
* Improve NLP accuracy with more training data

---

## 📌 Note

The `models/` folder is not included as it contains large files.
You can generate models using `rasa train`.

---
