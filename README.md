# AI Customer Support Agent

A beginner-friendly Python project that uses Google's Gemini AI to answer customer support questions and manage support tickets.

## Features

- AI-generated responses using Gemini
- Customer support for common questions
- Create and save support tickets
- View saved support tickets
- Search tickets by ticket ID
- Update ticket status
- Handle errors and API connection failures

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## Project Files

- `app.py` — Main customer support application
- `ticket_manager.py` — Creates, searches, views, and updates tickets
- `gemini_helper.py` — Connects the application to Gemini AI
- `requirements.txt` — Python dependencies
- `.gitignore` — Excludes sensitive and local files

## Setup

1. Install Python.
2. Install the required packages:

   `pip install -r requirements.txt`

3. Create a `.env` file in the project folder and add your Gemini API key:

   `GEMINI_API_KEY=your_api_key_here`

4. Run the application:

   `python app.py`

## Security

Never upload your `.env` file or share your API key publicly. Local ticket data is excluded from GitHub.

## Project Status

This project is being developed as a beginner-level Python AI customer support application.
