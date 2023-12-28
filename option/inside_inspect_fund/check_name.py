"""Информация о проверке названий организаций и фондов"""
from option.service import Service
from telebot import types
import random
import answer_main
from option.find_true_fund import find_fund
from option.inside_inspect_fund import answer
from keyboards import general
from keyboards.for_menu import get_keyboard_menu
from keyboards.for_feedback import get_keyboard_feedback
from keyboards.for_choice_repeat_or_next import get_keyboard_choice_repeat_or_next
from keyboards.inspect_fund.for_inspect_fund import get_keyboard_inspect_fund


class CheckName(Service):

    """Вывод информации по разделу"""
    def menu_check_name(self, msg):
        """Меню с возвратом"""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_INSPECT_FUND_INPUT_MSG,
                              reply_markup=types.ReplyKeyboardRemove())

        self.bot.register_next_step_handler(msg, self.check_fund)

    def check_fund(self, msg):
        """Проверяет организацию через известные источники"""
        msg_id = self.bot.send_message(msg.chat.id, "Ищу...",
                              reply_markup=types.ReplyKeyboardRemove())
        status = find_fund(msg.text)
        self.bot.delete_message(msg.chat.id, msg_id.id)
        if status:
            self.bot.send_message(msg.chat.id, answer.FUND_TRUE,
                                  reply_markup=get_keyboard_choice_repeat_or_next())
            self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)
        else:
            self.bot.send_message(msg.chat.id, answer.FUND_FALSE,
                                  reply_markup=get_keyboard_choice_repeat_or_next())
            self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)

    def choice_repeat_or_next(self, msg):
        """Обработка выбора возврата к меню или продолжения."""
        if msg.text.lower() == general.CHOICE_REPEAT[0]:
            self.bot.send_message(msg.chat.id, answer.CHOICE_REPEAT_OR_NEXT_FUND,
                                  reply_markup=get_keyboard_choice_repeat_or_next())
            self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)
        elif msg.text.lower() == general.CHOICE_REPEAT[1]:
            self.bot.send_message(msg.chat.id, answer.MSG_FUND,
                                  reply_markup=get_keyboard_inspect_fund())
        else:
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_repeat_or_next)

    def processing_repeat_or_next(self, msg):
        """Обработка выбора главное меню, пред.раздел, совет, отзыв."""
        text_msg = msg.text.lower()
        if text_msg == general.CHOICE_REPEAT_OR_NEXT[0]:
            self.bot.send_message(msg.chat.id, answer_main.HELLO_MAIN,
                                  reply_markup=get_keyboard_menu())
        elif text_msg == general.CHOICE_REPEAT_OR_NEXT[1]:
            self.bot.send_message(msg.chat.id, answer.MSG_FUND,
                                  reply_markup=get_keyboard_inspect_fund())
        elif text_msg == general.CHOICE_REPEAT_OR_NEXT[2]:
            self.bot.send_message(msg.chat.id, f"Совет #{random.randint(1,100)}: Начни с себя!",
                                  reply_markup=get_keyboard_menu())
        elif text_msg == general.CHOICE_REPEAT_OR_NEXT[3]:
            self.bot.send_message(msg.chat.id, answer_main.ANSWER_FEEDBACK,
                                  reply_markup=types.ReplyKeyboardRemove())
            self.bot.register_next_step_handler(msg, self.feedback)
        else:
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)

    def feedback(self, msg):
        """Обработка отзыва."""
        self.bot.send_message(msg.chat.id, answer_main.THX_FEEDBACK,
                              reply_markup=get_keyboard_feedback())
        self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)
