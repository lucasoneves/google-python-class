def repeat(s, exclaim):
    """
    This is a comment in python
    """

    result = s * 3

    if exclaim:
        result = result + '!!!'
        print(result)
    return result

repeat(str(10), True)