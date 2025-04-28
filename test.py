class UniversalGravity:
    def __init__(self):
        self.G: float = 6.67430e-11  # Default gravitational constant


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


class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float,
                 x: float, y: float, vel_x: float, vel_y: float):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance
        self._x = x
        self._y = y
        self._vel_x = vel_x
        self._vel_y = vel_y

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

    def __str__(self) -> str:
        return f"Planet({self._name})"


class SolarSystem:
    def __init__(self):
        self._the_sun: Sun = None
        self._planets: list[Planet] = []
        self._gravity = UniversalGravity()

    def add_planet(self, new_planet: Planet):
        self._planets.append(new_planet)

    def add_sun(self, the_sun: Sun):
        self._the_sun = the_sun

    def show_planets(self):
        for planet in self._planets:
            print(planet)

    def move_planets(self):
        # Placeholder for movement logic using self._gravity.G
        pass


class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods

    def run(self):
        for _ in range(self._num_periods):
            self._solar_system.move_planets()
            self._solar_system.show_planets()
