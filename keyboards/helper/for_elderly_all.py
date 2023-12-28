from telebot import types
from .keyboard import CHOICE_ELDERLY_ALL


def get_keyboard_elderly_all():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_ALL[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_ALL[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_ALL[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_ALL[3].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_ALL[4].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_ALL[5].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
