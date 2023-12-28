from telebot import types
from .keyboard import CHOICE_FEED_ANIMALS


def get_keyboard_feed_animals():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_FEED_ANIMALS[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_FEED_ANIMALS[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_FEED_ANIMALS[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_FEED_ANIMALS[3].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_FEED_ANIMALS[4].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_FEED_ANIMALS[5].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
