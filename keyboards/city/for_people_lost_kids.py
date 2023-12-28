from telebot import types
from .keyboard import CHOICE_PEOPLE_LOST_KIDS


def get_keyboard_people_lost_kids():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_KIDS[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_KIDS[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_KIDS[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_PEOPLE_LOST_KIDS[3].title()}"),
            ]
    markup.add(*buttons)

    return markup
