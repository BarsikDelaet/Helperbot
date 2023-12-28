from telebot import types
from ..keyboard_menu import CHOICE_CITY


def get_keyboard_city():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_CITY[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_CITY[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_CITY[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_CITY[3].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
