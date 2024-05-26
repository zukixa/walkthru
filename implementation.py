def get_us_date(day_count):
    """
    Get the US date corresponding to the given day count.

    Parameters:
        day_count (int): The number of days since January 1, 1960.

    Returns:
        str: The US date corresponding to the given day count.

    """
    init_day, init_month = 1, 1
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while day_count > 0:
        days_in_current_month = month_days[init_month - 1]
        days_till_month_end = days_in_current_month - init_day + 1
        
        if day_count >= days_till_month_end:
            day_count -= days_till_month_end
            init_month += 1
            init_day = 1
        else:
            init_day += day_count
            day_count = 0

        
    return f'{months[init_month - 1]} {init_day}, 1960'