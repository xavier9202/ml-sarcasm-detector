import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
load_dotenv()

API_KEY = os.getenv("TELEGRAM_API_KEY")

# creating app

def main() -> None:

    application = Application.builder().token(API_KEY).build()
    application = Application.builder().token(API_KEY).build()

    # commands
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))

    # message
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am a sarcasm detector bot!") # can change text later!

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any text, and I'll analyze it to determine how likely it is that it's sarcastic 🧐") # can change text later!
    
# responses

def handle_response(text):
    return f"you sent {text}" # filler to just test out bot first

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response) # can change text later!



if __name__ == '__main__':
    main()