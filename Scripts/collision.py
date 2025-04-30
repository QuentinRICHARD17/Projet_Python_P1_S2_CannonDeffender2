def detecter_collisions(boulets, bateaux):
    for boulet in boulets:
        for bateau in bateaux:
            if (boulet.position[0] == bateau.position[0] and
                boulet.position[1] == bateau.position[1]):
                bateau.pv -= 10
                boulets.remove(boulet)
                break
                # Pour  push