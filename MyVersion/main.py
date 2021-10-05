# Our object in video 4 is to make the red ball which was in 2D shape,
# with use of lambard shading + other theory to create a 3D shape
# make it look with shading
import argparse
from color import Color
from ..engine import RenderEngine
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", help="Pass the file name you want to generate Color within"
    )
    args = parser.parse_args()
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, -0.25, 0), 0.2, Color.from_hex("#fad000"))]
    # objects = [
    #     Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#299438")),
    #     # Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000")),
    #     # Sphere(Point(0, 2, 0), 0.5, Color.from_hex("#FAD000")),
    # ]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open(args.file, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
