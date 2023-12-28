from telebot import types
from ..keyboard_menu import CHOICE_INSPECT_FUND


def get_keyboard_inspect_fund():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_INSPECT_FUND[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_INSPECT_FUND[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_INSPECT_FUND[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_INSPECT_FUND[3].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
