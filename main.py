import os
import logging
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN: Final = os.getenv("TOKEN") or ""
BOT_USERNAME: Final = os.getenv("BOT_USERNAME") or ""

logger = logging.getLogger(__name__)
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am a bot btw :)")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am a bot btw :)")

# Responses

def handle_reponse(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hey there!"

    if "thank" in processed:
        return "You're welcome!"
    
    if ("how" and "r" and "u") in processed:
        return "I'm fine thanks! How can I help?"
    
    

    return "I do not understand bro..."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    logger.info(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_reponse(new_text)
        else:
            return
    else:
        response: str = handle_reponse(text)

    logger.info("Bot:", "{response}")
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Update {update} caused error {context.error}")










if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    logger.info("Polling...")
    app.run_polling(poll_interval=0.1)





