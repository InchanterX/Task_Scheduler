from datetime import datetime


def time_validation(date: str, format_pattern="%Y-%m-%d %H:%M:%S") -> bool:
    try:
        datetime.strptime(date, format_pattern)
        return True
    except:
        return False
