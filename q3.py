import numpy as np


def bicubic_interpolation(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    p: np.ndarray,
) -> float:
    xn = p[0]
    yn = p[1]

    x_index = np.searchsorted(a=x, v=xn) - 1
    y_index = np.searchsorted(a=y, v=yn) - 1

    x_bias = (xn - x[x_index]) / (x[x_index + 1] - x[x_index])
    y_bias = (yn - y[y_index]) / (y[y_index + 1] - y[y_index])

    c00 = z[x_index, y_index]
    c01 = z[x_index, y_index + 1]
    c10 = z[x_index + 1, y_index]
    c11 = z[x_index + 1, y_index + 1]

    c0 = c00 * (1 - x_bias) + c01 * x_bias
    c1 = c10 * (1 - x_bias) + c11 * x_bias

    c = c0 * (1 - y_bias) + c1 * y_bias

    return c


def bilinear_interpolation(x, y, z, p):
    xn = p[0]
    yn = p[1]

    if xn < x[0] or xn > x[-1] or yn < y[0] or yn > y[-1]:
        print("Out of range!")
        return

    for i in range(1, len(x)):
        if x[i] > xn:
            indx = i
            break

    for i in range(1, len(y)):
        if y[i] > yn:
            indy = i
            break

    x1 = x[indx - 1]
    x2 = x[indx]

    y1 = y[indy - 1]
    y2 = y[indy]

    f11 = z[indx - 1][indy - 1]
    f12 = z[indx - 1][indy]
    f21 = z[indx][indy - 1]
    f22 = z[indx][indy]

    den = (x1 - x2) * (y1 - y2)
    f = (xn - x2) * (yn - y2) * f11 / den
    f = f + (xn - x2) * (yn - y1) * f12 / (-den)
    f = f + (xn - x1) * (yn - y2) * f21 / (-den)
    f = f + (xn - x1) * (yn - y1) * f22 / (den)

    return f


if __name__ == "__main__":
    x = np.array(object=[0, 1, 2, 3], )
    y = np.array(object=[0, 1, 2, 3], )
    xx, yy = np.meshgrid(x, y)
    z = np.sin((xx**2) + (yy**2))

    p1 = int(input("Enter x: "))
    p2 = int(input("Enter y: "))
    p = [p1, p2]

    print(
        f"Bicubic Interpolation: {bicubic_interpolation(x=x, y=y, z=z, p=p, )}"
    )
    print(
        f"Bilinear Interpolation in \"Pmath04b.py\": {bilinear_interpolation(x, y, z, p)}"
    )
