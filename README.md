# 🤖 Gemini Chatbot

A simple AI chatbot built with **Streamlit** and **Google Gemini API** that lets users interact with a powerful LLM via a web interface.

This project demonstrates how to build a web-based AI assistant using Google’s Gemini models — perfect as a demo, prototype, or learning project.

---

## 🚀 Features

- 🗨️ Chat UI using **Streamlit**
- 🔑 Integration with **Google Gemini API**
- 📜 Conversation history stored per session
- 📦 Easy to set up and run locally

---

## 📁 Project Structure

```text
.
├── main.py                # Main Streamlit app
├── check_models.py        # List available Gemini models
├── requirements.txt       # Python dependencies
├── .env                   # Environment file (API key)
├── venv/                  # Python virtual environment
`
```
## 🛠️ Prerequisites

- Before running the app, install:

- Python 3.10+

- A Google Gemini API key

Get your API key from:
```
👉 https://aistudio.google.com/app/apikey
```

---

## 📦 Setup Instructions
1. Clone the repository
```
git clone https://github.com/avviiiral/Gemini-Chatbot.git
cd Gemini-Chatbot
```
2. Create & activate a Python virtual environment
```
python -m venv venv
.\venv\Scripts\activate        # Windows PowerShell
# OR
source venv/bin/activate       # macOS/Linux
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Add your API key

- Create a file named .env in the project root:
```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE
```

- Be sure to replace YOUR_GOOGLE_API_KEY_HERE with your real key.

---

## 📌 How to Run the App

- Start the app using Streamlit:
```
streamlit run main.py
```

- Then open the browser at:
```
http://localhost:8501
```

---

## 🧠 How It Works

The app uses the google-genai Python SDK to call Gemini models and generate replies:

- Users enter a message in the chat box

- The app sends the message to the Gemini API

- The API returns an AI-generated response

- The response is displayed in the Streamlit UI

---

## 🛡️ Notes

Your .env file must not be committed — include it in .gitignore

Model names must be compatible with your API key — check them with:
```
python check_models.py
```

---

## 📄 Example Code (Key snippet)
```
response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=user_input
)
```

---

## 📜 License

This project is open-source — feel free to use and modify!


---


