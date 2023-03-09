import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5819290456:AAER1y6az0jTQnLSN9Gi0BbxDSUL_0x9E28'
wikipedia.set_lang("uz")
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.answer("<b>Assalomu alaykum\nWikipedia botiga xush kelibsiz😊\nIltimos, "
                         "o'zingizga kerakli bo'lgan maqola nomini yuboring!</b>")

@dp.message_handler(commands=['help'])
async def yordam(message: types.Message):
    await message.answer("Botimizdan ma'lumot topolmagan "
                         "bo'lsangiz unda aqlingizni ishlating😂😊\n<b>Admin bilan a'loqa:</b>https://t.me/Asliddinbek_official")

@dp.message_handler()
async def sendWiki(message: types.Message):
   try:
       respond = wikipedia.summary(message.text)
       await message.reply(respond)
   except:
       await message.reply('<b>Bu mavzuga oid maqola topilmadi</b>')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)