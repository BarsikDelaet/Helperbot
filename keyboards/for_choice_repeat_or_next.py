from telebot import types
from keyboards.general import CHOICE_REPEAT_OR_NEXT


def get_keyboard_choice_repeat_or_next():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
            types.KeyboardButton(text=f"{CHOICE_REPEAT_OR_NEXT[0].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_REPEAT_OR_NEXT[1].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_REPEAT_OR_NEXT[2].capitalize()}"),
            types.KeyboardButton(text=f"{CHOICE_REPEAT_OR_NEXT[3].capitalize()}")
        ]
    markup.add(*buttons)
    return markup
