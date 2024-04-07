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

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6973256484:AAHmY_cTcuzwA6bnFjzUszwb6OESiqJPNdU").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
