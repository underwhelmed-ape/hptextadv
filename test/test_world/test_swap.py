

def test_trading():
    from world import PopupPotions
    from player import Player

    player = Player()
    # assert player has original allowance of money
    assert player.inventory[2].value == 493 * 2

    # assert player has had money deducted after purchace
    shop = PopupPotions(1,2)
    shop.swap(3, player)
    
    # 493 * 2 - 800
    assert player.inventory[2].value == (493 * 2) - 800
    
