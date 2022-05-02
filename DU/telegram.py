import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_telegram(config, subject, url):
    bot = telegram.Bot(token=config["account"]["token"])
    reply_markup = [[InlineKeyboardButton(text="바로가기", url=url)]]
    bot.sendMessage(chat_id=config["account"]["chatID"], text=subject, reply_markup=InlineKeyboardMarkup(reply_markup))
