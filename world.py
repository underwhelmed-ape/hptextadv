class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError('Create a subclass instead')

class StartTile(MapTile):
    def intro_text(self):
        return '''
        Welcome to the Ministry of Magic. \n
        This is where you work. \n
        '''

class DiagonAlleyBottom(MapTile):
    def intro_text(self):
        return '''
        This is the bottom end of Diagon Alley. \n
        '''

class DiagonAlleyTop(MapTile):
    def intro_text(self):
        return '''
        This is the top end of Diagon Alley. \n
        '''