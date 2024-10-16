import logging
from aiogram import Bot,Dispatcher,types
from aiogram.utils import executor
from dotenv import load_dotenv
import os


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


#configure logging
logging.basicConfig(level=logging.INFO)

#initialsie the bot and dispatcher
bot = Bot(token = TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi!\n I am an Echo Bot!\n Powered by Aiogram")


@dp.message_handler()
async def echo(message: types.Message):
    """This will return echo message

    Args:
        message (types.Message): _description_
    """

    await message.reply(message.text)
    # await message.reply("Got it")    


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)    