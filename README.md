# 🧮 LangChain MCP Calculator AI Agent

An AI-powered calculator that understands natural-language requests and performs arithmetic using **LangChain, Groq LLMs, and the Model Context Protocol (MCP)**.

Instead of entering mathematical expressions like `4 * 6`, you can ask questions such as:

- "Please multiply 4 by 6."
- "What is 25 times 8?"
- "Can you divide 100 by 4?"
- "Subtract 17 from 50."

The AI agent interprets the request, selects the appropriate calculator tool, executes the calculation through an MCP server, and returns a clear answer.

## 🚀 Features

- **Natural Language Understanding:** Understands mathematical requests written in everyday English.
- **AI Agent:** Uses LangChain to connect the language model with calculator tools.
- **MCP Integration:** Exposes calculator functions through a Model Context Protocol server.
- **Four Calculator Tools:** Supports addition, subtraction, multiplication, and division.
- **Groq LLM Integration:** Uses `openai/gpt-oss-120b` through Groq for language understanding and tool selection.
- **Interactive CLI:** Accepts multiple calculations in a single session.
- **Error Handling:** Handles runtime errors and division by zero.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Agent creation and tool orchestration |
| LangGraph | Agent execution infrastructure |
| Groq | LLM inference |
| GPT-OSS 120B | Natural-language understanding and tool selection |
| Model Context Protocol (MCP) | Communication between the AI client and calculator server |
| `langchain-mcp-adapters` | Integrates MCP tools with LangChain |
| `python-dotenv` | Loads environment variables from `.env` |

## 🏗️ Architecture

```text
                 User
                   |
                   v
       Natural-Language Request
                   |
                   v
           LangChain Agent
                   |
                   v
               Groq LLM
                   |
          Selects Calculator Tool
                   |
                   v
              MCP Client
                   |
             stdio Transport
                   |
                   v
              MCP Server
                   |
          +--------+--------+
          |        |        |
          v        v        v
         Add    Multiply  Divide
                   |
          Subtract (also available)
                   |
                   v
             Calculation Result
                   |
                   v
             LangChain Agent
                   |
                   v
              Final Answer
```

### How It Works

1. The user enters a calculation in natural language.
2. The LangChain agent sends the request to the Groq-hosted language model.
3. The model identifies the appropriate calculator tool and its arguments.
4. The MCP client communicates with the calculator server over standard input/output (`stdio`).
5. The MCP server executes the requested arithmetic operation.
6. The tool result returns to the agent.
7. The agent generates a clear response for the user.

**Key concept:** The LLM understands the request and chooses the tool, while Python executes the actual arithmetic operation.

## 📂 Project Structure

```text
langchain-mcp-calculator/
│
├── cal_server.py       # MCP server exposing calculator tools
├── client.py           # LangChain agent and interactive CLI
├── requirements.txt    # Python dependencies
├── .env                # Groq API key (not committed to Git)
├── .gitignore          # Excludes secrets and generated files
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-mcp-calculator.git
cd langchain-mcp-calculator
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

**Windows:**

```powershell
