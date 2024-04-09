from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler, ContextTypes,filters
import requests as r
from flask import Flask
from threading import Thread


ap = Flask(__name__)

@ap.route('/')
def aaa():
  return "ji"


def aa():
  ap.run(host="0.0.0.0")


ax = Thread(target=aa)
print(1)
ax.start()
print(2)

#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

async def start(update, context):
    # Define your keyboard buttons
    keyboard = [['Button 1', 'Button 2'], ['Button 3', 'Button 4']]

    # Create a ReplyKeyboardMarkup object
    reply_markup = ReplyKeyboardMarkup(keyboard)

    # Send a message with the keyboard
    await update.message.reply_text('Choose a button:', reply_markup=reply_markup)

app = ApplicationBuilder().token("6305519973:AAHC8f6IIw_rHUFPNo055cPGR8gGMToqbIY").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.Regex(r"aabc"), start))

app.run_polling()

