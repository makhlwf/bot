import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text(f"Olá {update.message.from_user.first_name}!")


def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    logger.warning(f'Update "{update}" caused error "{error}"')


def main():

    TOKEN = "TOKEN recebido pelo @Botfather"
    NAME = "Nome do app criado na Heroku"
    PORT = os.environ.get('PORT',5000)

    up = Updater(TOKEN)
    dp = up.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    up.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    up.bot.setWebhook(f"https://{NAME}.herokuapp.com/{TOKEN}")
    up.idle()

if __name__ == "__main__":
    main()