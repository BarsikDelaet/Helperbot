from telebot import types
from .keyboard import CHOICE_TECHNIC


def get_keyboard_technic():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_TECHNIC[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TECHNIC[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TECHNIC[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TECHNIC[3].capitalize()}")

        ]
    markup.add(*buttons)

    return markup
