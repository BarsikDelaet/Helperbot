from telebot import types
from .keyboard import CHOICE_ANIMAL


def get_keyboard_animal():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_ANIMAL[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_ANIMAL[1].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
