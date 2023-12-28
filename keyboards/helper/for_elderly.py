from telebot import types
from .keyboard import CHOICE_ELDERLY


def get_keyboard_elderly():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_ELDERLY[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY[2].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
