"""Dummy module."""


def bar():
    """
    Do nothing.

    Returns
    -------
    out : None
        Nothing.

    Examples
    --------
    If I try to plot something

    >>> import matplotlib.pyplot as plt
    >>> plt.plot([1, 2, 3], [1, 2, 3])
    >>> plt.show()

    but end the docstring with a text line right after invoking `plt.show()` the
    plot doesn't show up.
    """
    pass


def foo():
    """
    Do nothing again.

    Returns
    -------
    out : None
        Nothing.

    Examples
    --------
    However if I try to plot something without it being followed by text the
    plot is included.

    >>> import matplotlib.pyplot as plt
    >>> plt.plot([1, 2, 3], [1, 2, 3])
    >>> plt.show()
    """
    pass
