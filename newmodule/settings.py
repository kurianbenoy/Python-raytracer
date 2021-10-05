from color import Color
from light import Light
from material import ChequeredMaterial, Material
from point import Point
from sphere import Sphere
from vector import Vector


WIDTH = 640
HEIGHT = 480
RENDERED_IMG = "temp2balls.ppm"
CAMERA = Vector(x=0, y=-0.25, z=-1)
OBJECTS = [
    # Ground Plane
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        ChequeredMaterial(
            color1=Color.from_hex("#000000"),
            color2=Color.from_hex("#ffffff"),
            ambient=0.2,
            reflection=0.2,
        ),
    ),
    Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#ff1204"))),
    Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#1bd7f8"))),
]
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
]
