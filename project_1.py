def output_print(some_dict):
    """
    This function prints the game field.
    """

    for k, v in sorted(some_dict.items()):
        if int(k) < 3 or 3 < int(k) <= 5 or 6 < int(k) < 9:
            print(f'{"|":<2}{v}{"":>1}', end='')
        else:
            print(f'{"|":<2}{v}{"|":>2}')


def is_victory_or_draw(some_dict, moves):
    """
    This function checks the game status.
    """

    if (some_dict['1'] == some_dict['2'] == some_dict['3'] or
            some_dict['4'] == some_dict['5'] == some_dict['6'] or
            some_dict['7'] == some_dict['8'] == some_dict['9'] or
            some_dict['1'] == some_dict['4'] == some_dict['7'] or
            some_dict['2'] == some_dict['5'] == some_dict['8'] or
            some_dict['3'] == some_dict['6'] == some_dict['9'] or
            some_dict['1'] == some_dict['5'] == some_dict['9'] or
            some_dict['3'] == some_dict['5'] == some_dict['7']):
        return f'\33[32mПобеда за игроком: {moves}\33[0m'
    elif len(set(check_user_enter)) == 1:
        return f'\33[32mНичья!\33[0m'


def game(output_game, check_user_enter_game):
    """
    This function executes the game process.
    """

    first = 'X'
    second = 'O'
    print('Игра крестики нолики!')
    print('В игре участвуют два игрока.')
    first_player = input('Введите имя первого игрока: ')
    print(f'\33[31m{first_player} будет ходить "{first}"\33[0m')
    second_player = input('Введите имя второго игрока: ')
    print(f'\33[34m{second_player} будет ходить "{second}"\33[0m')
    who_moves = first_player
    while True:
        print(f'Игровая сетка:')
        output_print(output_game)
        if who_moves == first_player:
            print(f'\33[31mСейчас ходит {who_moves}\33[0m')
        else:
            print(f'\33[34mСейчас ходит {who_moves}\33[0m')

        user_enter = input('Введите цифрой от 1 до 9 - позицию Вашего хода согласно игровой сетке: ')
        if user_enter not in check_user_enter_game:
            print('\33[31m!!!\33[0m Ошибка ввода \33[31m!!!\33[0m\n'
                  'Введите цифрой от 1 до 9 - позицию Вашего хода согласно игровой сетке: ')
        else:
            if who_moves == first_player:
                output_game[user_enter] = f'\33[31m{first}\33[0m'
                check_user_enter_game[int(user_enter) - 1] = False
                if is_victory_or_draw(output_game, who_moves):
                    print(is_victory_or_draw(output_game, who_moves))
                    break
                who_moves = second_player
            else:
                output_game[user_enter] = f'\33[34m{second}\33[0m'
                check_user_enter_game[int(user_enter) - 1] = False
                if is_victory_or_draw(output_game, who_moves):
                    print(is_victory_or_draw(output_game, who_moves))
                    break
                who_moves = first_player


def stat_game():
    """
    This function start the game.
    """

    while True:
        print('Начать игру крестики нолики?')
        play = input('Для старта игры введите "да", для завершения - "нет": ')
        if play == 'да':
            output = {
                '9': '9', '8': '8', '7': '7',
                '4': '4', '5': '5', '6': '6',
                '1': '1', '2': '2', '3': '3',
            }
            check_user_enter = [str(i) for i in range(1, 10)]
            game(output, check_user_enter)
        elif play == 'нет':
            print('До свидания!')
            break
        else:
            print('Вы ввели что-то не то!')
            continue


stat_game()
