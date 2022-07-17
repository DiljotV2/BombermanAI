import pyglet

from agent import Agent
from graphics import egi


class Player(Agent):

    def __init__(self, world=None, box = None, mode='normal'):
        super.__init__()
        self.world = world
        self.box = box
        self.mode = mode  # normal or ai
        self.image = egi.load_image("BitmapResources/Player.bmp")
        self.bomb = None

    def update(self):
        if self.bomb:
            self.bomb.update()

    def render(self, color=None):
        sprite = pyglet.sprite.Sprite(self.image, self.box._pts[0].x, self.box._pts[0].y - 25)
        sprite.scale_x = 0.6
        sprite.scale_y = 0.6
        sprite.draw()
        if self.bomb:
            self.bomb.render()

    def move(self, direction):
        intended_position_box = None
        if direction == 'right':
            if self.box.idx % self.world.nx != self.world.nx - 1:
                intended_position_box = self.world.boxes[self.box.idx + 1]
        elif direction == 'left':
            if self.box.idx % self.world.nx != 0:
                intended_position_box = self.world.boxes[self.box.idx - 1]
        elif direction == 'up':
            if self.box.idx < ((self.world.nx * self.world.ny) - (self.world.nx + 1)):
                intended_position_box = self.world.boxes[self.box.idx + self.world.nx]
        elif direction == 'down':
            if self.box.idx >= self.world.nx:
                intended_position_box = self.world.boxes[self.box.idx - self.world.nx]
        else:
            pass

        if intended_position_box:
            self.box = intended_position_box if not self.collision_detection(intended_position_box) else self.box

    def collision_detection(self, future_position_box):
        for element in future_position_box.has_elements:
            if element in ['rocks', 'bricks']:
                return True
        return False

    def plant_bomb(self):
        # will be used to plant bomb

        pass

