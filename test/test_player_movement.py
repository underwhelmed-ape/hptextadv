
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

    assert player.x == 1
    assert player.y == 3


def test_player_moves_south():
    from player import Player

    player = Player()
    print(f'location: ({player.x},{player.y})')

    player.move_south()

    assert player.x == 1
    assert player.y == 1

def test_player_moves_east():
    from player import Player

    player = Player()
    print(f'location: ({player.x},{player.y})')

    player.move_east()

    assert player.x == 2
    assert player.y == 2

def test_player_moves_west():
    from player import Player

    player = Player()
    print(f'location: ({player.x},{player.y})')

    player.move_west()

    assert player.x == 0
    assert player.y == 2

