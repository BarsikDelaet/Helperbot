from telebot import types
from ..keyboard_menu import CHOICE_WASTE


def get_keyboard_waste():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_WASTE[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WASTE[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WASTE[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WASTE[3].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
