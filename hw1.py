from aiogram import Bot, Dispatcher
from aiogram.utilse import executor
from decouple import config

API_TOKEN = config
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

@dp.CommandHandler(commands=['mem'])
    pass

@dp.MessageHandler(update, context):
    message = update.message.text
    try:
        number = int(message)
        square = number ** 2
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(square))
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

 @dp.MessageHandler(executor, context):
message = update.message.text
try:
    number = int(message)
    square = number ** 2
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(square))
except ValueError:
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    if name == ‘__main__’:
        executor.start_polling(dp, skip_updates=True)

executor.start_polling(skip_updates=True)
executor.idle()

if __name__ == '__main__':
    executor()

