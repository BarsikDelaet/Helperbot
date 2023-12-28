"""Кнопки и информация о Людях в беде."""

from option.service import Service
from option.inside_helper import answer
import answer_main
from keyboards.helper import keyboard
from keyboards import keyboard_menu
from option.answer import HELLO_HELPER
from keyboards.helper.for_elderly import get_keyboard_elderly
from option.inside_helper.elderly_lost import ElderlyLost
from option.inside_helper.elderly_all import ElderlyAll
from option.inside_helper.elderly_neighbors import ElderlyNeighbors


class Elderly(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_elderly(self, msg):
        """Меню с кнопками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_HELPER,
                              reply_markup=get_keyboard_elderly())
        self.bot.register_next_step_handler(msg, self.choice_elderly)

    def choice_elderly(self, msg):
        """Обработка кнопок."""
        text_msg = msg.text.lower()
        if text_msg == keyboard.CHOICE_ELDERLY[0]:  # Старшим вообще
            info = ElderlyAll(self.bot)
            info.menu_elderly_all(msg)

        elif text_msg == keyboard.CHOICE_ELDERLY[1]:  # Старшим соседям
            info = ElderlyNeighbors(self.bot)
            info.menu_elderly_neighbors(msg)

        elif text_msg == keyboard.CHOICE_ELDERLY[2]:  # Старшему который потерялся
            info = ElderlyLost(self.bot)
            info.menu_elderly_lost(msg)

        elif text_msg in keyboard_menu.CHOICE_HELPER:
            self.bot.send_message(msg.chat.id, HELLO_HELPER)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_elderly)
