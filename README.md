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
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Groq API Key

Obtain an API key through the [Groq Console](https://console.groq.com/).

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
python client.py
```

The application will display the available calculator tools and prompt you to enter a calculation.

The MCP server is started automatically by the client. You do not need to start it separately.

## 💻 Usage Examples

Start the application:

```text
Available tools:
- add
- subtract
- multiply
- divide

Calculator AI is ready!
```

Example interactions:

| User Input | Expected Result |
|---|---|
| `Please do 4 multiply by 6` | `4 × 6 = 24` |
| `What is 25 times 8?` | `25 × 8 = 200` |
| `Can you divide 100 by 4?` | `100 ÷ 4 = 25` |
| `Subtract 17 from 50` | `50 − 17 = 33` |
| `Add 12 and 18` | `12 + 18 = 30` |

Type `exit` to stop the application.

*The exact wording and formatting of AI responses may vary.*

## 🔧 Available MCP Tools

The MCP server exposes four tools:

| Tool | Description | Example |
|---|---|---|
| `add(a, b)` | Adds two numbers | `add(12, 18) → 30` |
| `subtract(a, b)` | Subtracts the second number from the first | `subtract(50, 17) → 33` |
| `multiply(a, b)` | Multiplies two numbers | `multiply(4, 6) → 24` |
| `divide(a, b)` | Divides the first number by the second | `divide(100, 4) → 25` |

The division tool checks for division by zero and raises an error if the divisor is zero.

## 🧠 Key Concepts Learned

This project demonstrates the following concepts:

- **LLM-powered agents:** Using a language model to interpret requests and select tools.
- **Tool calling:** Allowing an LLM to request the execution of specific functions.
- **Model Context Protocol:** Exposing functions through a standardized client-server interface.
- **LangChain integration:** Connecting language models and external tools.
- **Agent orchestration:** Managing the interaction between the model, tools, and final response.
- **Environment variables:** Keeping API credentials outside the source code.
- **Asynchronous Python:** Using `asyncio` for asynchronous agent execution.

## 🔮 Future Improvements

- Add support for percentages, exponents, square roots, and scientific calculations.
- Display tool calls and execution results for debugging.
- Add conversation memory for contextual follow-up questions.
- Implement automated unit tests for calculator operations.
- Build a web interface using FastAPI and React.
- Add additional MCP servers to connect the agent to external services.

## 🔐 Security

- Store API credentials in a local `.env` file.
- Exclude `.env` and virtual environments through `.gitignore`.
- Never commit API keys or other secrets to version control.

## 👨‍💻 Author

**Digvijaysingh Gaikwad**

Built as a hands-on project to explore AI agents, LangChain, Groq, and the Model Context Protocol.
