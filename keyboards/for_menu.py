from telebot import types
from answer_main import CHOICE_MAIN


def get_keyboard_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    buttons = [
        types.KeyboardButton(text=f"{CHOICE_MAIN[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[3].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[4].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[5].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[6].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[7].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_MAIN[8].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
