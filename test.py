class Test():
    s = 's'
    def __init__(self):
        self.name = 'luo'
    @property
    def speake(self):
        return self.name
    @speake.setter
    def speake(self, size):
        self.name = size
        return self.name

s = Test()
s.speake = 'g'
print(s.speake)

