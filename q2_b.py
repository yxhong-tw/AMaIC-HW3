import numpy as np

from typing import List

from q1_a import f
from q1_c import exact_f_prime


def calculate_S_i_of_x(
    a_i: float,
    b_i: float,
    c_i: float,
    d_i: float,
    x: float,
    x_i: float,
) -> float:
    return a_i + b_i * (x - x_i) + c_i * (x - x_i)**2 + d_i * (x - x_i)**3


def calculate_S_i_prime_of_x(
    b_i: float,
    c_i: float,
    d_i: float,
    x: float,
    x_i: float,
) -> float:
    return b_i + 2 * c_i * (x - x_i) + 3 * d_i * (x - x_i)**2


def calculate_h_list(x_list: List[float]) -> List[float]:
    return [x_list[i] - x_list[i - 1] for i in range(1, len(x_list))]


def calculate_a_list(y_list: List[float]) -> List[float]:
    return y_list[:-1]


def calculate_c(x_list: List[float], y_list: List[float]):
    h_list = calculate_h_list(x_list=x_list)

    b_matrix = [[0 for _ in range(len(x_list))] for _ in range(len(x_list))]
    for i in range(1, len(x_list) - 1):
        b_matrix[i][i - 1] = h_list[i - 1]
        b_matrix[i][i] = 2 * (h_list[i - 1] + h_list[i])
        b_matrix[i][i + 1] = h_list[i]
    b_matrix[0][0] = 1
    b_matrix[-1][-1] = 1

    r_matrix = [0 for _ in range(len(x_list))]
    for i in range(1, len(x_list) - 1):
        r_matrix[i] = 3 * ((y_list[i + 1] - y_list[i]) / h_list[i] -
                           (y_list[i] - y_list[i - 1]) / h_list[i - 1])
    r_matrix[0] = 0
    r_matrix[-1] = 0

    return np.linalg.solve(b_matrix, r_matrix)


def calculate_b_list(x_list: List[float], y_list: List[float],
                     c_list: List[float], h_list: List[float]) -> List[float]:
    return [(y_list[i + 1] - y_list[i]) / h_list[i] - h_list[i] *
            (2 * c_list[i] + c_list[i + 1]) / 3
            for i in range(len(x_list) - 1)]


def calculate_d_list(x_list: List[float], c_list: List[float],
                     h_list: List[float]) -> List[float]:
    return [(c_list[i + 1] - c_list[i]) / (3 * h_list[i])
            for i in range(len(x_list) - 1)]


if __name__ == "__main__":
    x_list = [1.0, 1.32, 1.4, 1.55, 1.8]
    y_list = [f(x=x) for x in x_list]

    h_list = calculate_h_list(x_list=x_list)
    a_list = calculate_a_list(y_list=y_list)
    c_list = calculate_c(x_list=x_list, y_list=y_list)
    b_list = calculate_b_list(x_list=x_list,
                              y_list=y_list,
                              c_list=c_list,
                              h_list=h_list)
    d_list = calculate_d_list(x_list=x_list, c_list=c_list, h_list=h_list)

    x = 1.5
    x_i = None
    x_i_index = None
    for i in range(1, len(x_list)):
        if x_list[i - 1] <= x <= x_list[i]:
            x_i = x_list[i - 1]
            x_i_index = i - 1
            break

    S_i_prime_of_x = calculate_S_i_prime_of_x(
        b_i=b_list[x_i_index],
        c_i=c_list[x_i_index],
        d_i=d_list[x_i_index],
        x=x,
        x_i=x_i,
    )

    print(f"Value of f'(x) at x = {x} is {S_i_prime_of_x}")
    print(f"Value of exact f'(x) at x = {x} is {exact_f_prime(x=x,)}")
