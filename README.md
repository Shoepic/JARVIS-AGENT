# Jarvis Local Assistant

## 🧠 What It Is
A personal AI assistant powered by Mistral 7B, running locally via Ollama and integrated with LangChain + tools.

## 🚀 How to Run

1. Clone or extract this folder
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Start the assistant:

```
python start_assistant.py
```

4. Open your browser to:
```
http://localhost:8000
```

To use the chat UI:
```
file://<your-path>/frontend/index.html
```

Make sure Ollama is running and has `mistral` model pulled:

```
ollama run mistral
```
