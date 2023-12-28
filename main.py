"""Главное меню бота. Вывод приветсвенных сообщний. Клавиатура меню.
Переход к по кнопкам.
"""

import telebot
import time
import answer_main
from keyboards import keyboard_menu
from telebot import types
import config
from config import TOKEN
from keyboards.for_menu import get_keyboard_menu
from option.give_away import GiveAway
from option.helper import Helper
from option.city import City
from option.inspect_fund import InspectFund
from option.waste import Waste
from option.volunteer import Volunteer


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'menu'])
def message_start(msg):
    """Приветственное сообщение. Статистика и возможности.
       Клавиатура меню."""
    bot.send_message(msg.chat.id, answer_main.HELLO_MAIN, reply_markup=get_keyboard_menu())


@bot.message_handler()
def give_message(msg):
    """Обработка всех сообщений.(Кнопок клавиатуры и других сообщий не относящихся к клавиатуре."""
    text_msg = msg.text.lower()
    if text_msg == answer_main.CHOICE_MAIN[0]:  # Расскажи мне, что ты можешь
        bot.send_message(msg.chat.id, answer_main.I_DO, reply_markup=get_keyboard_menu())

    elif text_msg == answer_main.CHOICE_MAIN[1]:  # Отдать что-то ненужное
        info_give_away = GiveAway(bot)
        info_give_away.menu_give_away(msg)
        
    elif text_msg == answer_main.CHOICE_MAIN[2]:  # Помочь детям, собакам, старшим *
        info_helper = Helper(bot)
        info_helper.menu_helper(msg)

    elif text_msg == answer_main.CHOICE_MAIN[3]:  # Хочу проверить фонд/организацию
        info_inspect_fund = InspectFund(bot)
        info_inspect_fund.menu_inspect_fund(msg)

    elif text_msg == answer_main.CHOICE_MAIN[4]:  # Ситуация в городе: как действовать
        info_city = City(bot)
        info_city.menu_city(msg)

    elif text_msg == answer_main.CHOICE_MAIN[5]:  # Раздельно сдать отходы
        info_waste = Waste(bot)
        info_waste.menu_waste(msg)

    elif text_msg == answer_main.CHOICE_MAIN[6]:  # Где стать волонтером или донором
        info_volunteer = Volunteer(bot)
        info_volunteer.menu_volunteer(msg)

    elif text_msg == answer_main.CHOICE_MAIN[7]:  # Предложить что-то интересное
        bot.send_message(msg.chat.id, answer_main.SOMTHING_INTERESTING)

    elif text_msg == answer_main.CHOICE_MAIN[8]:  # Напишет свой вариант
        bot.send_message(msg.chat.id, answer_main.ANSWER_THEIR_QUESTION,
                         reply_markup=types.ReplyKeyboardRemove())
        """Передаю в функцию отправляющей акк оргов, возвращаю к меню..."""
        bot.register_next_step_handler(msg, their_questions)

    elif text_msg in keyboard_menu.CHOICE_GIVE_AWAY:  # Меню пожертвований
        info_give_away = GiveAway(bot)
        info_give_away.choice_give_away(msg)

    elif text_msg in keyboard_menu.CHOICE_HELPER:  # Меню помощи: детям, взрослым, собакам
        info_helper = Helper(bot)
        info_helper.choice_helper(msg)

    elif text_msg in keyboard_menu.CHOICE_CITY:  # Меню города
        info_city = City(bot)
        info_city.choice_city(msg)

    elif text_msg in keyboard_menu.CHOICE_INSPECT_FUND:  # Меню фондов/организаций
        info_inspect_fund = InspectFund(bot)
        info_inspect_fund.choice_inspect_fund(msg)

    elif text_msg in keyboard_menu.CHOICE_WASTE:  # Меню переработки
        info_waste = Waste(bot)
        info_waste.choice_waste(msg)

    elif text_msg in keyboard_menu.CHOICE_VOLUNTEER:  # Меню волонтерства
        info_volunteer = Volunteer(bot)
        info_volunteer.choice_volunteer(msg)

    else:  # Обработка сообщений не с кнопки
        bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG,
                         reply_markup=get_keyboard_menu())
        bot.register_next_step_handler(msg, give_message)


def their_questions(msg):
    """ Обработка кнопки "Свой вариант" """
    bot.send_message(config.CHAT_ID, f"""{msg.text}
@{msg.from_user.username}""")
    bot.send_message(msg.chat.id,   answer_main.THEIR_QUESTION, reply_markup=get_keyboard_menu())
    bot.register_next_step_handler(msg, give_message)


while True:  # Бесконечный цикл обработки
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
