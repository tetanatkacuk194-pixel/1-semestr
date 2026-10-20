class LimitedInventory:
    def __init__(self, max_slots, max_stack):
        self.max_slots = max_slots
        self.max_stack = max_stack
        self.slots = {}

    def add_item(self, name, count=1):
        try:
            if count <= 0:
                return
            if name in self.slots:
                pototo_vsego = self.slots[name]
                zaniato_slots = (pototo_vsego + self.max_stack - 1) // self.max_stack
                vilsno_v_stakah = (zaniato_slots * self.max_stack) - pototo_vsego

                if count <= vilsno_v_stakah:
                    self.slots[name] += count
                    return
                else:
                    self.slots[name] += vilsno_v_stakah
                    count -= vilsno_v_stakah
            nuzhno_slots = (count + self.max_stack - 1) // self.max_stack
            vsego_zaniato = sum((v + self.max_stack - 1) // self.max_stack for v in self.slots.values())
            if vsego_zaniato + nuzhno_slots > self.max_slots:
                raise IndexError()
            if name in self.slots:
                self.slots[name] += count
            else:
                self.slots[name] = count
        except IndexError:
            raise IndexError("Mistsa nemae!")

    def remove_item(self, name, count=1):
        try:
            if name not in self.slots or self.slots[name] < count:
                raise KeyError()

            self.slots[name] -= count
            if self.slots[name] <= 0:
                del self.slots[name]
        except KeyError:
            raise KeyError("Predmet ne znaideno!")
    def get_info(self):
        vsego_zaniato = sum((v + self.max_stack - 1) // self.max_stack for v in self.slots.values())
        return f"{vsego_zaniato}/{self.max_slots}"