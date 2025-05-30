import turtle

class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float,
                 x: float, y: float, vel_x: float, vel_y: float, color: str, icon='circle'):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance
        self._x = x
        self._y = y
        self._vel_x = vel_x
        self._vel_y = vel_y
        self._t = turtle.Turtle()
        self._t.color(color)
        self._t.shape(icon)
        self._t.speed(10)
        self._t.penup()
        self._t.goto(self._x, self._y)
        self._t.pendown()

    def get_mass(self) -> float:
        return self._mass

    def get_distance(self) -> float:
        return self._distance

    def get_x_pos(self) -> float:
        return self._x

    def get_x_vel(self) -> float:
        return self._vel_x

    def get_y_pos(self) -> float:
        return self._y

    def get_y_vel(self) -> float:
        return self._vel_y

    def set_x_vel(self, new_x_vel: float):
        self._vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self._vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self._x = new_x
        self._y = new_y
        self._t.goto(self._x, self._y)

    def __str__(self) -> str:
        return f"Planet(name={self._name}, mass={self._mass}, x={self._x}, y={self._y})"

    def __eq__(self, other):
        return self._name == other._name

def main():
    p1 = Planet('earth', 5.0, 100.0, 1000.0, 1.0, 1.0, 500.0, 100.0, 'blue')
    p2 = Planet('earth', 5.0, 100.0, 1000.0, 1.0, 1.0, 500.0, 100.0, 'blue')

    print(p1 == p2)

if __name__ == '__main__':
    main()