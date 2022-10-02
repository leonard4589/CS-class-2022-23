class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def yreturn(self, x):
        y = self.a*(x)**2 + self.b*x + self.c
        self.y = y
        return y
    def xreturn(self, y):
        x1 = (-self.b + ((self.b)**2 - 4*self.a*(self.c*y))**0.5)/2*self.a
        x2 = (-self.b - ((self.b)**2 - 4*self.a*(self.c*y))**0.5)/2*self.a
        return x1, x2
    def vertex(self):
        x = -self.b/(2*self.a)
        y = self.yreturn(x)
        return x,y
    def yintercept(self):
        b = self.c
        return b 
    def zeros(self):
        z1 = (-self.b + ((self.b)**2 - 4*self.a*(self.c))**0.5)/2*self.a
        z2 = (-self.b - ((self.b)**2 - 4*self.a*(self.c))**0.5)/2*self.a
        return z1, z2 