from telebot import types
from .keyboard import CHOICE_KIDS_LOST


def get_keyboard_kids_lost():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_KIDS_LOST[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_LOST[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_LOST[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_LOST[3].title()}")
        ]
    markup.add(*buttons)

    return markup
