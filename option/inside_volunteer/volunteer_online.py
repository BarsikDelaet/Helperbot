"""Кнопки и информация о <<отдаче>> игрушек."""

from option.service import Service
from telebot import types
import random
from option.inside_volunteer import answer
import answer_main
from keyboards import general
from keyboards.volunteer import keyboard
from keyboards.volunteer.for_volunteer_online import get_keyboard_volunteer_online
from keyboards.volunteer.for_volunteer import get_keyboard_volunteer
from keyboards.for_repeat import get_keyboard_repeat
from keyboards.for_choice_repeat_or_next import get_keyboard_choice_repeat_or_next
from keyboards.for_menu import get_keyboard_menu
from keyboards.for_feedback import get_keyboard_feedback


class VolunteerOnline(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_volunteer_online(self, msg):
        """Меню с кнопками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_VOLUNTEER,
                              reply_markup=get_keyboard_volunteer_online())
        self.bot.register_next_step_handler(msg, self.choice_volunteer_online)

    def choice_volunteer_online(self, msg):
        """Обработка кнопок."""
        text_msg = msg.text.lower()
        chat_id = msg.chat.id

        result_msg = answer.VOLUNTEER_ONLINE.get(text_msg, answer_main.UNDERSTAND_MSG)

        if text_msg in keyboard.CHOICE_ONLINE:
            self.bot.send_message(chat_id, result_msg,
                                  reply_markup=get_keyboard_repeat())
            self.bot.register_next_step_handler(msg, self.choice_repeat_or_next)

        else:
            self.bot.send_message(chat_id, result_msg)
            self.bot.register_next_step_handler(msg, self.choice_volunteer_online)

    def choice_repeat_or_next(self, msg):
        """Обработка выбора возврата к меню или продолжения."""
        if msg.text.lower() == general.CHOICE_REPEAT[0]:
            self.bot.send_message(msg.chat.id, answer.CHOICE_REPEAT_OR_NEXT_VOLUNTEER,
                                  reply_markup=get_keyboard_choice_repeat_or_next())
            self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)
        elif msg.text.lower() == general.CHOICE_REPEAT[1]:
            self.bot.send_message(msg.chat.id, answer.VOLUNTEER_MSG,
                                  reply_markup=get_keyboard_volunteer())
        else:
            self.bot.send_message(msg.chat.id, answer_main.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_repeat_or_next)

    def processing_repeat_or_next(self, msg):
        """Обработка выбора главное меню, пред.раздел, совет, отзыв."""
        text_msg = msg.text.lower()
        if text_msg == general.CHOICE_REPEAT_OR_NEXT[0]:
            citizens = 0
            self.bot.send_message(msg.chat.id, answer_main.HELLO_MAIN,
                                  reply_markup=get_keyboard_menu())
        elif text_msg == general.CHOICE_REPEAT_OR_NEXT[1]:
            self.bot.send_message(msg.chat.id, answer.VOLUNTEER_MSG,
                                  reply_markup=get_keyboard_volunteer())
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
