"""Раздел Ситуация в городе
Все инструкции по этому вопросу."""


from option import answer
from keyboards import keyboard_menu
from keyboards.city.for_city import get_keyboard_city
from option.service import Service
from option.inside_city.people_trouble import PeopleTrouble
from option.inside_city.animal_trouble import AnimalTrouble
from option.inside_city.ecological_problem import EcologicalProblem
from option.inside_city.feed_animals import FeedAnimals


class City(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_city(self, msg):
        """Меню с конпками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_CITY,
                              reply_markup=get_keyboard_city())
        self.bot.register_next_step_handler(msg, self.choice_city)

    def choice_city(self, msg):
        """Обрабатывает выбранный пункт и отправляет соответствующую информацию."""
        text_msg = msg.text.lower()
        if text_msg == keyboard_menu.CHOICE_CITY[0]:  # Человек в беде
            info = PeopleTrouble(self.bot)
            info.menu_people_trouble(msg)

        elif text_msg == keyboard_menu.CHOICE_CITY[1]:  # Животное в беде
            info = AnimalTrouble(self.bot)
            info.menu_animal_trouble(msg)

        elif text_msg == keyboard_menu.CHOICE_CITY[2]:  # Экологическая проблема
            info = EcologicalProblem(self.bot)
            info.menu_ecological_problem(msg)

        elif text_msg == keyboard_menu.CHOICE_CITY[3]:  # Чем кормить птиц/животных
            info = FeedAnimals(self.bot)
            info.menu_feed_animals(msg)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_city)
