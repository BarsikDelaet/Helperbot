from telebot import types
from .keyboard import CHOICE_OFFLINE


def get_keyboard_volunteer_offline():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_OFFLINE[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_OFFLINE[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_OFFLINE[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_OFFLINE[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_OFFLINE[4].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
