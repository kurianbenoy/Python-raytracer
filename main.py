"""A Pure Python Raytracer for my Ammachi
Created by Kurian Benoy
Project started on: September 10, 2021

"""
import argparse
import importlib
import os
from multiprocessing import cpu_count

from engine import RenderEngine
from scene import Scene


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("imageout", help="Path to module to be rendered")
    parser.add_argument(
        "-p",
        "--processes",
        action="store",
        type=int,
        default=0,
        dest="processes",
        help="Specify the number of processors",
    )
    args = parser.parse_args()
    if args.processes == 0:
        process_count = cpu_count()
    else:
        process_count = args.processes
    mera = importlib.import_module(args.imageout)

    scene = Scene(mera.CAMERA, mera.OBJECTS, mera.LIGHTS, mera.WIDTH, mera.HEIGHT)
    engine = RenderEngine()
    # image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(mera.__file__)))
    with open(mera.RENDERED_IMG, "w") as img_file:
        # image.write_ppm(img_file=img_file)
        engine.render_multiprocess(scene, process_count, img_file)


if __name__ == "__main__":
    main()
