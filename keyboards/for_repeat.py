from telebot import types
from keyboards.general import CHOICE_REPEAT


def get_keyboard_repeat():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_REPEAT[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_REPEAT[1].capitalize()}")
        ]
    markup.add(*buttons)

    return markup
