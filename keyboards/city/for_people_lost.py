from telebot import types
from .keyboard import CHOICE_PEOPLE_LOST


def get_keyboard_people_lost():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST[1].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
