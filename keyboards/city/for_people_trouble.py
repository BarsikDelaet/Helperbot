from telebot import types
from .keyboard import CHOICE_PEOPLE_TROUBLE


def get_keyboard_people_trouble():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_TROUBLE[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_TROUBLE[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_TROUBLE[2].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
