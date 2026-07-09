import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

# Welcome message template
WELCOME_MESSAGE = """
🎉 *Welcome to the Project!* 🎉

Hello {first_name}! 👋

I'm your welcome bot. Here's what you can do:
• Get started with our project
• Find helpful resources
• Connect with the community

*Quick Links:*
📖 [Documentation](https://your-docs-link.com)
💬 [Community Chat](https://t.me/yourcommunity)
🐛 [Report Issues](https://github.com/yourrepo)

Type /help to see all available commands.
"""

HELP_MESSAGE = """
🤖 *Available Commands:*

/start - Show welcome message
/help - Show this help message
/about - Learn more about this bot
/contact - Get contact information

*Need something else?*
Just type any message and I'll respond! 😊
"""

ABOUT_MESSAGE = """
ℹ️ *About This Bot*

This is a welcome bot created for our project.
It helps new members get started and provides
quick access to important resources.

*Version:* 1.0.0
*Hosted on:* Railway
*Source Code:* [GitHub](https://github.com/yourrepo)
"""

CONTACT_MESSAGE = """
📞 *Contact Information*

Project Lead: @yourusername
Email: your@email.com
GitHub: https://github.com/yourrepo

*Need help?*
Join our community chat: https://t.me/yourcommunity
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when /start is issued."""
    user = update.effective_user
    first_name = user.first_name or "there"
    
    # Personalize the welcome message
    welcome_text = WELCOME_MESSAGE.format(first_name=first_name)
    
    # Create inline keyboard with buttons
    keyboard = [
        [
            InlineKeyboardButton("📖 Docs", url="https://your-docs-link.com"),
            InlineKeyboardButton("💬 Community", url="https://t.me/yourcommunity"),
        ],
        [
            InlineKeyboardButton("🐛 Report Issue", url="https://github.com/yourrepo/issues"),
            InlineKeyboardButton("⭐ Star on GitHub", url="https://github.com/yourrepo"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when /help is issued."""
    await update.message.reply_text(HELP_MESSAGE, parse_mode="Markdown")


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send an about message when /about is issued."""
    await update.message.reply_text(ABOUT_MESSAGE, parse_mode="Markdown")


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send contact information when /contact is issued."""
    await update.message.reply_text(CONTACT_MESSAGE, parse_mode="Markdown")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message for any other text messages."""
    user_message = update.message.text
    user = update.effective_user
    first_name = user.first_name or "there"
    
    response = f"Hey {first_name}! You said: \n\n\"{user_message}\"\n\nType /help to see what I can do."
    await update.message.reply_text(response)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle unknown commands."""
    await update.message.reply_text(
        "Sorry, I don't recognize that command. Type /help to see available commands."
    )


def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("contact", contact_command))
    
    # Register message handler for regular text (non-commands)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Register handler for unknown commands
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the bot (using polling)
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
