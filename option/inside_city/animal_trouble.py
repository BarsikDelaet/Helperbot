"""Кнопки и информация о Людях в беде."""

from option.service import Service
from option.inside_city import answer
import answer_main
from keyboards.city import keyboard
from keyboards import keyboard_menu
from option.answer import HELLO_CITY
from keyboards.city.for_animal_trouble import get_keyboard_animal_trouble
from option.inside_city.animal_home import AnimalHome
from option.inside_city.animal_wild import AnimalsWild


class AnimalTrouble(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_animal_trouble(self, msg):
        """Меню с кнопками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_CITY,
                              reply_markup=get_keyboard_animal_trouble())
        self.bot.register_next_step_handler(msg, self.choice_animal_trouble)

    def choice_animal_trouble(self, msg):
        """Обработка кнопок."""
        text_msg = msg.text.lower()
        if text_msg == keyboard.CHOICE_ANIMAL_TROUBLE[0]:  # Дикое живтоное
            info = AnimalsWild(self.bot)
            info.menu_animal_wild(msg)

        elif text_msg == keyboard.CHOICE_ANIMAL_TROUBLE[1]:  # Домашнее животное
            info = AnimalHome(self.bot)
            info.menu_animal_home(msg)

        elif text_msg in keyboard_menu.CHOICE_CITY:
            self.bot.send_message(msg.chat.id, HELLO_CITY)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_animal_trouble)
