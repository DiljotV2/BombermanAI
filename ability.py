from state import State
from stateManager import StateManager


class Ability(State):
    """Need to have more virtual methods along the way"""
    def __init__(self, world=None, box = None, image_string = None):
        self.world = world
        self.box = box
        self.image_string = image_string
        self.visibility = False

    def update(self):
        pass

    def render(self):
        pass

    def effect(self):
        pass