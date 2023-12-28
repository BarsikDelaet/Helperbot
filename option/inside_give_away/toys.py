"""Кнопки и информация о <<отдаче>> игрушек."""

from option.service import Service
from telebot import types
import random
from option.inside_give_away import answer
import answer_main
from option.find_address import find_in_city
from keyboards import general
from keyboards.give_away import keyboard
from keyboards.give_away.for_toys import get_keyboard_toys
from keyboards.give_away.for_give_away import get_keyboard_give_away
from keyboards.for_repeat import get_keyboard_repeat
from keyboards.for_choice_repeat_or_next import get_keyboard_choice_repeat_or_next
from keyboards.for_menu import get_keyboard_menu
from keyboards.for_feedback import get_keyboard_feedback


class Toys(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_toys(self, msg):
        """Меню с кнопками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_INSIDE_GIVE_AWAY,
                              reply_markup=get_keyboard_toys())
        self.bot.register_next_step_handler(msg, self.choice_toys)

    def choice_toys(self, msg):
        """Обработка кнопок."""
        text_msg = msg.text.lower()
        chat_id = msg.chat.id

        result_msg = answer.TOYS.get(text_msg, answer_main.UNDERSTAND_MSG)

        if text_msg == keyboard.CHOICE_TOYS[0]:
            self.bot.send_message(chat_id, "В каком вы городе?",
                                  reply_markup=types.ReplyKeyboardRemove())  # Убрать клавиатуру
            self.bot.register_next_step_handler(msg, self.address_find)

        elif text_msg in keyboard.CHOICE_TOYS:
            self.bot.send_message(chat_id, result_msg,
                                  reply_markup=get_keyboard_repeat())
            self.bot.register_next_step_handler(msg, self.choice_repeat_or_next)

        else:
            self.bot.send_message(msg.chat.id, result_msg)
            self.bot.register_next_step_handler(msg, self.choice_toys)

    def address_find(self, msg):
        """Гуглим запрос по городу."""
        msg_id = self.bot.send_message(msg.chat.id, "Ищу...",
                              reply_markup=types.ReplyKeyboardRemove())
        result = find_in_city(msg.text, answer.ITEM_TOYS)
        self.bot.delete_message(msg.chat.id, msg_id.id)
        if result:
            if len(result) < 3:
                result.append(' ')
                result.append(' ')
            self.bot.send_message(msg.chat.id, f"""Вот что я смог найти в г.{msg.text}
{result[0]}
{result[1]}
{result[2]}
Можете поискать ещё информацию сами.""")
            self.bot.send_message(msg.chat.id, """Чек-лист для вас 
Фото/Текс/Документ.""",
                                  reply_markup=get_keyboard_repeat())
            self.bot.register_next_step_handler(msg, self.choice_repeat_or_next)
        else:
            self.bot.send_message(msg.chat.id, answer.ADDRESS_NOT_FOUND)
            self.bot.register_next_step_handler(msg, self.address_find)

    def choice_repeat_or_next(self, msg):
        """Обработка выбора возврата к меню или продолжения."""
        if msg.text.lower() == general.CHOICE_REPEAT[0]:
            self.bot.send_message(msg.chat.id, answer.CHOICE_REPEAT_OR_NEXT_GIVE_AWAY,
                                  reply_markup=get_keyboard_choice_repeat_or_next())
            self.bot.register_next_step_handler(msg, self.processing_repeat_or_next)
        elif msg.text.lower() == general.CHOICE_REPEAT[1]:
            self.bot.send_message(msg.chat.id, "Выберите что именно хотите отдать",
                                  reply_markup=get_keyboard_give_away())
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
            self.bot.send_message(msg.chat.id, answer.MSG_GIVE_AWAY,
                                  reply_markup=get_keyboard_give_away())
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
