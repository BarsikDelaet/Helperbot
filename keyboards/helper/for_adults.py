from telebot import types
from .keyboard import CHOICE_ADULTS


def get_keyboard_adults():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_ADULTS[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ADULTS[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ADULTS[2].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
