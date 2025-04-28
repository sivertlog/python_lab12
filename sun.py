class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float, y: float):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._temp = temp
        self._x = x
        self._y = y

    def get_mass(self) -> float:
        return self._mass

    def get_x_pos(self) -> float:
        return self._x

    def get_y_pos(self) -> float:
        return self._y

    def __str__(self) -> str:
        return f"Sun({self._name})"