"""Раздел <<Отдать что-то ненужное>>
Все инструкции по этому вопросу."""


from option import answer
from keyboards import keyboard_menu
from option.service import Service
from option.inside_give_away.clothing_kids import ClothingKids
from option.inside_give_away.toys import Toys
from option.inside_give_away.technic import Technic
from option.inside_give_away.book_people import BookPeople
from keyboards.give_away.for_give_away import get_keyboard_give_away


class GiveAway(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_give_away(self, msg):
        """Меню с конпками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_GIVE_AWAY,
                              reply_markup=get_keyboard_give_away())
        self.bot.register_next_step_handler(msg, self.choice_give_away)

    def choice_give_away(self, msg):
        """Обрабатывает выбранный пункт и отправляет соответствующую информацию.
        Одежда/Игрушки/Техника/Книги/Обработка не кнопки"""
        text_msg = msg.text.lower()
        if text_msg == keyboard_menu.CHOICE_GIVE_AWAY[0]:  # Одежда
            info = ClothingKids(self.bot)
            info.menu_clothing_kids(msg)

        elif text_msg == keyboard_menu.CHOICE_GIVE_AWAY[1]:  # Игрушки
            info = Toys(self.bot)
            info.menu_toys(msg)

        elif text_msg == keyboard_menu.CHOICE_GIVE_AWAY[2]:  # Техника
            info = Technic(self.bot)
            info.menu_technic(msg)

        elif text_msg == keyboard_menu.CHOICE_GIVE_AWAY[3]:  # Книги
            info = BookPeople(self.bot)
            info.menu_book_people(msg)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_give_away)
