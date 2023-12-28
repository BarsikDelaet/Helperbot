from telebot import types
from ..keyboard_menu import CHOICE_VOLUNTEER


def get_keyboard_volunteer():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_VOLUNTEER[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_VOLUNTEER[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_VOLUNTEER[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_VOLUNTEER[3].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
