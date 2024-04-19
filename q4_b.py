import numpy as np


def f(
    x: float,
    y: float,
    z: float,
) -> float:
    return 2 * (x**2) + 3 * (y**2) - z


def trilinear_interpolation(
    x: float,
    y: float,
    z: float,
    x_grid: np.ndarray,
    y_grid: np.ndarray,
    z_grid: np.ndarray,
    f_table: np.ndarray,
) -> float:
    x_index = np.searchsorted(a=x_grid, v=x) - 1
    y_index = np.searchsorted(a=y_grid, v=y) - 1
    z_index = np.searchsorted(a=z_grid, v=z) - 1

    x_bias = (x - x_grid[x_index]) / (x_grid[x_index + 1] - x_grid[x_index])
    y_bias = (y - y_grid[y_index]) / (y_grid[y_index + 1] - y_grid[y_index])
    z_bias = (z - z_grid[z_index]) / (z_grid[z_index + 1] - z_grid[z_index])

    c000 = f_table[x_index, y_index, z_index]
    c001 = f_table[x_index, y_index, z_index + 1]
    c010 = f_table[x_index, y_index + 1, z_index]
    c011 = f_table[x_index, y_index + 1, z_index + 1]
    c100 = f_table[x_index + 1, y_index, z_index]
    c101 = f_table[x_index + 1, y_index, z_index + 1]
    c110 = f_table[x_index + 1, y_index + 1, z_index]
    c111 = f_table[x_index + 1, y_index + 1, z_index + 1]

    c00 = c000 * (1 - x_bias) + c100 * x_bias
    c01 = c001 * (1 - x_bias) + c101 * x_bias
    c10 = c010 * (1 - x_bias) + c110 * x_bias
    c11 = c011 * (1 - x_bias) + c111 * x_bias

    c0 = c00 * (1 - y_bias) + c10 * y_bias
    c1 = c01 * (1 - y_bias) + c11 * y_bias

    c = c0 * (1 - z_bias) + c1 * z_bias

    return c


if __name__ == "__main__":
    x_grid = np.arange(6)
    y_grid = np.arange(6)
    z_grid = np.arange(6)

    f_table = np.zeros((6, 6, 6))
    for i, x in enumerate(x_grid):
        for j, y in enumerate(y_grid):
            for k, z in enumerate(z_grid):
                f_table[i, j, k] = f(x, y, z)

    x = input("Enter x: ")
    y = input("Enter y: ")
    z = input("Enter z: ")
    print(
        f"Estimated value at ({x}, {y}, {z}) is: {trilinear_interpolation(x=x, y=y, z=z, x_grid=x_grid, y_grid=y_grid, z_grid=z_grid, f_table=f_table)}"
    )
