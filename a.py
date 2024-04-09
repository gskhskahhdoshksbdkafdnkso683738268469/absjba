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

from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('6305519973:AAE3EIcBD5HPdAJ0ae5J6vlvsd-9LwMHWsQ')



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling())
