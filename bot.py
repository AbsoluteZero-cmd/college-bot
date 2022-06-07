from ast import keyword
from email import message
from aiogram import Bot, Dispatcher, executor, types
from cgitb import handler
from lib2to3.pgen2 import token

from config import API_TOKEN
from texts import WELCOME_MESSAGE
from keyboards import HELP_MARKUP

import logging

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    logging.debug('Welcome message is sent successfully')

    await message.reply(WELCOME_MESSAGE)


@dp.message_handler(commands=['help'])
async def proceed_help_keyboard(message: types.Message):
    await message.reply('Here\'s what I can do:', reply_markup=HELP_MARKUP)



@dp.callback_query_handler(lambda c: c.data == 'button_find')
async def process_callback_button1(callback_query: types.CallbackQuery):
    logging.debug('Find button is clicked!')
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Find button is clicked!')


@dp.callback_query_handler(lambda c: c.data == 'button_stats')
async def process_callback_button1(callback_query: types.CallbackQuery):
    logging.debug('Stats button is clicked!')
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Stats button is clicked!')


@dp.callback_query_handler(lambda c: c.data == 'button_resources')
async def process_callback_button1(callback_query: types.CallbackQuery):
    logging.debug('Resources button is clicked!')
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Resources button is clicked!')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)