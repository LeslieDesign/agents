#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from financial_researcher.crew import ResearchCrew

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Map OpenRouter env to OpenAI-compatible vars if present
if os.getenv('OPENROUTER_API_KEY') and not os.getenv('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENROUTER_API_KEY')

if os.getenv('OPENROUTER_API_KEY') and not os.getenv('OPENAI_BASE_URL'):
    os.environ['OPENAI_BASE_URL'] = 'https://openrouter.ai/api/v1'

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    inputs = {
        'company': 'Apple'
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()