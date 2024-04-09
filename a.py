from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
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
ax.start()

#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

def start(update, context):
    # Define your keyboard buttons
    keyboard = [['Button 1', 'Button 2'], ['Button 3', 'Button 4']]

    # Create a ReplyKeyboardMarkup object
    reply_markup = ReplyKeyboardMarkup(keyboard)

    # Send a message with the keyboard
    update.message.reply_text('Choose a button:', reply_markup=reply_markup)

app = ApplicationBuilder().token("6305519973:AAE3EIcBD5HPdAJ0ae5J6vlvsd-9LwMHWsQ").build()

app.add_handler(CommandHandler("start", statt))

app.run_polling()

