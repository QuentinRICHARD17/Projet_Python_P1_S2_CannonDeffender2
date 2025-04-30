class Boulet:
    def __init__(self, position, vitesse):
        self.position = list(position)
        self.vitesse = vitesse

    def mouvoir(self):
        self.position[0] += self.vitesse[0]
        self.position[1] += self.vitesse[1]