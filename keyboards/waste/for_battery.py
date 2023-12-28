from telebot import types
from .keyboard import CHOICE_BATTERY


def get_keyboard_battery():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_BATTERY[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BATTERY[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BATTERY[2].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
