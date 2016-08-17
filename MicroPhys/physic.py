class PhysicObject:
    def __init__(self, pos, speed, mass):
        self.pos, self.speed, self.mass = pos, speed, mass


class PhysicHandler:
    def __init__(self, dt=1, n=5):
        self.speed_modifier = []
        self.objects = []
        self.n = n
        self.time = 0
        self.dt = dt

    def add_modifier(self, f):
        self.speed_modifier.append(f)

    def compute_speed(self, obj, pos=None, date=None):
        s = obj.speed
        for m in self.speed_modifier:
            s += m(obj, pos, date)
        obj.speed = s
        return s

    def compute_pos(self, begin, end):
        h = (end-begin)/self.n
        for o in self.objects:
            date, pos = begin, o.pos
            while date < end:
                k1 = self.compute_speed(o, pos, date)
                k2 = self.compute_speed(o, pos.sum(k1.times(h / 2)), date + h / 2)
                k3 = self.compute_speed(o, pos.sum(k2.times(h / 2)), date + h / 2)
                k4 = self.compute_speed(o, pos.sum(k3.times(h)), date + h)
                date += h
                pos = pos.add(k1.add(k4.add(k2.times(2).add(k3.times(2)))).times(h/6))
            o.pos = pos

    def update(self):
        self.compute_pos(self.time, self.time + self.dt)
        self.time += self.dt
