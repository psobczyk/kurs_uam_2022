"""
Dummy module

"""


def dummy_function(arg_1):
    """
    Multiply by 2

    :param arg_1
    """
    return arg_1 * 2


if __name__ == "main":
    x = 2  # pylint: disable=C0103
    print(dummy_function(x))
