import random


def print_apples_place(apples):
    # Вывод игрового поля
    apples_place = ''
    for i in range(len(apples)):
        apples_place += str(i + 1) + '. ' + apples[i] + ' | '

    print(apples_place)
    print('\n')


def get_flag_repeat():
    # Продолжить или закончить игру?
    repeat = int(input('Желаете продолжить? 1 - Да, 2 - Нет:'))
    if type(repeat) is int:
        if 0 > repeat > 2:
            print('Ошибка: Некорректный ввод')
            get_flag_repeat()

        else:
            return repeat


def print_win_text(player_score, level):
    # Вывод текста, если пользователь выиграл
    print('Вы угадали!')
    print('Вам начислено 10 очков')
    print(f'Ваш текущий уровень: {level}. Ваш текущий счет: {player_score}')


def print_lose_text(player_score, level):
    # Вывод текста, если пользователь проиграл
    print('Вы не угадали!')
    print('К сожалению вы проиграли!')
    print(f'Ваш уровень: {level}. Ваш счет составил: {player_score}')


def get_player_choose():
    # Выбор одного из полей
    print('\nВыберете одно число из 6')
    choose = int(input('Введите число: '))\

    if type(choose) is int:
        if 6 < choose < 0:
            print('Ошибка: был совершен некорректный ввод')
            get_player_choose()
        else:
            return choose - 1


def instruction():
    # Вывод инструкции как играть
    print('''
Игроку дается выбор: любое число от 1 до 6.
Главная задача угадать где находится яблоко, иначе игрок проиграет.
За выигрыш в раунде игроку начисляется 10 очков, умноженных на его уровень.
С каждым уровнем количество огрызков на игровом поле увеличивается на 1.
Если вы достигли 5 уровня, то на поле всегда будет только 1 яблоко.
Желаю удачи! :-)
''')
    main()


def get_index(count_spot_for_stub, apples):
    # Получения индекса куда можно вставить огрызок
    index = -1
    for i in range(count_spot_for_stub):
        index = random.randint(0, len(apples) - 1)

    return index


def play(player_score, level):
    # Процесс игры
    apples = ['Яблоко'] * 6
    stub = 'Огрызок'
    count_spot_for_stub = level
    count_inserted_stub = 0

    if level == 6:
        count_spot_for_stub = 5

    while count_inserted_stub != count_spot_for_stub:
        index_for_stub = get_index(count_spot_for_stub, apples)
        if apples[index_for_stub] != stub:
            apples[index_for_stub] = stub
            count_inserted_stub += 1

    choose = get_player_choose()
    if apples[choose] == 'Яблоко':
        player_score += 10 * level
        level += 1
        print_win_text(player_score, level)
        print_apples_place(apples)
        play(player_score, level)
    else:
        print_lose_text(player_score, level)
        print_apples_place(apples)
        repeat = get_flag_repeat()

        if repeat == 1:
            player_score = 0
            level = 1
            play(player_score, level)

        else:
            print('Игра окончена!\n\n')
            main()


def main():
    print('1.Играть')
    print('2.Как играть?')
    choose = int(input('Введите номер пункта: '))

    player_score = 0
    level = 1

    if choose == 1:
        play(player_score, level)
    elif choose == 2:
        print(instruction())


main()
