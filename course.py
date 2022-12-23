import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5291009377:AAFUw0Pjfa9i2wsTI4sscK2pVOQCbmx5lfc'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def kirit(x):
    # Where USD is the base currency you want to use

    url = f"https://v6.exchangerate-api.com/v6/e2f0123a768eff54090e5aec/pair/{x.upper()}/UZS"

    # Making our request
    response = requests.get(url)
    data = response.json()

    uzs = (data['conversion_rate'])
    time = data['time_last_update_utc']
    javob = f"1 {x.upper()} = {uzs} so'm\n\nVaqt: {data['time_last_update_utc']}\n\n" \
            f"Keyingi kurs yangilanadigan vaqt: {data['time_next_update_utc']}"
    return(javob)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Valyuta botiga Xush kelibsiz!!!\nValyuta birligini kiriting --> (Misol uchun:usd)")

@dp.message_handler()
async def course(message: types.Message):
    try:
        natija = kirit(message.text)
        await message.reply(natija)
    except:
        await  message.reply("Valyuta birligini kiriting !!!!\nMisol uchun: usd, rub,eur......")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
