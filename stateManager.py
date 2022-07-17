

class StateManager(object):
    """May be change it to ability manager but either way is fine"""

    def __init__(self):
        self.running = True
        self.states = []
        self.this_instance = self

    def update(self):
        self.current_state().update()

    def render(self):
        self.current_state().render()

    def calculate(self):
        return self.current_state().calculate()

    def current_state(self):
        return self.states[-1]

    def push_state(self, state):
        self.states.append(state)

    def pop_state(self):
        self.states.pop(-1)

