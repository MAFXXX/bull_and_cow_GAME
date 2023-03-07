from tkinter import *
from tkinter.dialog import *
from random import choice
import mini_engine
from mini_engine import *

attempts = 0
time = 0

def play(event):
    global attempts, time
    if mini_engine.random_number == 0:
        mystery_number()
        msg2.config(text='')
    attempts = analysis_of_attempts()
    input_number = ent.get()
    a_input_number = input_number
    bull, cow = take_from_number(a_input_number)
    msg2.config(text=msg2.cget('text') + str(attempts) + '. Ваше число: ' + input_number + ' содержит ' +
                     str(bull) + ' быка и ' + str(cow) + ' корову/коров.\n')
    ent.delete(0, END)
    if bull == 4:  # В случае победы,
        gameOwer = Dialog(title='Вы победили за ' + str(attempts) + ' хода/ходов; ',
                          text='     Сыграем ещё?           ',
                          bitmap='questhead',
                          default=0,
                          strings=('Да', 'Нет'))
        if gameOwer.num == 1: exit()  # Закончить игру
        attempts = 0  # Очистить счётчик ходов
        mini_engine.random_number = ''  # Очистить строку x для случайного числа
        msg2.config(text='Бык - цифра на своём месте.\n'
                         'Корова - цифра не на своём месте.')  # Выводим правила игры в окно сообщений


window = Tk()                                       # Создаём окно пиложения
window.geometry('1280x600')                          # Задаём размер окна пиложения в пикселях
window.title('Быки и Коровы (by MAF)')               # Название программы в заголовке окна

msg = Message(width=500, padx=30, pady=10,
              text='Введите число от 1023 до 9876 '
              'такое, чтобы цифры, составляющие это число,'
              ' не повторялись!')
msg.pack(padx=15, pady=5)                                                   # Размещаем окно сообщений в окне tk
msg.config(bg="light grey", fg='blue', font=('times', 16, 'italic'))        # Параметры для msg

ent = Entry(width=5)                            # Создаём поле ввода
ent.pack()                                      # Размещаем поле ввода в окне tk
ent.focus()                                     # Поместить фокус в поле ввода
ent.bind('<Return>', play)

msg2 = Message(width=400, padx=10, pady=5,
              text='Бык - цифра на своём месте.\n'
               'Корова - цифра не на своём месте.')     # Создаём окно сообщений
msg2.pack(padx=10, pady=5)                      # Размещаем окно сообщений в окне tk
msg2.config(fg='gray', font=('times', 12, 'normal'))       # Параметры для msg

mainloop()                                      # Цикл ожидания событий