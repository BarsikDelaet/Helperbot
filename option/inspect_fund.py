"""Раздел <<Проверить фонд/организацию>>
Все инструкции по этому вопросу."""

from option import answer
from keyboards import keyboard_menu
from option.service import Service
from option.inside_inspect_fund.check_name import CheckName
from option.inside_inspect_fund.check_fund import CheckFund
from option.inside_inspect_fund.alms_streets import AlmsOnStreets
from option.inside_inspect_fund.check_not_fund import CheckNotFund
from keyboards.inspect_fund.for_inspect_fund import get_keyboard_inspect_fund


class InspectFund(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_inspect_fund(self, msg):
        """Меню с конпками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSPECT_FUND,
                              reply_markup=get_keyboard_inspect_fund())
        self.bot.register_next_step_handler(msg, self.choice_inspect_fund)

    def choice_inspect_fund(self, msg):
        """Обрабатывает выбранный пункт и отправляет соответствующую информацию.
        Проверить фонд или организацю/Проверить не фонд/Милостыня на улице/Проверить по названию/Обработка не кнопки"""
        text_msg = msg.text.lower()
        if text_msg == keyboard_menu.CHOICE_INSPECT_FUND[0]:  # Проверить фонд или организацю
            info = CheckFund(self.bot)
            info.menu_check_fund(msg)

        elif text_msg == keyboard_menu.CHOICE_INSPECT_FUND[1]:  # Проверить не фонд
            info = CheckNotFund(self.bot)
            info.menu_check_not_fund(msg)

        elif text_msg == keyboard_menu.CHOICE_INSPECT_FUND[2]:  # Милостыня на улице
            info = AlmsOnStreets(self.bot)
            info.menu_alms_streets(msg)

        elif text_msg == keyboard_menu.CHOICE_INSPECT_FUND[3]:  # Проверить по названию
            info = CheckName(self.bot)
            info.menu_check_name(msg)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_inspect_fund)


