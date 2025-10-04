# 🚀 LangChain Multi-Language Code Debugger (Powered by Gemini)

## Project Overview

This is an advanced **AI agent** built on the **LangChain framework** and powered by the **Gemini Large Language Model (LLM)**, designed for seamless integration into the developer's terminal. Its core function is to automate the process of finding and fixing errors across multiple programming languages, specifically **Python, C++, and Java**.

## How It Works

The system operates on a closed-loop "Observe-Reason-Act" agent model:

1.  **Input & Detection:** The user pastes buggy code. The agent first identifies the programming language (Python, C++, or Java).
2.  **Execution & Error Capture:** It uses a set of specialized **LangChain execution tools** (e.g., `execute_cpp_code`) to run the code in an isolated environment. This action captures the precise **stack trace** or error output.
3.  **LLM Analysis:** The captured error output and the original code are fed to the **Gemini LLM** (via the API key). Gemini analyzes the error and the code to diagnose the root cause.
4.  **Fix & Verification:** Gemini generates the **fully corrected code** and an explanation. Crucially, the agent attempts to **verify the fix** by running the corrected code again to confirm successful execution before presenting the final answer to the user.

## Motivation: Terminal-First Debugging

The primary motivation for this project is to drastically **reduce context switching** and **debugging time** in the daily development workflow.

* **Seamless Workflow:** By operating entirely within the command-line interface, developers no longer need to copy code, switch to a web browser, and then paste the fixed code back.
* **Speed and Efficiency:** Consolidating execution, error capture, LLM analysis, and fix generation into one place creates a fast, efficient, and educational debugging companion.
* **Daily Utility:** The goal is to build a tool that becomes an essential part of the developer's daily life, allowing them to identify and resolve bugs quickly and focus more on feature development and less on manual error hunting.
