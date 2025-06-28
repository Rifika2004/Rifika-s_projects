# mock_calendar.py

booked = []

def is_free(start, end):
    for s, e, _ in booked:
        if max(s, start) < min(e, end):  # time overlaps
            return False
    return True

def book(start, end, title):
    booked.append((start, end, title))
."
