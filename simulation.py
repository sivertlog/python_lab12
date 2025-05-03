import random
from solar_system import SolarSystem
from sun import Sun
from planet import Planet
import turtle

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods
        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._screen = turtle.Screen()
        self._screen.setup(width = self._width, height = self._height)
        self._screen.bgcolor('black')
        self._screen.addshape("sunshine.gif")
        self._screen.addshape("earth.gif")
        self._t.clear()

    def run(self):
        self._solar_system.show_planets()
        for _ in range(self._num_periods):
            self._solar_system.move_planets()
            self._solar_system.show_planets()

    def freeze(self):
        self._screen.exitonclick()

def draw_star(t:turtle.Turtle, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def main():
    solar_system = SolarSystem()
    simulation = Simulation(solar_system, 500, 500, 200000)

    t = turtle.Turtle()
    draw_sky(t, 10)

    sol = Sun('Sol', 5000, 1000000000000000, 5000, 0, 0, 'sunshine.gif')
    solar_system.add_sun(sol)
    earth = Planet('Earth', 500, 1000, 75, 0, 75, 20, 0, 'blue', 'earth.gif')
    solar_system.add_planet(earth)
    earth2 = Planet('Earth2', 500, 1000, 75, 0, -75, -25, 0, 'green')
    solar_system.add_planet(earth2)
    mars = Planet('Mars', 500, 1000, 150, 150, 0, (-.001), (-17), 'red')
    solar_system.add_planet(mars)

    simulation.run()


if __name__ == '__main__':
    main()