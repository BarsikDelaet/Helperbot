from telebot import types
from .keyboard import CHOICE_PLASTIC


def get_keyboard_plastic():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_PLASTIC[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PLASTIC[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PLASTIC[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PLASTIC[3].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
