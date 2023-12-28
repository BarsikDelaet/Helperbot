from telebot import types
from .keyboard import CHOICE_ANIMAL_TROUBLE


def get_keyboard_animal_trouble():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_TROUBLE[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_TROUBLE[1].capitalize()}")
            ]
    markup.add(*buttons)

    return markup
