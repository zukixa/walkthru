def is_leap_year(year):
    """
    Determines if a given year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
    
def get_us_date(day_count):
    """
    Get the US date corresponding to the given day count.

    Parameters:
        day_count (int): The number of days since January 1, 1960.

    Returns:
        str: The US date corresponding to the given day count.

    """
    current_day, current_month, current_year = 1, 1, 1960
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while day_count > 0:
        if is_leap_year(current_year):
            month_days[1] = 29
        else:
            month_days[1] = 28
        days_in_current_month = month_days[current_month - 1]
        days_till_month_end = days_in_current_month - current_day + 1
        
        if day_count >= days_till_month_end:
            day_count -= days_till_month_end
            current_month += 1
            current_day = 1
        else:
            current_day += day_count
            day_count = 0
        if current_month > 12:  
            current_month = 1
            current_year += 1
        
    return f'{months[current_month - 1]} {current_day}, {current_year}'