# code_debugger/main.py

import os
import dotenv
from agent import create_agent

def main():
    """
    Main entry point for the Code Debugger.
    """
    dotenv.load_dotenv()
    
    if not os.getenv("GOOGLE_API_KEY"):
        print("🚨 Error: GOOGLE_API_KEY is not set in your .env file.")
        return

    print("🚀 Welcome to the LangChain Code Debugger 🚀")
    print("👉 Paste the code you want to debug. When you're done, type 'EOF' on a new line by itself.")
    print("   Type 'exit' to end the session.")
    print("-" * 70)

    agent_executor = create_agent(model_name="gemini-1.5-flash", verbose=True)
    
    while True:
        try:
            print("\nPlease paste your code now (type 'EOF' on a new line to finish):")
            
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'EOF':
                    break
                if line.strip().lower() == 'exit':
                    lines = ['exit']
                    break
                lines.append(line)
            
            if lines and lines[0] == 'exit':
                print("🤖 Goodbye!")
                break

            code_to_debug = "\n".join(lines)

            if not code_to_debug.strip():
                continue

            # --- PROMPT IMPROVEMENT IS HERE ---
            task = f"""
            Please act as an expert Python debugger. Your task is to analyze and debug the code provided below.

            Here is the code:
            ```python
            {code_to_debug}
            ```

            Follow these steps:
            1. First, use the `execute_python_code` tool to run the code and confirm the error.
            2. Analyze the error and explain the root cause.
            3. Provide the fully corrected code.
            4. Verify your fix by running the corrected code with the `execute_python_code` tool.

            ***IMPORTANT RULE***
            When you use the `execute_python_code` tool, the 'Action Input' must be ONLY the raw Python code.
            Do NOT wrap the code in markdown backticks like ```python or ```.
            """

            print("\n🤖 Agent is analyzing the code...\n")
            
            response = agent_executor.invoke({"input": task})
            
            print("\n" + "="*70)
            print("✅ Debugging Complete. Here is the agent's final answer:")
            print("="*70 + "\n")
            print(f"{response.get('output', 'Sorry, I encountered an issue.')}")
            print("\n" + "-"*70)
            
        except KeyboardInterrupt:
            print("\n🤖 Session interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n🚨 An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()