from telebot import types
from .keyboard import CHOICE_KIDS_ORPHAN


def get_keyboard_kids_orphan():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[3].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[4].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[5].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[6].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[7].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[8].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[9].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[10].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_ORPHAN[11].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
