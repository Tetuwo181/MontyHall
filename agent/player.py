from typing import Callable
from random import randint
from game.monty_hall import MontyHall
from agent import strategy as st


class Player(object):
    def __init__(self, strategy):
        """
        初期化
        :param strategy: 箱を一度選んだ後どうするかという戦略 1番目の引数に選んだ番号,２番目の引数に司会者が明けた番号,3番目に箱の総数を入れる
        """
        self.__profit = 0
        self.__iteration_num = 0
        self.__strategy = strategy

    @property
    def ave_profit(self):
        if self.__iteration_num == 0:
            return 0
        return float(self.__profit/self.__iteration_num)

    @property
    def strategy(self):
        return self.__strategy

    def bet(self, game: MontyHall = MontyHall()):
        """
        モンティホール問題を行う
        :param game:ゲームを行うクラス
        :return:
        """
        first_chosen_number = randint(0, game.box_num)
        other_loser = game.show_other(first_chosen_number)
        chosen_number = self.strategy(first_chosen_number, other_loser, game.box_num)
        if game.game(chosen_number):
            self.__profit = self.__profit + 1
        self.__iteration_num = self.__iteration_num + 1

