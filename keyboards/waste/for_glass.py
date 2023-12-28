from telebot import types
from .keyboard import CHOICE_GLASS


def get_keyboard_glass():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_GLASS[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_GLASS[1].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
