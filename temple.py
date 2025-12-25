import os

class DarshanManager:
    def __init__(self):
        self.slots = {
            "6AM-8AM": 0,
            "8AM-10AM": 0,
            "10AM-12PM": 0,
            "4PM-6PM": 0
        }

    def book_people(self, slot, count):
        if slot not in self.slots:
            print("Invalid slot")
            return
        self.slots[slot] += count

    def check_crowd(self, slot):
        people = self.slots[slot]
        if people <= 50:
            return "LOW"
        elif people <= 100:
            return "MEDIUM"
        else:
            return "HIGH"

    def best_time_slot(self):
        return min(self.slots, key=self.slots.get)


if __name__ == "__main__":
    manager = DarshanManager()

    # 🔑 Jenkins parameters (NO input())
    slot = os.getenv("ENTER_SLOT", "6AM-8AM")
    people = int(os.getenv("ENTER_PEOPLE", "0"))

    manager.book_people(slot, people)

    print("Slot:", slot)
    print("People:", people)
    print("Crowd Level:", manager.check_crowd(slot))
    print("Best Slot:", manager.best_time_slot())
