import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5183908850:AAE-AtU9gnrAI7wcHTal1T1xz6Q3ps-3R54'

wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipedia botiga Xush kelibsiz !!!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)