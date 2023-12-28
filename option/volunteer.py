"""Раздел Волонтер и Донор
Все инструкции по этому вопросу."""

from option import answer
from keyboards import keyboard_menu
from option.service import Service
from option.inside_volunteer.blood_donor import BloodDonor
from option.inside_volunteer.bone_marrow_donor import BoneMarrowDonor
from option.inside_volunteer.volunteer_online import VolunteerOnline
from option.inside_volunteer.volunteer_offline import VolunteerOffline
from keyboards.volunteer.for_volunteer import get_keyboard_volunteer


class Volunteer(Service):

    """Создание и обработка всех кнопок раздела."""
    def menu_volunteer(self, msg):
        """Меню с конпками."""
        self.bot.send_message(msg.chat.id, answer.HELLO_VOLUNTEER,
                              reply_markup=get_keyboard_volunteer())
        self.bot.register_next_step_handler(msg, self.choice_volunteer)

    def choice_volunteer(self, msg):
        """Обрабатывает выбранный пункт и отправляет соответствующую информацию.
        Донор крови/Дноро костного мозга/Волонтер офлайн/Волонтер онлайн/Обработка не кнопки"""
        text_msg = msg.text.lower()
        if text_msg == keyboard_menu.CHOICE_VOLUNTEER[0]:  # Донор крови
            info = BloodDonor(self.bot)
            info.menu_blood_donor(msg)

        elif text_msg == keyboard_menu.CHOICE_VOLUNTEER[1]:  # Дноро костного мозга
            info = BoneMarrowDonor(self.bot)
            info.menu_bone_marrow_donor(msg)

        elif text_msg == keyboard_menu.CHOICE_VOLUNTEER[2]:  # Волонтер офлайн
            info = VolunteerOffline(self.bot)
            info.menu_volunteer_offline(msg)

        elif text_msg == keyboard_menu.CHOICE_VOLUNTEER[3]:  # Волонтер онлайн
            info = VolunteerOnline(self.bot)
            info.menu_volunteer_online(msg)

        else:  # Обработка не кнопки
            self.bot.send_message(msg.chat.id, answer.UNDERSTAND_MSG)
            self.bot.register_next_step_handler(msg, self.choice_volunteer)

