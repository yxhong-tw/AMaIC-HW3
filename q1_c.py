import math

from q1_a import two_point_central_f_prime, three_point_central_f_double_prime
from q1_b import three_point_backward_f_prime, three_point_forward_f_prime, \
    four_point_backward_f_double_prime, four_point_forward_f_double_prime


def G(
    g1: float,
    g2: float,
    p: float,
) -> float:
    return (((2**p) * g2) - g1) / (2**p - 1)


def exact_f_prime(x: float, ) -> float:
    return math.sin(x) + x * math.cos(x)


def exact_f_double_prime(x: float, ) -> float:
    return 2 * math.cos(x) - x * math.sin(x)


if __name__ == "__main__":
    h1 = 0.4
    h2 = 0.2
    p = 2

    x = 1.6
    g1 = two_point_central_f_prime(
        x=x,
        h=h1,
    )
    g2 = two_point_central_f_prime(
        x=x,
        h=h2,
    )
    print(
        f"Value of more accurate f'(x) at x = {x} is {G(g1=g1, g2=g2, p=p,)}")
    print(f"Value of exact f'(x) at x = {x} is {exact_f_prime(x=x,)}")

    g1 = three_point_central_f_double_prime(
        x=x,
        h=h1,
    )
    g2 = three_point_central_f_double_prime(
        x=x,
        h=h2,
    )
    print(
        f"Value of more accurate f''(x) at x = {x} is {G(g1=g1, g2=g2, p=p,)}")
    print(f"Value of exact f''(x) at x = {x} is {exact_f_double_prime(x=x,)}")

    x = 1.0
    g1 = three_point_forward_f_prime(
        x=x,
        h=h1,
    )
    g2 = three_point_forward_f_prime(
        x=x,
        h=h2,
    )
    print(
        f"Value of more accurate 3-point forward f'(x) at x = {x} is {G(g1=g1, g2=g2, p=p,)}"
    )
    print(f"Value of exact f'(x) at x = {x} is {exact_f_prime(x=x,)}")

    g1 = four_point_forward_f_double_prime(
        x=x,
        h=h1,
    )
    g2 = four_point_forward_f_double_prime(
        x=x,
        h=h2,
    )
    print(
        f"Value of more accurate 3-point forward f''(x) at x = {x} is {G(g1=g1, g2=g2, p=p,)}"
    )
    print(f"Value of exact f''(x) at x = {x} is {exact_f_double_prime(x=x,)}")

    x = 2.0
    g1 = three_point_backward_f_prime(
        x=x,
        h=h1,
    )
    g2 = three_point_backward_f_prime(
        x=x,
        h=h2,
    )
    print(
        f"Value of more accurate 3-point backward f'(x) at x = {x} is {G(g1=g1, g2=g2, p=p,)}"
    )
    print(f"Value of exact f'(x) at x = {x} is {exact_f_prime(x=x,)}")

    g1 = four_point_backward_f_double_prime(
        x=x,
        h=h1,
    )
    g2 = four_point_backward_f_double_prime(
        x=x,
        h=h2,
    )
    print(
        f"Value of more accurate 3-point backward f''(x) at x = {x} is {G(g1=g1, g2=g2, p=p,)}"
    )
    print(f"Value of exact f''(x) at x = {x} is {exact_f_double_prime(x=x,)}")
