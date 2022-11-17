""" Модуль бота """

from random import random

from telebot import *

from data import *

code = '5600321198:AAHVWmPCagBxmo102LW6EMUR8wTnguzphoY'
bot = TeleBot(code)

Vectors = {}
Points = {}


@bot.message_handler(commands=["start"])
def start(message, res=False):
    """ Функция, обрабатывающая команду /start """
    bot.send_message(message.chat.id, Base.start_message_1)
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.main_menu_actions])
    bot.send_message(message.chat.id, Base.choose_action, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    """ Функция обрабатывающая текстовые сообщения """
    if message.text.strip() == Base.main_menu_actions[0]:
        add_choose(message)
    elif message.text.strip() == Base.main_menu_actions[1]:
        operation_choose(message)


def main_menu(message):
    """ Основное меню бота """
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.main_menu_actions])
    bot.send_message(message.chat.id, Base.choose_action, reply_markup=markup)


# ---------- === ADD === ----------
def add_choose(message):
    """ Меню выбора при добавлении объекта """
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.add_actions])
    bot.send_message(message.chat.id, Base.choose_action, reply_markup=markup)
    bot.register_next_step_handler(message, add_obj)


def add_obj(message):
    """ Функция  анализирует ответы пользователя в меню добавления объекта и запускает функции считывания """
    if message.text.strip() == Base.add_actions[0]:
        bot.send_message(message.chat.id, Base.read_vec, reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_vec)
    elif message.text.strip() == Base.add_actions[1]:
        bot.send_message(message.chat.id, Base.read_point, reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_point)
    elif message.text.strip() == Base.add_actions[2]:
        main_menu(message)
    else:
        add_choose(message)


def get_vec(message):
    """ Функция считывания и создания вектора """
    try:
        args = list(message.text.split())
        cords = map(int, args[:3])
        if len(args) > 3:
            name = args[3]
        else:
            name = random.choice(Base.names)
            Base.names = Base.names.replace(name, '')
        t.Vectors[name.upper()] = cords
        bot.send_message(message.chat.id, Base.read_vec_completed)
        bot.send_message(message.chat.id, str(t.Vectors))
        main_menu(message)

    except ValueError:
        bot.send_message(message.chat.id, Base.add_read_error_value)
        bot.register_next_step_handler(message, get_vec)


def get_point(message):
    """ Функция считывания и создания точки """
    try:
        args = list(message.text.split())
        cords = map(int, args[:3])
        if len(args) > 3:
            name = args[3]
        else:
            name = random.choice(Base.names)
            Base.names = Base.names.replace(name, '')
        t.Points[name.upper()] = cords
        bot.send_message(message.chat.id, str(Base.read_point_completed))
        bot.send_message(message.chat.id, str(t.Points))
        main_menu(message)

    except ValueError:
        bot.send_message(message.chat.id, Base.add_read_error_value)
        bot.register_next_step_handler(message, get_point)


# ------ === OPERATIONS === -------
def operation_choose(message):
    """ Меню выбора операции """
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.operations])
    bot.send_message(message.chat.id, Base.choose_action, reply_markup=markup)
    bot.register_next_step_handler(message, operations)


def operations(message):
    """ Функция  анализирует ответы пользователя в меню выбора и запускает функции решения задач """
    # if message.text.strip() == Base.operations[0]:
    #     if len(P.points) >= 2:
    #         bot.send_message(message.chat.id, Base.find_vec, reply_markup=types.ReplyKeyboardRemove())
    #         bot.send_message(message.chat.id, P.show())
    #         bot.register_next_step_handler(message, find_vec)
    #     else:
    #         bot.send_message(message.chat.id, Base.find_vec_error)
    #         add_choose(message)
    # elif message.text.strip() == Base.operations[1]:
    #     bot.send_message(message.chat.id, Base.read_expression, reply_markup=types.ReplyKeyboardRemove())
    #     bot.register_next_step_handler(message, read)
    # elif message.text.strip() == Base.operations[2]:
    #     bot.send_message(message.chat.id, Base.help, reply_markup=types.ReplyKeyboardRemove())
    #     operation_choose(message)
    # elif message.text.strip() == Base.operations[3]:
    #     main_menu(message)
    # else:
    #     operation_choose(message)
    pass


def find_vec(message):
    """ Функция нахождения и создания вектора """
    # try:
    #     points = message.text[:2].upper()
    #     a = P.points.get(points[0])
    #     b = P.points.get(points[1])
    #     vec = V.find(a, b)
    #     bot.send_message(message.chat.id, Base.find_vec_completed + vec.show())
    #     bot.send_message(message.chat.id, V.show() + P.show())
    #     operation_choose(message)
    # except ValueError:
    #     bot.send_message(message.chat.id, Base.find_vec_error_name)
    #     bot.register_next_step_handler(message, find_vec)
    pass


def read(message):
    """ Функция считывания выражения """
    try:
        m = message.text.strip()
        c = eval(m)
        c.change_name('c')
        bot.send_message(message.chat.id, c.show)
    except Any:
        main_menu(message)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
