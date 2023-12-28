from telebot import types
from .keyboard import CHOICE_LIGHT_BULB


def get_keyboard_light_bulb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_LIGHT_BULB[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_LIGHT_BULB[1].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
