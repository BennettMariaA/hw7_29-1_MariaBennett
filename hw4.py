import sqlite3
from telegram.ext import Updater, ConversationHandler

conn = sqlite3.connect('mentors.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mentors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mentor_name TEXT,
        mentor_direction TEXT,
        mentor_age INTEGER,
        mentor_group TEXT
    )
''')

conn.close()

updater = Updater('5881946915:AAFmLj8q1YjRzq1GHTCb3g3TtU39rPT0ILw', context=True)
dispatcher = updater.dispatcher

def mentor_group_handler(update, context):
    mentor_group = update.message.text
    context.user_data['mentor_group'] = mentor_group

    conn = sqlite3.connect('mentors.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO mentors (mentor_name, mentor_direction, mentor_age, mentor_group)
        VALUES (?, ?, ?, ?)
    ''', (context.user_data['mentor_name'], context.user_data['mentor_direction'], context.user_data['mentor_age'], context.user_data['mentor_group']))

    conn.commit()
    conn.close()

    context.bot.send_message(chat_id=update.effective_chat.id, text="Ментор успешно добавлен.")
    return ConversationHandler.END

updater.start_polling()
