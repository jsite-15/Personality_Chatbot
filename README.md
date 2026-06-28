# 🤖 AI Personality Chatbot

An AI-powered personality chatbot built using **Python**, **LangChain**, **Mistral AI**, and **Streamlit**. The chatbot engages users in natural, context-aware conversations while maintaining a consistent personality through prompt engineering.

## 🚀 Features

- 💬 Interactive conversational AI
- 🧠 Powered by Mistral Large Language Models
- 🎭 Consistent chatbot personality using system prompts
- 💭 Context-aware conversations with chat history
- ⚡ Fast and responsive Streamlit interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- python-dotenv

---

## 📂 Project Structure

```
Personality_Chatbot/
│── uichatbot.py          # Main Streamlit application
│── requirements.txt      # Project dependencies
│── README.md             # Documentation
│── .env                  # Environment variables (not included)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jsite-15/Personality_Chatbot.git
cd Personality_Chatbot
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

```env
MISTRAL_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Mistral API key.

---

## ▶️ Run the Application

Using Streamlit:

```bash
streamlit run uichatbot.py
```

or

```bash
python -m streamlit run uichatbot.py
```

or (using uv)

```bash
uv run streamlit run uichatbot.py
```

---

## 💡 How It Works

1. Loads the Mistral API key securely from the `.env` file.
2. Initializes the Mistral Large Language Model using LangChain.
3. Maintains conversation history for contextual responses.
4. Uses prompt engineering to preserve the chatbot's personality.
5. Displays an interactive chat interface through Streamlit.

---

## 📸 Demo

Add screenshots of the chatbot interface here.

Example:

```
images/chatbot.png
```

---

## 📦 Requirements

Main libraries used:

- streamlit
- langchain
- langchain-mistralai
- python-dotenv

See `requirements.txt` for the complete list.

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## 👩‍💻 Author

**Jasmine Singh**

GitHub: https://github.com/jsite-15
