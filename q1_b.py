import math


def f(x: float, ) -> float:
    return x * math.sin(x)


def three_point_backward_f_prime(
    x: float,
    h: float,
) -> float:
    """ Three-point backward f prime

    Args:
        x (float): x
        h (float): h

    Returns:
        float: f'(x)
    """

    return (f(x - 2 * h) - 4 * f(x - h) + 3 * f(x)) / (2 * h)


def three_point_forward_f_prime(
    x: float,
    h: float,
) -> float:
    """ Three-point forward f prime

    Args:
        x (float): x
        h (float): h

    Returns:
        float: f'(x)
    """

    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)


def four_point_backward_f_double_prime(
    x: float,
    h: float,
) -> float:
    """ Four-point backward f double prime

    Args:
        x (float): x
        h (float): h

    Returns:
        float: f''(x)
    """

    return (-f(x - 3 * h) + 4 * f(x - 2 * h) - 5 * f(x - h) + 2 * f(x)) / (h**
                                                                           2)


def four_point_forward_f_double_prime(
    x: float,
    h: float,
) -> float:
    """ Four-point forward f double prime

    Args:
        x (float): x
        h (float): h

    Returns:
        float: f''(x)
    """

    return (2 * f(x) - 5 * f(x + h) + 4 * f(x + 2 * h) - f(x + 3 * h)) / (h**2)


if __name__ == "__main__":
    h = 0.1

    x = 1.0
    print(
        f"Value of 3-point forward f'(x) at x = {x} is {three_point_forward_f_prime(x=x, h=h,)}"
    )
    print(
        f"Value of 4-point forward f''(x) at x = {x} is {four_point_forward_f_double_prime(x=x, h=h,)}"
    )

    x = 2.0
    print(
        f"Value of 3-point backward f'(x) at x = {x} is {three_point_backward_f_prime(x=x, h=h,)}"
    )
    print(
        f"Value of 4-point backward f''(x) at x = {x} is {four_point_backward_f_double_prime(x=x, h=h,)}"
    )
