from datetime import date

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def time(update: Update, context: CallbackContext):
    update.message.reply_text(f"Today: {date.today()}")


updater = Updater("1315138805:AAGSVl4y0a5HS8addQRBgSq-QPeC00QyM7Y")

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("today", time))

updater.start_polling()
updater.idle()
