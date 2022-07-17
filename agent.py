'''An agent with Seek, Flee, Arrive, Pursuit behaviours

Created for COS30002 AI for Games by Clinton Woodward <cwoodward@swin.edu.au>

For class use only. Do not publically share or post this code without permission.

'''

from point2d import Point2D
from graphics import egi, KEY
from math import sin, cos, radians
from random import random, randrange, uniform
from way import Way

AGENT_MODES = ['A*', 'Dijkstra', 'DFS', 'BFS']


class Agent(object):

    def __init__(self, world=None, nameid = None, box = None, index = None, search_mode=None, color='ORANGE', mode=None):
        # keep a reference to the world object
        self.world = world
        self.box = box
        self.pos = Point2D(box._vc.x, box._vc.y)
        self.index = index
        self.color = color
        self.path = None
        self.way = Way()
        self.name_id = nameid
        self.search_algo = search_mode
        self.mode = mode
        self.target_idx = None

    def set_pos(self):
        self.pos = Point2D(self.box._vc.x, self.box._vc.y)

    def update(self):
        if self.mode == "Target_Hunter":
            # self.target_pos
            if self in self.world.agents and self.world.target is not None:
                if self.world.target.idx != self.target_idx or not self.path:
                    self.target_idx = self.world.target.idx
                    self.path = self.world.find_target_path(self, self.search_algo)
                    path_points = list(self.path.path)
                    self.way.set_pts(path_points)
                else:
                    self.way.inc_current_pt()
                    self.box = self.world.boxes[self.way.current_pt()]
                    self.index = self.box.idx

        if self.mode == 'Agent_Hunter':
            chasing_target_hunter_path = None
            chasing_target_path_list = None
            # This will get the path algo of the nearest agent.
            if self in self.world.agents and self.world.target is not None:
                for agent in self.world.agents:
                    if agent.mode == "Target_Hunter":
                        self.path = self.world.find_agent_path(self.index, agent.index, self.search_algo)
                        path_points = list(self.path.path)

                        if chasing_target_hunter_path is None:
                            chasing_target_hunter_path = self.path
                            chasing_target_path_list = list(chasing_target_hunter_path.path)
                        elif len(path_points) > len(chasing_target_path_list):
                            self.path = chasing_target_hunter_path

            self.way.set_pts(list(self.path.path))
            self.way.inc_current_pt()
            self.box = self.world.boxes[self.way.current_pt()]
            self.index = self.box.idx

    def render(self, color=None):
        if self.mode == 'Target_Hunter':
            self.set_pos()
            egi.set_pen_color(name=self.color)
            egi.circle(self.pos, 5, filled=True)

        if self.mode == "Agent_Hunter":
            egi.set_pen_color(name=self.color)
            egi.closed_shape(self.box._pts)

    def __str__(self):
        return "{0}({1})({2})".format(self.name_id, self.color, self.mode)
