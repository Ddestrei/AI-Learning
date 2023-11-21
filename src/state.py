class State:

    def __init__(self, x, y, char, last_state):
        self.x = x
        self.y = y
        self.last_state = last_state
        self.end = False
        self.char = char

    def go(self, x, y, char):
        self.x += x
        self.y += y
        self.char = char
        self.end = self.check_end()
        return self

    def check_end(self):
        if self.char == 'B':
            return True
        else:
            return False