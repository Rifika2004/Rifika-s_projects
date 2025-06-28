# mock_calendar.py
import datetime

class MockCalendar:
    def __init__(self):
        self.bookings = []

    def is_free(self, start: datetime.datetime, end: datetime.datetime) -> bool:
        return all(end <= b["start"] or start >= b["end"] for b in self.bookings)

    def book(self, start: datetime.datetime, end: datetime.datetime, summary: str):
        if not self.is_free(start, end):
            return False
        self.bookings.append({"start": start, "end": end, "summary": summary})
        return True

calendar = MockCalendar()
