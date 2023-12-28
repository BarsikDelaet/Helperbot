from telebot import types
from .keyboard import CHOICE_PEOPLE_STREET


def get_keyboard_people_street():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_STREET[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_STREET[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_STREET[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_STREET[3].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
