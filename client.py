import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

SYSTEM_PROMPT = """
You are a smart, friendly AI Calculator Assistant.

Understand mathematical requests written in natural language and provide
clear, concise, human-friendly answers.

Rules:
1. Use the available calculator tools for every arithmetic calculation.
2. Understand phrases such as "multiply 4 by 6", "4 times 6",
   "divide 100 by 4", and "subtract 17 from 50".
3. Preserve the correct order of operands.
4. Show the calculation and answer clearly.
5. Avoid LaTeX, Markdown formatting, and unnecessary explanations.
6. Use plain text with simple mathematical symbols.
7. Keep responses short and natural.
8. If the request is ambiguous, ask for clarification.

Examples:
User: Please multiply 4 by 6.
Assistant: 4 × 6 = 24

User: What is 25 times 8?
Assistant: 25 × 8 = 200

User: Divide 100 by 4.
Assistant: 100 ÷ 4 = 25

User: Subtract 17 from 50.
Assistant: 50 − 17 = 33

User: Add 12 and 18.
Assistant: 12 + 18 = 30
"""


async def main():
    # 1. Initialize the LLM
    model = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )

    # 2. Connect to the MCP calculator server
    client = MultiServerMCPClient(
        {
            "calculator": {
                "command": sys.executable,
                "args": [str(BASE_DIR / "cal_server.py")],
                "transport": "stdio",
            }
        }
    )

    # 3. Load tools exposed by the MCP server
    tools = await client.get_tools()

    print("Available tools:")
    for tool in tools:
        print("-", tool.name)

    # 4. Create the LangChain agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    print("\nCalculator AI is ready!")

    # 5. Accept natural-language calculations
    while True:
        user_input = input(
            "\nEnter your calculation (or 'exit'): "
        ).strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_input,
                        }
                    ]
                }
            )

            # 6. Display the final response
            final_message = response["messages"][-1]
            print("\nAI:", final_message.content)

        except Exception as error:
            print(f"\nSomething went wrong: {error}")


if __name__ == "__main__":
    asyncio.run(main())