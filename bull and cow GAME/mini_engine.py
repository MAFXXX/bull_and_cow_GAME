'''Мини движок игры Бык и Корова'''
from tkinter import *
from random import choice

random_number = 0
attempts = 0

def mystery_number():
    '''Компьютер загадывает число'''
    global random_number
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x_number = []
    temp = 0
    while len(x_number) != 4:
        temp_number = choice(number)
        x_number.append(temp_number)
        if x_number[0] == '0':
            x_number.remove('0')
            continue
        number.remove(x_number[temp])
        temp += 1
        # print(x_number)
        # print(number)
    random_number = "".join(x_number)
    # print(random_number)

def take_from_number(x):
    '''Анализ числа'''
    bull = 0; cow = 0
    for i in range(4):
        if x[i] == random_number[i]:
            bull += 1
        elif random_number[i] in x:
            cow += 1
    # print(x, 'содержит', bull, 'быка и', cow, 'корову/коровы.')
    return bull, cow



def analysis_of_attempts():
    global attempts
    attempts += 1
    return attempts

def game_over(bull):
    if bull == 4:
        return True



