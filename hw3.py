from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

MENTOR_ID, MENTOR_NAME, MENTOR_DIRECTION, MENTOR_AGE, MENTOR_GROUP = range(5)

def add_mentor_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Давайте добавим нового ментора.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите ID ментора:")
    return MENTOR_ID

def mentor_id_handler(update, context):
    mentor_id = update.message.text
    context.user_data['mentor_id'] = mentor_id
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите имя ментора:")
    return MENTOR_NAME

def mentor_name_handler(update, context):
    mentor_name = update.message.text
    context.user_data['mentor_name'] = mentor_name
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите направление:")
    return MENTOR_DIRECTION

def mentor_direction_handler(update, context):
    mentor_direction = update.message.text
    context.user_data['mentor_direction'] = mentor_direction
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите возраст ментора:")
    return MENTOR_AGE

def mentor_age_handler(update, context):
    mentor_age = update.message.text
    context.user_data['mentor_age'] = mentor_age
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите группу ментора:")
    return MENTOR_GROUP

def mentor_group_handler(update, context):
    mentor_group = update.message.text
    context.user_data['mentor_group'] = mentor_group

    context.bot_data.setdefault('mentors', []).append(context.user_data)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Ментор успешно добавлен.")
    return ConversationHandler.END

def main():
    updater = Updater("5881946915:AAFmLj8q1YjRzq1GHTCb3g3TtU39rPT0ILw", use_context=True)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("add_mentor", add_mentor_handler)],
        states={
            MENTOR_ID: [MessageHandler(Filters.text, mentor_id_handler)],
            MENTOR_NAME: [MessageHandler(Filters.text, mentor_name_handler)],
            MENTOR_DIRECTION: [MessageHandler(Filters.text, mentor)]