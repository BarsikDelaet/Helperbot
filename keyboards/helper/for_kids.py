from telebot import types
from .keyboard import CHOICE_KIDS


def get_keyboard_kids():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_KIDS[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS[2].capitalize()}")
       ]
    markup.add(*buttons)

    return markup
