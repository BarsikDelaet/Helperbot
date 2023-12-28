"""Раздел Помоч: детям, собакам, старшим
Все инструкции по этому вопросу."""


from option import answer
from keyboards import keyboard_menu
from option.service import Service
from keyboards.helper.for_helper import get_keyboard_helper
from option.inside_helper.kids import Kids
from option.inside_helper.homeless import Homeless
from option.inside_helper.woman import Woman
from option.inside_helper.adults import Adults
from option.inside_helper.elderly import Elderly
from option.inside_helper.animal import Animal
from option.inside_helper.nature import Nature
from option.inside_helper.own_version import OwnVersion


class Helper(Service):
    """Создание и обработка всех кнопок раздела."""

    def menu_helper(self, msg):
        """Меню с конпками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_HELPER,
                              reply_markup=get_keyboard_helper())
        self.bot.register_next_step_handler(msg, self.choice_helper)

    def choice_helper(self, msg):
        """Обрабатывает выбранный пункт и отправляет соответствующую информацию."""
        text_msg = msg.text.lower()
        if text_msg == keyboard_menu.CHOICE_HELPER[0]:  # Детям
            info = Kids(self.bot)
            info.menu_kids(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[1]:  # Бездомному
            info = Homeless(self.bot)
            info.menu_homeless(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[2]:  # Природе
            info = Nature(self.bot)
            info.menu_nature(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[3]:  # Женщинам
            info = Woman(self.bot)
            info.menu_woman(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[4]:  # Взрослым
            info = Adults(self.bot)
            info.menu_adults(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[5]:  # Старшим или пожилым
            info = Elderly(self.bot)
            info.menu_elderly(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[6]:  # Животному
            info = Animal(self.bot)
            info.menu_animal(msg)

        elif text_msg == keyboard_menu.CHOICE_HELPER[7]:  # Мой вариант
            info = OwnVersion(self.bot)
            info.menu_own_version(msg)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_helper)
