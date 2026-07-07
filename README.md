# 🔬 Prompt Playground Lab

A Python-based playground for experimenting with Large Language Models (LLMs), studying prompt behavior, and evaluating responses through the OpenRouter API.

This project was built as part of my **AI Security Bootcamp** to better understand how LLMs process prompts before moving into topics such as RAG, AI Agents, Prompt Injection, and AI Guardrails.

---

# ✨ Features

* 💬 Interactive chat with an LLM
* ⚙️ Custom System Prompt support
* 🧠 Conversation history management
* 🗑️ Clear conversation history
* 📖 Display conversation history
* 📊 Context statistics

  * User message count
  * Assistant message count
  * Context length
* 🤖 Reasoning mode toggle (supported models)
* 🧪 Automated prompt testing using JSON test cases
* 💾 Save experiment results to JSON
* 📈 Token usage monitoring

  * Prompt Tokens
  * Completion Tokens
  * Total Tokens
* ❌ Error handling for common API failures

---

# 📂 Project Structure

```text
Prompt-Playground-Lab/
│
├── experiments/
├── docs/
|     └── note.md
├── main.py
├── test_case.json
├── test_result.json
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/eforiea/Prompt-Playground-Lab.git
cd Prompt-Playground-Lab
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=your_openrouter_api_key
```

Run the project:

```bash
python main.py
```

---

# 📋 Menu

```text
PROMPT PLAYGROUND LAB

1 - Start Chat
2 - Set System Prompt
3 - Show History
4 - Prompt Test
5 - Context Info
6 - Toggle Reasoning
0 - Exit
```

---

# 🧪 Prompt Testing

The project supports automated prompt evaluation.

Create test cases inside:

```text
test_case.json
```

Each test case contains a system prompt and a user prompt.

The application automatically:

* Sends all test cases
* Collects responses
* Saves the results to

```text
test_result.json
```

This makes it easy to compare model behavior across different prompts and models.

---

# 📊 Context Information

The playground can display useful conversation statistics:

* Number of user messages
* Number of assistant messages
* Approximate context length

This helps visualize how conversation history grows over time.

---

# 🎯 Learning Objectives

This project explores fundamental LLM concepts, including:

* System Prompt
* User Prompt
* Prompt Hierarchy
* Conversation History
* Context Window
* Stateless LLMs
* Prompt Engineering
* Structured Output
* Few-shot Prompting
* Basic LLM Evaluation

# 📄 License

This project is intended for educational purposes as part of my AI Security learning journey.

---

# 👨‍💻 Author

Developed as part of a hands-on AI Security Bootcamp focused on practical learning, experimentation, and building a professional GitHub portfolio.
