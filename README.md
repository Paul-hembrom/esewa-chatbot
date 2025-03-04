# ESEWA-CHATBOT
A Flask-based chatbot for eSewa services in Nepal, running on HTTPS with Mistral LLM via Ollama.

## Features
- Chat interface for eSewa queries (Topup & Recharge, etc.).
- HTTPS support with self-signed certs.
- Built solo by Paulus Hembrom (@SoloBot Crew).

## Setup
1. Install dependencies: `pip install flask langchain-ollama`
2. Run Ollama: `ollama run mistral`
3. Run: `python chat.py`
4. Access: `https://localhost:5000`
