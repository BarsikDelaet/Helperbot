from telebot import types
from .keyboard import CHOICE_HOMELESS


def get_keyboard_homeless():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_HOMELESS[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HOMELESS[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HOMELESS[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HOMELESS[3].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
