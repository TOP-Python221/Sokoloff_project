from main import PLAYERS
# Заготовка на будущее для импортирования ботов с разной сложностью игры
#from easy_mode improt bot1(bot1 - easy mode)
#from hard_mode improt bot2((bot2 - hard mode))
from get_player_name import get_player_name

# ОТВЕТИТЬ: уверены, что стоит разносить функции game_mode() и get_difficultly_level() по разным модулям?
# аргументируйте решение
def get_difficultly_level():
    """Запрашивает у пользователя уровень сложности для игры с ботом."""
    level = input('Type difficult level of game(easy or hard)')
    if level == 'easy':
        # bot1()

        # ИСПОЛЬЗОВАТЬ: с ключевым словом pass вы сможете создавать пустые заготовки
        # блоков и при этом любым образом использовать все нужные вам файлы
        pass
    if level == 'hard':
        # bot2()
        pass


# ИСПРАВИТЬ: согласно документации, функция должна именно запрашивать режим игры,
# а не принимать его в качестве параметра
# возврат значения этой ↯ функцией был убран в ходе обсуждения
def game_mode() -> None:
    """Запрашивает режим для новой партии, добавляет имя бота либо второго игрока в
    глобальную переменную текущих игроков, запрашивает очерёдность ходов."""
    global PLAYERS
    # stdin -> mode
    mode = input('Type game mode (single or double): ')
    # if mode == 'single':
    #     get_difficulty_level()
    if mode.lower() == 'single':
        get_difficultly_level()
    elif mode.lower() == 'double':
        # get_player_name()
        get_player_name()
        # ИСПОЛЬЗОВАТЬ: с ключевым словом pass вы сможете создавать пустые заготовки блоков и
        # при этом любым образом использовать все нужные вам файлы
        pass
    # who_is_cross = input('who is cross?: ')
    # name -> PLAYERS
game_mode()
