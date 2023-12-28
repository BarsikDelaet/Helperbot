from telebot import types
from .keyboard import CHOICE_ANIMAL_WILD


def get_keyboard_animal_wild():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_WILD[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_ANIMAL_WILD[1].capitalize()}"),
            ]
    markup.add(*buttons)

    return markup
