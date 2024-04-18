import math


def f(x: float, ) -> float:
    return x * math.sin(x)


def two_point_central_f_prime(
    x: float,
    h: float,
) -> float:
    """ Two-point central f prime

    Args:
        x (float): x
        h (float): h

    Returns:
        float: f'(x)
    """

    return (f(x + h) - f(x - h)) / (2 * h)


def three_point_central_f_double_prime(
    x: float,
    h: float,
) -> float:
    """ Three-point central f double prime

    Args:
        x (float): x
        h (float): h

    Returns:
        float: f''(x)
    """

    return (f(x - h) - 2 * f(x) + f(x + h)) / (h**2)


if __name__ == "__main__":
    x = 1.6
    h = 0.1

    print(
        f"Value of f'(x) at x = {x} is {two_point_central_f_prime(x=x, h=h,)}")
    print(
        f"Value of f''(x) at x = {x} is {three_point_central_f_double_prime(x=x, h=h,)}"
    )
