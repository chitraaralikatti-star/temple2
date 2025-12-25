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
            print("Invalid slot selected")
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

    while True:
        print("\nAvailable Slots:")
        for s in manager.slots:
            print(s)

        slot = input("Enter slot (or type exit): ")
        if slot.lower() == "exit":
            break

        count = int(input("Enter number of people: "))
        manager.book_people(slot, count)

        print("Crowd level for", slot, ":", manager.check_crowd(slot))

    print("\nFinal Crowd Status:")
    for s in manager.slots:
        print(s, "->", manager.check_crowd(s))

    print("Best slot to visit:", manager.best_time_slot())

