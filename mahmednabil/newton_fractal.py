import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from alive_progress import alive_bar

"""
function and it's derivative
"""
def f(x): return x**3 - 1
def fprime(x): return 3*x**2


TOL = 1.e-8
colors = ['b', 'r', 'g', 'y']


def newton_method(x0, f, fprime, ITER=2000):
    x = x0
    for i in range(ITER):
        step = f(x)/fprime(x)
        # approximat to zero
        if abs(step) < TOL:
            return x
        # move estimation to zero
        x -= step
    # dose not conversion
    return False


def plot_newton_fractal(f, fprime, n=200, domain=(-1, 1, -1, 1)):
    """
    get the closest root to the point after applying newton methods
    """
    def get_root_index(roots, r):
        try:
            return np.where(np.isclose(roots, r, atol=TOL))[0][0]
        except IndexError:
            roots.append(r)
            return len(roots) - 1

    roots = []
    m = np.zeros((n, n))

    with alive_bar(n) as bar:
        xmin, xmax, ymin, ymax = domain
        for ix, x in enumerate(np.linspace(xmin, xmax, n)):
            for iy, y in enumerate(np.linspace(ymin, ymax, n)):
                x0 = x + y*1j
                _root = newton_method(x0, f, fprime)
                if _root is not False:
                    root_index = get_root_index(roots, _root)
                    m[ix, iy] = root_index
            bar()

    print("[LOG] DONE")
    nroots = len(roots)
    if nroots > len(colors):
        cmap = 'hsv'
    else:
        cmap = ListedColormap(colors[:nroots])

    # TODO
    cmap = 'Accent'

    plt.imshow(m, cmap=cmap, origin='lower')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    plot_newton_fractal(f, fprime, n=1000)
