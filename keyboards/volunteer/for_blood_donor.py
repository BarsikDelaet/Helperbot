from telebot import types
from .keyboard import CHOICE_BLOOD_DONOR


def get_keyboard_blood_donor():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_BLOOD_DONOR[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BLOOD_DONOR[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BLOOD_DONOR[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BLOOD_DONOR[3].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
