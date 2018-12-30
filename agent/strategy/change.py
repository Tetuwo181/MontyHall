import numpy as np


def change(chosen_number: int, other_loser_number: int, box_num: int):
    """
    箱を変えない戦略
    :param chosen_number: 初めに選んだ箱
    :param other_loser_number: 残った箱で外れのほうの箱
    :param box_num:箱の数
    :return:
    """
    box_set = np.array([number for number in range(box_num)
                        if (number != chosen_number) and (number != other_loser_number)])
    return np.random.choice(box_set)

