class PistolGun:
    def __init__(self, caliber, capacity):
        if caliber <= 0 or capacity <= 0:
            raise ValueError("Caliber and capacity must be positive integers.")
        self.caliber = caliber
        self.capacity = capacity
        self.ammo_count = 0
        self.safety_on = True

    def load_gun(self, count):
        if count < 0:
            raise ValueError("Number of bullets to load must be non-negative.")
        if self.safety_on:
            raise ValueError("Safety is on. Turn off safety to load the gun.")
        space_available = self.capacity - self.ammo_count
        count = min(count, space_available, 20)
        self.ammo_count += count
        return self.ammo_count

    def shoot_gun(self):
        if self.safety_on:
            raise ValueError("Safety is on. Turn off safety to shoot the gun.")
        if self.ammo_count > 0:
            self.ammo_count -= 1
        return self.ammo_count

    def toggle_safety(self):
        self.safety_on = not self.safety_on

    def inspect_gun(self):
        if self.safety_on:
            safety_state = "on"
        else:
            safety_state = "off"
        return f"Caliber: {self.caliber},Capacity: {self.capacity},Ammo Count: {self.ammo_count},Safety: {safety_state}"
