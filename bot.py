from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN = "7755733307:AAEp1ForpHNMHCnpm2veU9bzH9qAuVgZ-zQ"
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "OLUGAB Empire Bot is running."

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def start(update, context):
    update.message.reply_text("👑 Welcome to the OLUGAB MORINGA EMPIRE!\nVisit: https://www.olugab.life")

def help_command(update, context):
    update.message.reply_text("Type any message and I’ll respond. More features coming!")

def reply(update, context):
    update.message.reply_text("Thank you for your message. You’ll be linked to our support shortly.")

from telegram.ext import CallbackContext
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

if __name__ == "__main__":
    app.run()
