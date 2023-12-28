"""Кнопки и информация о Людях в беде."""

from option.service import Service
from option.inside_helper import answer
import answer_main
from keyboards.helper import keyboard
from keyboards import keyboard_menu
from option.answer import HELLO_HELPER
from keyboards.helper.for_kids import get_keyboard_kids
from option.inside_helper.kids_lost import KidsLost
from option.inside_helper.kids_disease import KidsDisease
from option.inside_helper.kids_orphan import KidsOrphan


class Kids(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_kids(self, msg):
        """Меню с кнопками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_HELPER,
                              reply_markup=get_keyboard_kids())
        self.bot.register_next_step_handler(msg, self.choice_kids)

    def choice_kids(self, msg):
        """Обработка кнопок."""
        text_msg = msg.text.lower()
        if text_msg == keyboard.CHOICE_KIDS[0]:  # Ребенок потерялся
            info = KidsLost(self.bot)
            info.menu_kids_lost(msg)

        elif text_msg == keyboard.CHOICE_KIDS[1]:  # Детям с заболеваниями
            info = KidsDisease(self.bot)
            info.menu_kids_disease(msg)

        elif text_msg == keyboard.CHOICE_KIDS[2]:  # Детям-сиротам
            info = KidsOrphan(self.bot)
            info.menu_kids_orphan(msg)

        elif text_msg in keyboard_menu.CHOICE_HELPER:
            self.bot.send_message(msg.chat.id, HELLO_HELPER)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_kids)
