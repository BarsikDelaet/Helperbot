from telebot import types
from .keyboard import CHOICE_MARROW_DONOR


def get_keyboard_bone_marrow_donor():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_MARROW_DONOR[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_MARROW_DONOR[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_MARROW_DONOR[2].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
