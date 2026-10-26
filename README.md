# 🤖 Gemini Chatbot

A simple AI chatbot built with **Streamlit** and the **Google Gemini API** that lets users interact with an LLM through a web interface.

This project demonstrates a local web-based AI assistant and is suitable as a demo, prototype, or learning project.

---

## Features

- Chat UI built with Streamlit
- Integration with the Google Gemini API
- Conversation history stored per session
- Local setup using a Python virtual environment

## Project Structure

```text
.
├── main.py                # Main Streamlit app
├── check_models.py        # List available Gemini models
├── requirements.txt       # Python dependencies
├── .env.example           # Template for local API-key configuration
└── .gitignore             # Excludes secrets and local environments
```

## Prerequisites

- Python 3.10 or newer
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/avviiiral/Gemini-Chatbot.git
   cd Gemini-Chatbot
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   On macOS/Linux, activate it with `source venv/bin/activate`.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a local `.env` file from the template:

   ```powershell
   Copy-Item .env.example .env
   ```

   On macOS/Linux, use `cp .env.example .env`. Edit `.env` and replace `YOUR_GOOGLE_API_KEY_HERE` with your actual key. Never commit `.env` or publish the key.

## Run

```bash
streamlit run main.py
```

Open `http://localhost:8501` in your browser.

## How It Works

1. The user enters a message in the Streamlit interface.
2. The application sends the message to a Gemini model through the Google Gen AI SDK.
3. The generated response is displayed in the chat interface.

## Troubleshooting

Run `python check_models.py` to inspect models available to your API key. Model availability can depend on the SDK version and API access.

## Security

Keep API keys in your local `.env` file. The `.env` file is ignored by Git; commit only the `.env.example` template.

## License

A license file is not currently included in this repository. Add a `LICENSE` file with your chosen license before redistributing or inviting reuse.
