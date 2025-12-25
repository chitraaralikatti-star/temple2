from temple import DarshanManager

def test_booking_parameter():
    d = DarshanManager()
    d.book_people("6AM-8AM", 30)
    assert d.slots["6AM-8AM"] == 30

def test_medium_crowd():
    d = DarshanManager()
    d.book_people("8AM-10AM", 80)
    assert d.check_crowd("8AM-10AM") == "MEDIUM"

def test_high_crowd():
    d = DarshanManager()
    d.book_people("10AM-12PM", 120)
    assert d.check_crowd("10AM-12PM") == "HIGH"

def test_best_slot():
    d = DarshanManager()
    d.book_people("6AM-8AM", 100)
    d.book_people("4PM-6PM", 20)
    assert d.best_time_slot() == "4PM-6PM"
