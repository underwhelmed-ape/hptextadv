
def test_player_starts_at_1_2():
    from player import Player

    player = Player()

    assert player.x == 1
    assert player.y == 2
    



def test_player_moves_north():
    from player import Player

    player = Player()
    print(f'location: ({player.x},{player.y})')

    player.move_north()

    assert player.y == 3

