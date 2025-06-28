# mock_calendar.py

class MockCalendar:
    def __init__(self):
        self.booked = []

    def is_free(self, start, end):
        for s, e, _ in self.booked:
            if max(s, start) < min(e, end):
                return False
        return True

    def book(self, start, end, title):
        self.booked.append((start, end, title))

calendar = MockCalendar()
