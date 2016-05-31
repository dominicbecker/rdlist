# Simple node class to contain our nodes
# data: any data, in our test caes we use an int
# down: another node or None
# right: another node or None
class node:
    def __init__(self, data, down, right):
        self.data = data
        self.down = down
        self.right = right

    def __repr__(self):
        dr = repr(self.down)
        rr = repr(self.right)
        return 'node(%s, %s, %s)' % (self.data, dr, rr)
