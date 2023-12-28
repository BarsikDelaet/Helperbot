"""Раздел Раздельно сдать отходы
Все инструкции по этому вопросу."""

from option import answer
from keyboards import keyboard_menu
from option.service import Service
from keyboards.waste.for_waste import get_keyboard_waste
from option.inside_waste.plastic import Plastic
from option.inside_waste.battery import Battery
from option.inside_waste.glass import Glass
from option.inside_waste.light_bulb import LightBulb


class Waste(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_waste(self, msg):
        """Меню с конпками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_WASTE,
                              reply_markup=get_keyboard_waste())
        self.bot.register_next_step_handler(msg, self.choice_waste)

    def choice_waste(self, msg):
        """Обрабатывает выбранный пункт и отправляет соответствующую информацию.
        Пластик/Батарейки/Стекло/Лампочки"""
        text_msg = msg.text.lower()
        if text_msg == keyboard_menu.CHOICE_WASTE[0]:  # Пластик
            info = Plastic(self.bot)
            info.menu_plastic(msg)

        elif text_msg == keyboard_menu.CHOICE_WASTE[1]:  # Батарейка
            info = Battery(self.bot)
            info.menu_battery(msg)

        elif text_msg == keyboard_menu.CHOICE_WASTE[2]:  # Стекло
            info = Glass(self.bot)
            info.menu_glass(msg)

        elif text_msg == keyboard_menu.CHOICE_WASTE[3]:  # Лампочки
            info = LightBulb(self.bot)
            info.menu_light_bulb(msg)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_waste)


