from telebot import types
from .keyboard import CHOICE_ELDERLY_NEIGHBORS


def get_keyboard_elderly_neighbors():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_NEIGHBORS[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_NEIGHBORS[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_NEIGHBORS[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ELDERLY_NEIGHBORS[3].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
