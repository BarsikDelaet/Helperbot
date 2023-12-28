from telebot import types
from .keyboard import CHOICE_PEOPLE_LOST_ELDERLY


def get_keyboard_people_lost_elderly():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_ELDERLY[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_ELDERLY[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_ELDERLY[2].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
