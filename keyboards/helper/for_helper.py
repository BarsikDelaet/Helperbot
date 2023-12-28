from telebot import types
from ..keyboard_menu import CHOICE_HELPER


def get_keyboard_helper():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_HELPER[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[3].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[4].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[5].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[6].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_HELPER[7].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
