from server.game.game import Game


def test_next_turn():
    # Creamos una nueva partida
    game = Game()

    # Comprobamos que la partida empieza en el turno 1
    assert game.turn == 1

    # Pasamos al siguiente turno
    game.next_turn()

    # Comprobamos que ahora estamos en el turno 2
    assert game.turn == 2