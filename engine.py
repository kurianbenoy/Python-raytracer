import shutil
import tempfile
from multiprocessing import Process, Value
from pathlib import Path
from typing import Any, List

from color import Color
from image import Image
from point import Point
from ray import Ray
from scene import Scene


class RenderEngine:
    """Renders 3D objects into 2D objects using ray tracing"""

    MAX_DEPTH = 5
    MIN_DISPLACE = 1e-4

    def render_multiprocess(self, scene: Scene, process_count: int, img_file):
        def split_range(count, parts) -> List:
            d, r = divmod(count, parts)
            return [
                (i * d + min(i, r), (i + 1) * d + min(i + 1, r)) for i in range(parts)
            ]

        width = scene.width
        height = scene.height
        ranges = split_range(height, process_count)
        temp_dir = Path(tempfile.mkdtemp())
        temp_file_tmpl = "puray-part-{}.temp"
        processes = []
        try:
            rows_done = Value("i", 0)
            for hmin, hmax in ranges:
                part_file = temp_dir / temp_file_tmpl.format(hmin)
                processes.append(
                    Process(
                        target=self.render,
                        args=(scene, hmin, hmax, part_file, rows_done),
                    )
                )

            # start all processes
            for process in processes:
                process.start()

            # wait for processes to end
            for process in processes:
                process.join()

            Image.write_ppm_header(img_file, height=height, width=width)

            for hmin, _ in ranges:
                part_file = temp_dir / temp_file_tmpl.format(hmin)
                img_file.write(open(part_file, "r").read())
        finally:
            shutil.rmtree(temp_dir)

    def render(self, scene, hmin, hmax, part_file, rows_done):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, hmax - hmin)

        for j in range(hmin, hmax):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                ray = Ray(camera, Point(x, y, 0) - camera)
                pixels.set_pixel(i, j - hmin, self.ray_trace(ray, scene))

            # update progress bar
            # print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")
            if rows_done:
                with rows_done.get_lock():
                    rows_done.value += 1
                    # print(
                    #     "{.3.0f}%".format(float(rows_done.value) / float(height) * 100),
                    #     end="\r",
                    # )
                    print(
                        "{:3.0f}%".format(float(rows_done.value) / float(height) * 100),
                        end="\r",
                    )
        with open(part_file, "w") as part_fileobj:
            pixels.write_ppm_raw(part_fileobj)

    def ray_trace(self, ray, scene, depth: float = 0):
        color = Color(0, 0, 0)
        # Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        if depth < self.MAX_DEPTH:
            new_ray_pos = hit_pos + hit_normal * self.MIN_DISPLACE
            new_ray_dir = (
                ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            )
            new_ray = Ray(new_ray_pos, new_ray_dir)

            # Attenuation of reflected ray coefficent
            color += (
                self.ray_trace(new_ray, scene, depth=depth + 1)
                * obj_hit.material.reflection
            )

        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)

    def color_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.material
        obj_color = material.color_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_hex(
            "#FFFFFF"
        )  # to use ambient light you need to use white color instead of black
        # Light calculations
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # Diffuse shading (Lambert)
            color += (
                obj_color
                * material.diffuse
                * max(normal.dot_product(to_light.direction), 0)
            )
            # Specular shading (Blinn-Phong)
            half_vector = (to_light.direction + to_cam).normalize()
            color += (
                light.color
                * material.specular
                * max(normal.dot_product(half_vector), 0) ** specular_k
            )
        return color


# class RenderEngine:
#     """Renders 3D objects into 2D objects using ray tracing"""

#     def render(self, scene) -> Image:
#         width = scene.width
#         height = scene.height
#         aspect_ratio = float(width) / height
#         x0 = -1.0
#         x1 = +1.0
#         xstep = (x1 - x0) / (width - 1)
#         y0 = -1.0 / aspect_ratio
#         y1 = +1.0 / aspect_ratio
#         ystep = (y1 - y0) / (height - 1)

#         camera = scene.camera
#         pixels = Image(width, height)

#         for j in range(height):
#             y = y0 + j * ystep
#             for i in range(width):
#                 x = x0 + i * xstep
#                 ray = Ray(camera, Point(x, y) - camera)
#                 pixels.set_pixel(i, j, self.ray_trace(ray, scene))
#             # Reason for progress bar
#             print("{:3.0f}%".format(float(j) / float(height) * 100), end="\r")
#         return pixels

#     def ray_trace(self, ray, scene) -> Color:
#         color = Color(0, 0, 0)
#         # Find the nearest object hit by the ray in the scene
#         dist_hit, obj_hit = self.find_nearest(ray, scene)
#         if obj_hit is None:
#             return color
#         hit_pos = ray.origin + ray.direction * dist_hit
#         hit_normal = obj_hit.normal(hit_pos)
#         color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
#         return color

#     def find_nearest(self, ray, scene):
#         dist_min = None
#         obj_hit = None
#         for obj in scene.objects:
#             dist = obj.intersects(ray)
#             if dist is not None and (obj_hit is None or dist < dist_min):
#                 dist_min = dist
#                 obj_hit = obj
#         return (dist_min, obj_hit)

#     def color_at(self, obj_hit, hit_pos, normal, scene):
#         material = obj_hit.material
#         obj_color = material.color_at(hit_pos)
#         to_cam = scene.camera - hit_pos
#         specular_k = 50
#         color = material.ambient * Color.from_hex("#000000")
#         # Light calculations
#         for light in scene.lights:
#             to_light = Ray(hit_pos, light.position - hit_pos)
#             # Diffuse shading (Lambert)
#             color += (
#                 obj_color
#                 * material.diffuse
#                 * max(normal.dotproduct(to_light.direction), 0)
#             )
#             # Specular shading (Blinn-Phong)
#             half_vector = (to_light.direction + to_cam).normalize()
#             color += (
#                 light.color
#                 * material.spectular
#                 * max(normal.dotproduct(half_vector), 0) ** specular_k
#             )
#         return color


# Episode 3
# def color_at(self, obj_hit, hit_pos, scene):
#     return obj_hit.material
