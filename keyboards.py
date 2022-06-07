from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


button_find = InlineKeyboardButton('Find the university 🔎', callback_data='button_find')
button_stats = InlineKeyboardButton('My stats 📋', callback_data='button_stats')
button_resources = InlineKeyboardButton('Useful resources 📚', callback_data='button_resources')

HELP_MARKUP = InlineKeyboardMarkup().add(button_find).add(button_stats).add(button_resources)