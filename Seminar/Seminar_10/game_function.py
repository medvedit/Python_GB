from random import randint
from time import sleep
import enum
import emoji


# SYMBOL_X = '❌'
# SYMBOL_O = '⭕'

class Order(enum.Enum):
    '''кто ходит'''
    player = 0
    cpu = 1


class Game:
    help = (emoji.emojize('❌''⭕'))

    matrix: list  # Игровое поле
    game_status: bool  # состояние игры

    def __init__(self):
        self.game_status = False
        '''начальное состояние игры (остановлена)'''
        self.matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        '''Игровое поле'''
        self.act = Order.player
        '''чей ход: cpu/player'''

    def start(self):
        '''старт игры'''
        self.game_status = True
        self.matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def stop(self):
        '''остановка игры'''
        self.game_status = False

    def action_player(self, num_position):
        ''' ход игрока
        Args: num_position (int): номер позиции в игровом поле, куда игрок поставил знак "Х" '''
        if self.game_status:

            '''игрок сделал ход'''
            if (self.matrix[num_position-1] != 'X') and (self.matrix[num_position-1] != '0'):
                self.matrix[num_position-1] = 'X'
                return
        else:
            pass



    def action_cpu(self):
        '''ход компьютера
        Returns:
            int : позиция, на которую компьютер поставил знак "О" '''
        if self.game_status:
            for i in range(0,len(self.matrix)):
                i = randint(0, 8)
                if (self.matrix[i] != 'X') and (self.matrix[i] != '0'):
                    self.matrix[i] = '0'
                    return
        else:
            return 0


    def check_game_state(self):
        ''' Проверка победителя '''
        while True:
            if self.matrix[0] == self.matrix[1] == self.matrix[2]:
                return f'Победили {self.matrix[0]}'
            elif self.matrix[3] == self.matrix[4] == self.matrix[5]:
                return f'Победили {self.matrix[3]}'
            elif self.matrix[6] == self.matrix[7] == self.matrix[8]:
                return f'Победили {self.matrix[6]}'
            elif self.matrix[0] == self.matrix[3] == self.matrix[6]:
                return f'Победили {self.matrix[0]}'
            elif self.matrix[1] == self.matrix[4] == self.matrix[7]:
                return f'Победили {self.matrix[1]}'
            elif self.matrix[2] == self.matrix[5] == self.matrix[8]:
                return f'Победили {self.matrix[2]}'
            elif self.matrix[0] == self.matrix[4] == self.matrix[8]:
                return f'Победили {self.matrix[0]}'
            elif self.matrix[2] == self.matrix[4] == self.matrix[6]:
                return f'Победили {self.matrix[2]}'
            else: return False


    def check_drawn_game(self):
        ''' Проверка ничьей '''
        if len(set(self.matrix)) == 2:
            return True



    def showMatrix(self):
        return  f'|  {self.matrix[0]}  |  {self.matrix[1]}  |  {self.matrix[2]}  |\n'\
                f'|  {self.matrix[3]}  |  {self.matrix[4]}  |  {self.matrix[5]}  |\n'\
                f'|  {self.matrix[6]}  |  {self.matrix[7]}  |  {self.matrix[8]}  |\n'

