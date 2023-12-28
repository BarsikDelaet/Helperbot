from telebot import types
from keyboards.general import CHOICE_FEEDBACK


def get_keyboard_feedback():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_FEEDBACK[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_FEEDBACK[1].capitalize()}")
        ]
    markup.add(*buttons)
    return markup
