from telebot import types
from .keyboard import CHOICE_ANIMAL_HOME


def get_keyboard_animal_home():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_HOME[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_HOME[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_HOME[2].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
