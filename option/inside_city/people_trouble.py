"""Кнопки и информация о Людях в беде."""

from option.service import Service
from option.inside_city import answer
import answer_main
from keyboards.city import keyboard
from keyboards import keyboard_menu
from option.answer import HELLO_CITY
from keyboards.city.for_people_trouble import get_keyboard_people_trouble
from option.inside_city.people_lost import PeopleLost
from option.inside_city.people_fight import PeopleFight
from option.inside_city.people_street import PeopleStreet


class PeopleTrouble(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_people_trouble(self, msg):
        """Меню с кнопками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_CITY,
                              reply_markup=get_keyboard_people_trouble())
        self.bot.register_next_step_handler(msg, self.choice_people_trouble)

    def choice_people_trouble(self, msg):
        """Обработка кнопок."""
        text_msg = msg.text.lower()
        if text_msg == keyboard.CHOICE_PEOPLE_TROUBLE[0]:  # Человек потерялся
            info = PeopleLost(self.bot)
            info.menu_people_lost(msg)

        elif text_msg in keyboard.CHOICE_PEOPLE_TROUBLE[1]:  # Драка/кого-то обижают
            info = PeopleFight(self.bot)
            info.menu_people_fight(msg)

        elif text_msg == keyboard.CHOICE_PEOPLE_TROUBLE[2]:  # Стало плохо на улице/в транспорте
            info = PeopleStreet(self.bot)
            info.menu_people_street(msg)

        elif text_msg in keyboard_menu.CHOICE_CITY:
            self.bot.send_message(msg.chat.id, HELLO_CITY)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_people_trouble)
