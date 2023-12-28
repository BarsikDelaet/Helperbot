from telebot import types
from .keyboard import CHOICE_BOOK


def get_keyboard_book_people():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_BOOK[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BOOK[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BOOK[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BOOK[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BOOK[4].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BOOK[5].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_BOOK[6].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
