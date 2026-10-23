# AI Customer Support Agent

## Project Overview

An AI-powered customer support chatbot built using Python and Google's Gemini API. It answers customer questions and helps manage support tickets.

## Features

- AI-generated customer support responses using Gemini
- Rule-based answers for common questions
- Create and search support tickets
- Ticket priority classification
- Update ticket status
- View ticket summaries and dashboards
- Search tickets by issue keyword
- Collect and view customer feedback
- Calculate average customer ratings
- Generate a project status report

## Technologies Used

- Python
- Google Gemini API
- VS Code
- `google-genai`
- `python-dotenv`
- Text files for ticket and feedback storage

## Project Files

- `app.py` — Main chatbot application
- `ticket_manager.py` — Ticket and feedback management
- `gemini_helper.py` — Gemini API integration
- `tickets.txt` — Saved support tickets (local data)
- `feedback.txt` — Saved customer feedback (local data)
- `.env` — Local API key configuration; never upload this file
- `requirements.txt` — Required Python packages
- `.gitignore` — Excludes secret and temporary files

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal in the project folder.
4. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Create a `.env` file and configure your Gemini API key using the environment variable name expected by `gemini_helper.py`.
6. Run the application:

   ```bash
   python app.py
   ```

## Security

- Never upload `.env` or expose your Gemini API key publicly.
- Keep API keys private.
- Use `.gitignore` to exclude secrets and temporary Python files.

## Future Improvements

- Build a web-based user interface
- Integrate a database for ticket storage
- Add automated testing
- Improve ticket reporting and analytics
