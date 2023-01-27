from ROOT import FILE


class Polygon:
    def __init__(self, polygon, parameters=(False, False)):
        self.polygon = polygon
        self.is_passed, self.is_permanent = parameters

    def save(self):
        FILE.write(self.polygon + [(self.is_passed, self.is_permanent)])

    def __eq__(self, other):
        return self.polygon == other.polygon

    def set_passed(self):
        self.is_passed = True
