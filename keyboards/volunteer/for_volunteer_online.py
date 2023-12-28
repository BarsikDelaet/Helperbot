from telebot import types
from .keyboard import CHOICE_ONLINE


def get_keyboard_volunteer_online():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_ONLINE[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ONLINE[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ONLINE[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ONLINE[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ONLINE[4].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
