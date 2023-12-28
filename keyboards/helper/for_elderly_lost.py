from telebot import types
from .keyboard import CHOICE_ELDERLY_LOST


def get_keyboard_elderly_lost():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_LOST[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_LOST[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_LOST[2].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
