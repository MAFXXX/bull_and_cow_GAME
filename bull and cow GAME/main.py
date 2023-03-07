from mini_engine import take_from_number, mystery_number, analysis_of_attempts, game_over

mystery_number()
while True:
    attempts = analysis_of_attempts()
    input_number = input('Введите четырехзначное число:')
    a_input_number = input_number
    bull, cow = take_from_number(a_input_number)
    print(input_number, 'содержит', bull, 'быка и', cow, 'корову/коровы.')
    if game_over(bull):
        print('Молодец! Угадал за', attempts, 'попытки/ок')
        break