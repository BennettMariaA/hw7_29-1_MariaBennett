from aiogram.dispatcher import dispatcher
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Добро пожаловать в викторину. Готовы начать?")

def quiz_handler(update, context):
    question = "Какой язык программирования вы предпочитаете?"
    answers = ["Python", "Java", "C++"]
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(answer, callback_data=answer)] for answer in answers])
    context.bot.send_message(chat_id=update.effective_chat.id, text=question, reply_markup=reply_markup)

def answer_handler(update, context):
    query = update.callback_query
    answer = query.data
    context.bot.send_message(chat_id=query.message.chat_id, text=f"Ваш ответ: {answer}")

def main():
    updater = Updater("6056428908:AAFFmovqP0mVmkdGkRJubSUR4lgbYiZwW_M", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("quiz", quiz_handler))
    dispatcher.add_handler(CallbackQueryHandler(answer_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

def quiz_handler(update, context):
    question = "Какой язык программирования вы предпочитаете?"
    answers = ["Python", "Java", "C++"]
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(answer, callback_data=answer)] for answer in answers
    ])
    context.bot.send_message(chat_id=update.effective_chat.id, text=question, reply_markup=reply_markup)

def answer_handler(update, context):
    query = update.callback_query
    answer = query.data
    context.bot.send_message(chat_id=query.message.chat_id, text=f"Ваш ответ: {answer}")

def pin_handler(update, context):
    message = "pin!"

def main():
    dispatcher.add_handler(CommandHandler("quiz", quiz_handler))
    dispatcher.add_handler(CallbackQueryHandler(answer_handler))




