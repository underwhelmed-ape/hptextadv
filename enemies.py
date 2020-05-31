class Enemy:
    def __init__(self):
        raise NotImplementedError('Do not create raw Enemy objects')

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class FinalBoss(Enemy):
    def __init__(self):
        self.name = 'Willy Widdershins'
        self.hp = 150
        self.damage = 50





if __name__ == "__main__":
    pass