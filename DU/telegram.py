import telegram

def send_telegram(config, subject, url):
    bot = telegram.Bot(token=config["account"]["token"])
    bot.sendMessage(chat_id=config["account"]["chatID"], text=subject + "\n" + url)