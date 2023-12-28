from telebot import types
from .keyboard import CHOICE_ECOLOGICAL_PROBLEM


def get_keyboard_ecological_problem():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[4].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[5].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[6].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[7].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ECOLOGICAL_PROBLEM[8].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
