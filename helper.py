class Patient:
    def __init__(self, mrn, name):
        self.mrn = mrn
        self.name = name

    class Field:
        def __init__(self, fname, rangeshifter, depth, snout, rotation):
            self.fname = fname
            self.rangeshifter = rangeshifter
            self.depth = depth
            self.snout = snout
            self.rotation = rotation

class TimeDelay:
    def __init__(self, rangeshift, depth, snout, rotation):
        self.rangeshift = rangeshift
        self.depth = depth
        self.snout = snout
        self.rotation = rotation
