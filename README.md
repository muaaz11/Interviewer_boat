# Interview Coach Bot

A terminal-based mock interviewer built with Python and the Groq API.
Pick an interviewer personality (strict, friendly, or senior dev) and the bot runs a live interview, asking one question at a time.
It keeps the full conversation history in memory, so follow-up questions and feedback build on your earlier answers.

## Run

1. `pip install groq python-dotenv`
2. Create a `.env` file with `GROQ_API_KEY=your_key`
3. `python main.py`
