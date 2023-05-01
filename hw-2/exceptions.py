class LowFuelError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num

class NotEnoughFuel(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num
class CargoOverload(Exception):
    def __init__(self, text, num, m=100):
        self.txt = text
        self.n = num
        self.m = m