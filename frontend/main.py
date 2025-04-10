import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
# import models from backend folder


load_dotenv()

API_KEY = os.getenv("TELEGRAM_API_KEY")

# creating app


def main() -> None:

    application = Application.builder().token(API_KEY).build()

    # commands
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))

    # message
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am a sarcasm detector bot! Please send me a text, and I'll tell you how likely it is to be sarcastic!") # can change text later!

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any text, and I'll analyze it to determine how likely it is that it's sarcastic 🧐") # can change text later!
    
# responses

def handle_response(text):
    return f"you sent {text}" # filler to just test out bot first
    """
    ideally each of the models should have a predict_sarcasm function
    loop to pass it through all the models, and take the average (i.e. score = amount of models that predict sarcastic / 6).

    e.g.
    predictions = []  # put the predictions in each of the models here
    average_score = sum(predictions) / 6
    if average_score >= 0.5:
        prediction = "Sarcastic"
        confidence = average_score * 100
    else if average_score < 0.5:
        prediction = "Not sarcastic"
        confidence = (1 - average_score) * 100

    reply_message = (
        "<b>Analysis Complete!</b>\n\n"
        f"<b>Your sentence:</b> ‘{text}’\n\n"
        f"<b>Prediction:</b> {prediction} (Confidence: {confidence:.0f}%)\n\n"
    )

    return reply_message
    """
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response, parse_mode = "HTML") # can change text later!



if __name__ == '__main__':
    main()