from player import Player

class Bomb(object):

    def __init__(self, player, position_box):
        self.player = player
        self.position_box = position_box
        self.timer = 10

    def update(self):
        pass

    def render(self):
        pass