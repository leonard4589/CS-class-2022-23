class StLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2 
    def slope(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self. y1
        m = dy/dx
        self.m = m
        return m 
    def yintercept(self):
        m = self.slope()
        b = self.y1 - (m*self.x1)
        self.b = b
        return b 
    def xreturn(self, y):
        b = self.yintercept()
        m = self.slope()
        x = (y - b)/m
        return x
    def yreturn(self, x):
        b = self.yintercept()
        m = self.slope()
        y = m*x + b 
        return y 

