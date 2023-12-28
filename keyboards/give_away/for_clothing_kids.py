from telebot import types
from .keyboard import CHOICE_CLOTHING


def get_keyboard_clothing_kids():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_CLOTHING[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_CLOTHING[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_CLOTHING[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_CLOTHING[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_CLOTHING[4].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
