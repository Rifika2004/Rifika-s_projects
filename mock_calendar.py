# mock_calendar.py

calendar_data = {}

def is_available(date_str: str) -> bool:
    return date_str not in calendar_data

def book_slot(date_str: str) -> str:
    if is_available(date_str):
        calendar_data[date_str] = True
        return f"✅ Slot booked for {date_str}"
    else:
        return f"❌ Sorry, {date_str} is already booked."
