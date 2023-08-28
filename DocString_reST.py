def add_numbers(x, y):
    """
    Adds two numbers together
    :param x: The first number to add
    :type x: int or float
    :param y: The second number to add
    :type y: int or float
    :return: The sum of x and y
    :type: int or float
    :raises ValueError: If either x or y is not an int or float
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError('Both x and y must be ints or floats')
    return x + y
