from q1_a import f
from q1_c import exact_f_prime


def lagrange_f_prime(x, y, z, a):
    return ((f(x=x) * (2*a - y - z) / ((x - y) * (x - z))) + \
            (f(x=y) * (2*a - x - z) / ((y - x) * (y - z))) + \
            (f(x=z) * (2*a - x - y) / ((z - x) * (z - y))))


if __name__ == "__main__":
    x = 1.32
    y = 1.4
    z = 1.55
    a = 1.5

    print(
        f"Value of f'(x) at x = {a} is {lagrange_f_prime(x=x, y=y, z=z, a=a,)}"
    )
    print(f"Value of exact f'(x) at x = {a} is {exact_f_prime(x=a,)}")
