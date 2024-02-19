class PistolGun:
    def __init__(self, caliber, capacity):
        self.caliber = caliber
        self.capacity = capacity
        self.ammo_count = 0

    def load_gun(self, count):
        if count < 0:
            return self.ammo_count
        space_available = self.capacity - self.ammo_count
        if count > 20:
            count = 20
        if count <= space_available:
            self.ammo_count += count
        return self.ammo_count

    def shoot_gun(self):
        if self.ammo_count > 0:
            self.ammo_count -= 1
        return self.ammo_count







