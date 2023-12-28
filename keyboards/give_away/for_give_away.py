from telebot import types
from ..keyboard_menu import CHOICE_GIVE_AWAY


def get_keyboard_give_away():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text=f"{CHOICE_GIVE_AWAY[0].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_GIVE_AWAY[1].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_GIVE_AWAY[2].capitalize()}"),
        types.KeyboardButton(text=f"{CHOICE_GIVE_AWAY[3].capitalize()}")
    ]
    markup.add(*buttons)

    return markup
