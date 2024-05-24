def get_us_date(day_count):
    """
    Get the US date corresponding to the given day count.

    Parameters:
        day_count (int): The number of days since January 1, 1960.

    Returns:
        str: The US date corresponding to the given day count.

    """
    return f'January {1 + day_count}, 1960'