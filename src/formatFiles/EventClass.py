class Event:
    def __init__(self, x, y, pol, ts):
        self.x = x
        self.y = y
        self.pol = pol
        self.ts = ts

    def __str__(self):
        return "Event =\n\tx: {}\n\ty: {}\n\tpol: {}\n\tts: {}\n".format(self.x, self.y, self.pol, self.ts)

    def __repr__(self):
        return self.__str__()
