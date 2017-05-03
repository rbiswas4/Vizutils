"""
Methods for plotting higher dimensional data on 2D plots
"""
__all__ = ['get_scatter']
import matplotlib.pyplot as plt
from six import string_types

def get_scatter(X, Y, Z, data=None, bandname="r", ax=None,
                xTransform=None, yTransform=None, zTransform=None, **kwdargs):
    """
    """
    if ax is None:
        fig, ax = plt.subplots()
    cm = plt.cm.get_cmap('cubehelix')

    lst = []
    for elem, trans in zip((X, Y, Z), (xTransform, yTransform, zTransform)):
        if isinstance(elem, string_types):
            elem = data[elem]
        if trans is not None:
            lst.append(trans(elem))
    X, Y, Z = lst
    im = ax.scatter(X, Y, c=Z, s=0.1, lw=0., cmap=cm, **kwargs)
    return ax
