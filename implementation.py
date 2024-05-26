def is_leap_year(year):
    """
    Returns the number of days in February for a given year.

    Parameters:
        year (int): The year to check.

    Returns:
        int: 29 if the year is a leap year, 28 otherwise.
    """
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return 29
    return 28
    
def get_us_date(day_count: int):
    """
    Get the US date corresponding to the given day delta.

    Parameters:
        day_count (int): The delta of days to January 1, 1960.

    Returns:
        str: The US date corresponding to the given day delta.

    """
    if not isinstance(day_count, int):
        raise ValueError('Day delta must be an integer.')
    
    current_day, current_month, current_year = 1, 1, 1960
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while day_count > 0:
        month_days[1] = is_leap_year(current_year) 
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
            
    while day_count < 0:
        if current_month == 1:
            current_year -= 1
            current_month = 12
        else:
            current_month -= 1

        month_days[1] = is_leap_year(current_year) 
        days_in_previous_month = month_days[current_month - 1]
        
        if -day_count > days_in_previous_month:
            day_count += days_in_previous_month
        else:
            current_day = days_in_previous_month + day_count + 1
            day_count = 0

        
    return f'{months[current_month - 1]} {current_day}, {current_year}'