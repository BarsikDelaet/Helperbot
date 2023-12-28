from keyboards.give_away import keyboard


HELLO_INSIDE_GIVE_AWAY = """Выберите интересующий пункт"""

MSG_GIVE_AWAY = """Выберите что именно хотите отдать"""

CHOICE_REPEAT_OR_NEXT_GIVE_AWAY = """Вы молодец! Рад, если смог вам помочь. Может, хотите еще пообщаться?

В главное меню 
Советы о том, куда и как отдать ненужное
Могу дать случайный совет про любую тему
Хотите оставить отзыв?

Кстати, вы можете подписаться на канал Что может один человек. Пару раз в неделю вы будете получать веселые или серьезные советы, подсказки, идеи о том, что еще можно делать в городе созидательного."""

#ADDRESSES_IN_CITY = f"""Вот что я смог найти в г.{msg.text}
#{result[0]}
#{result[1]}
#{result[2]}
#Можете поискать ещё информацию сами."""

ADDRESS_NOT_FOUND = """Адресса не найдены, проверть корректность введеного названия города
Либо можете попробовать поискать сами)

Можем поискать ещё, в каком городе ищем?"""

ITEM_BOOK_PEOPLE = "книг"
ITEM_CLOTHING_KIDS = "одежды"
ITEM_TECHNIC = "бытовой%20техники"
ITEM_TOYS = "игрушек"

BOOK_PEOPLE = {
    keyboard.CHOICE_BOOK[0]: "В каком вы городе?",
    keyboard.CHOICE_BOOK[1]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_BOOK[2]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_BOOK[3]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_BOOK[4]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_BOOK[5]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_BOOK[6]: "Фото/Текст/Документы(чек-лист)"
}

CLOTHING_KIDS = {
    keyboard.CHOICE_CLOTHING[0]: "В каком вы городе?",
    keyboard.CHOICE_CLOTHING[1]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_CLOTHING[2]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_CLOTHING[3]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_CLOTHING[4]: "Фото/Текст/Документы(чек-лист)"
}

TECHNIC = {
    keyboard.CHOICE_TECHNIC[0]: "В каком вы городе?",
    keyboard.CHOICE_TECHNIC[1]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_TECHNIC[2]: "Фото/Текст/Документы(чек-лист)",
    keyboard.CHOICE_TECHNIC[3]: "Фото/Текст/Документы(чек-лист)"
}

TOYS = {
    keyboard.CHOICE_TOYS[0]: "В каком вы городе?",
    keyboard.CHOICE_TOYS[1]: "Фото/Текст/Документы(чек-лист)И",
    keyboard.CHOICE_TOYS[2]: "Фото/Текст/Документы(чек-лист)И",
    keyboard.CHOICE_TOYS[3]: "Фото/Текст/Документы(чек-лист)И",
    keyboard.CHOICE_TOYS[4]: "Фото/Текст/Документы(чек-лист)И"
}
