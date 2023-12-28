from telebot import types
from .keyboard import CHOICE_TOYS


def get_keyboard_toys():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_TOYS[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TOYS[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TOYS[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TOYS[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TOYS[4].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_TOYS[5].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
