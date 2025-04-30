class Canon:
    def __init__(self, position, angle, puissance):
        self.position = list(position)
        self.angle = angle
        self.puissance = puissance

    def tirer(self):
        from Scripts.projectile import Boulet
        return Boulet(position=self.position, vitesse=[self.puissance, -self.puissance])