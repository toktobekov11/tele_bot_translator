import logging

from aiogram import (
    Bot, Dispatcher,
    executor, types
)

import config as cfg


logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.API_TOKEN)
dp = Dispatcher(bot)

# ls = str()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
        This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\n I'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    handler
    """
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
