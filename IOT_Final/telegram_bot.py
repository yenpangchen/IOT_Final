from telegram.ext import Updater, CommandHandler, CallbackContext,CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
import os


def hello(update: Update, context:CallbackContext) -> None:
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))

def start(update: Update, context:CallbackContext) -> None:
    update.message.reply_text("請將手張開並放置於鏡頭下面")
    update.message.reply_text('洗洗手、洗出健康、洗出快樂、YA！')
    os.system("python3 soapdispenser.py")
    
        
def main():
    updater = Updater('5059291452:AAFV1w3mvtYYQRQlAkijWe-jho2AGZffOZM')

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
        

    
if __name__ == '__main__':
    main()