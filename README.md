# Welcome Kit Bot 🤖

A Telegram bot that welcomes new members to your project community.

## Features
- Personalized welcome messages
- Quick links to documentation and resources
- Helpful commands
- Easy to deploy on Railway

## Commands
- `/start` - Show welcome message
- `/help` - Show available commands
- `/about` - Learn about the bot
- `/contact` - Get contact information

## Deployment on Railway

1. Fork this repository on GitHub
2. Create a new project on Railway
3. Connect your GitHub repository
4. Add the environment variable:
   - `TELEGRAM_BOT_TOKEN` = your bot token
5. Railway will automatically deploy

## Local Development

1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with your token
5. Run: `python main.py`

## Tech Stack
- Python 3.9+
- python-telegram-bot library
- Railway for hosting
