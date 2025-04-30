class Bateau:
    def __init__(self, position, pv):
        self.position = list(position)
        self.pv = pv

    def avancer(self):
        self.position[0] -= 2
        # Pour  push