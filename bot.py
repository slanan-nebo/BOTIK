from random import random

import telebot
from telebot import *

from data import *

code = '5600321198:AAHVWmPCagBxmo102LW6EMUR8wTnguzphoY'
bot = telebot.TeleBot(code)
V = Vectors()
P = Points()


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, Base.start_message_1)
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.start_actions])
    bot.send_message(message.chat.id, Base.start_message_2, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == Base.start_actions[0]:
        add_choose(message)
    elif message.text.strip() == Base.start_actions[1]:
        operation_choose(message)


def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.start_actions])
    bot.send_message(message.chat.id, Base.start_message_2, reply_markup=markup)


def add_choose(message):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.add_actions])
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, add_obj)


def operation_choose(message):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row(*[i for i in Base.operations])
    bot.send_message(message.chat.id, "Выберите возможные операции из перечня",
                     reply_markup=markup)
    bot.register_next_step_handler(message, operations)


def operations(message):
    if message.text.strip() == Base.operations[0]:
        if len(P.points) > 2:
            bot.send_message(message.chat.id, "Выберите координаты начала и конца вектора и запишите их без пробелов",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, P.show())
            bot.register_next_step_handler(message, find_vec)
        else:
            bot.send_message(message.chat.id, "Сначала добавьте точки")
            add_choose(message)
    elif message.text.strip() == Base.operations[1]:
        bot.send_message(message.chat.id, "Введите выражение",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, read)
    elif message.text.strip() == Base.operations[2]:
        bot.send_message(message.chat.id, Base.help, reply_markup=types.ReplyKeyboardRemove())
        operation_choose(message)
    elif message.text.strip() == Base.operations[3]:
        main_menu(message)


def add_obj(message):
    if message.text.strip() == Base.add_actions[0]:
        bot.send_message(message.chat.id, "Введите координаты вектора через пробел и его название",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_vec)
    elif message.text.strip() == Base.add_actions[1]:
        bot.send_message(message.chat.id, "Введите координаты точки через пробел и её название",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_point)
    elif message.text.strip() == Base.add_actions[2]:
        main_menu(message)


def get_vec(message):
    try:
        args = list(message.text.split())
        cords = map(int, args[:3])
        if len(args) > 3:
            vec = Vector(*cords, args[3])
        else:
            vec = Vector(*cords, 'a')
        V.add_vec(vec)
        bot.send_message(message.chat.id, "Вектор создан")
        bot.send_message(message.chat.id, V.show() + P.show())
        main_menu(message)

    except ValueError:
        bot.send_message(message.chat.id, Base.error_value)
        bot.register_next_step_handler(message, get_vec)


def get_point(message):
    try:
        args = list(message.text.split())
        cords = map(int, args[:3])
        if len(args) > 3:
            name = args[3]
        else:
            name = random.choice(Base.names)
            Base.names = Base.names.replace(name, '')
            print(Base.names)
        point = Point(*cords, name)
        P.add_point(point)
        bot.send_message(message.chat.id, "Точка создана")
        bot.send_message(message.chat.id, V.show() + P.show())
        main_menu(message)

    except ValueError:
        bot.send_message(message.chat.id, Base.error_value)
        bot.register_next_step_handler(message, get_point)


def find_vec(message):
    try:
        points = message.text[:2].upper()
        a = P.points.get(points[0])
        b = P.points.get(points[1])
        vec = V.find(a, b)
        bot.send_message(message.chat.id, "Вектор найден: " + vec.show())
        bot.send_message(message.chat.id, V.show() + P.show())
        operation_choose(message)
    except ValueError:
        bot.send_message(message.chat.id, "Введите названия двух точек без пробелов: AB")
        bot.register_next_step_handler(message, find_vec)


def read(message):
    bot.send_message(message.chat.id, "Пока недоступно")
    operation_choose(message)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
