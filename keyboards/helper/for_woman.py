from telebot import types
from .keyboard import CHOICE_WOMAN


def get_keyboard_woman():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_WOMAN[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WOMAN[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WOMAN[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WOMAN[3].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WOMAN[4].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WOMAN[5].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_WOMAN[6].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
