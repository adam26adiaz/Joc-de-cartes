class Game:
    def __init__(self):
        # El juego empieza en el turno 1
        self.turn = 1

    def next_turn(self):
        # Pasamos al siguiente turno
        self.turn += 1