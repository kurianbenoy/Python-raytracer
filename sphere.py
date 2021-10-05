"""A function for rendering the sphere"""
from math import sqrt
from point import Point
from ray import Ray
from material import Material
from typing import Any, Optional


class Sphere:
    def __init__(self, center: Point, radius: float, material: Material) -> None:
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray: Ray) -> Optional[Any]:
        """Checks if ray intersects this sphere."""
        sphere_to_ray = ray.origin - self.center
        # a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist

        return None

    def normal(self, surface_point: Any) -> Any:
        """Returns surface normal to point on sphere's surface"""
        return (surface_point - self.center).normalize()
