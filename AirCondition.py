class AirCondition:
    def __init__(self):
        self.ac_off = False
        self.ac_on = False
        self.ac_temp = 16

    def get_ac_on(self):
        return self.ac_on

    def get_ac_off(self):
        return self.ac_off

    def get_ac_temp(self):
        return self.ac_temp

    def set_ac_on(self, ac_on):
        self.ac_on = ac_on

    def set_ac_off(self, ac_off):
        self.ac_off = ac_off

    def set_ac_temp(self, ac_temp):
        if self.ac_on and 16 <= ac_temp <= 30:
            self.ac_temp = ac_temp

    def increase_ac(self):
        if self.ac_on and ac_temp >= 16 and ac_temp < 30:
            self.ac_temp += 1

    def decrease_ac(self):
        if self.ac_on and ac_temp > 16 and ac_temp <= 30:
            self.ac_off -= 1



