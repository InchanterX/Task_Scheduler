from datetime import datetime


def time_validation(date: str, format_pattern="%Y-%m-%d %H:%M:%S") -> bool:
    '''Determine if the given date string is valid according to the specified format.'''
    try:
        datetime.strptime(date, format_pattern)
        return True
    except ValueError:
        return False
