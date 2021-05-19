class Event:
    def __init__(self, x, y, pol, ts):
        self.x = int(x)
        self.y = int(y)
        self.pol = bool(pol)
        self.ts = float(ts)

    def __str__(self):
        return "Event =\n\tx: {}\n\ty: {}\n\tpol: {}\n\tts: {}\n".format(self.x, self.y, self.pol, self.ts)

    def __repr__(self):
        return self.__str__()
