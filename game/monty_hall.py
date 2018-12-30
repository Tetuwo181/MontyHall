import numpy as np


class MontyHall(object):
    def __init__(self, box_num: int = 3, game_num: int = 1000):
        """
        コンストラクタ
        :param box_num: 箱の数
        :param iteration_num: 試行回数：この回数分だけ当たりとなる回数を生成
        """
        self.__winning_number_set = np.random.randint(0, box_num, game_num)
        self.__number_set = np.arange(box_num)
        self.__iteration_num = 0

    @property
    def box_num(self):
        return len(self.__number_set)

    @property
    def __winning_number(self):
        """
        プロパティだけど政界を外部からアクセスされたくないので
        :return: その時点での正解となるナンバー
        """
        return self.__winning_number_set[self.__iteration_num]

    @property
    def game_num(self):
        return len(self.__winning_number_set)

    def show_other(self, chosen_number: int):
        """
        選んだ番号に対して外れとなる値を表示
        :param chosen_number:挑戦者が選んだ値
        :return:外れとなる箱の1つ
        """
        loser_number_set = np.array([number for number in self.__number_set
                                     if (number != self.__winning_number and number != chosen_number) ])
        return np.random.choice(loser_number_set)

    def game(self, choice_number: int)->bool:
        """
        実際に箱を開ける
        :param choice_number: 選んだ番号
        :return: 選んだ番号が当たりかどうか
        """
        try:
            return choice_number == self.__winning_number
        finally:
            if self.__iteration_num > len(self.__winning_number_set) - 2:
                self.__iteration_num = 0
            else:
                self.__iteration_num = self.__iteration_num + 1


