from datetime import datetime

calendar = {}

def is_available(dt: datetime) -> bool:
    return dt not in calendar

def book_slot(dt: datetime):
    calendar[dt] = True
