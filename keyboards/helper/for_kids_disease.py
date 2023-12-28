from telebot import types
from .keyboard import CHOICE_KIDS_DISEASE


def get_keyboard_kids_disease():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[3].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[4].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[5].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[6].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[7].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[8].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[9].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[10].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_KIDS_DISEASE[11].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
