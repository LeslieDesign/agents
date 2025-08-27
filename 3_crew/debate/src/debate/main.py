#!/usr/bin/env python
import os
import sys
import warnings

from datetime import datetime

from debate.crew import Debate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

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

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'There needs to be strict laws to regulate LLMs',
    }
    
    try:
        result = Debate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
