'''Path container to support easy path following by Agents

Created for COS30002 AI for Games by Clinton Woodward <cwoodward@swin.edu.au>

For class use only. Do not publically share or post this code without permission.

'''

from random import random, uniform
#from matrix33 import Matrix33
#from vector2d import Vector2D
from graphics import egi

from math import pi

TWO_PI = pi * 2.0

class Way(object):
    ''' Container to hold a number of way points and a cursor to the
        current way point. The cursor can be moved to the next way point by
        calling set_next_way_pt(). Paths can be open or looped. '''

    def __init__(self):#, num_pts=0, pts=[]):
        ''' If number of points (num_pts) is provided, a path of random
            non-overlapping waypoints will be created in the region specified
            by the min/max x/y values provided. If the path is looped, the last
            way point is connected to the first. '''

        self._cur_pt_idx = -1
        self._pts = None

    def current_pt(self):
        ''' Return the way point of the path indicated by the current point
            index. '''
        return self._pts[self._cur_pt_idx]

    def inc_current_pt(self):
        ''' Update the current point to the next in the path list.
            Resets to the first point if looped is True. '''
        self._cur_pt_idx += 1

    def is_finished(self):
        ''' Return True if at the end of the path. '''
        return self._cur_pt_idx >= self._num_pts - 1

    def set_pts(self, path_pts):
        ''' Replace our internal set of points with the container of points
            provided. '''
        self._pts = path_pts
        self._reset()

    def _reset(self):
        ''' Point to the first waypoint and set the limit count based on the
            number of points we've been given. '''
        self._cur_pt_idx = 0
        self._num_pts = len(self._pts)

    def clear(self):
        ''' Remove all way points and reset internal counters. '''
        self._pts = []
        self._reset()

    def get_pts(self):
        ''' Simple wrapper to return a reference to the internal list of
            points.'''
        return self._pts