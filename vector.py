"""File for Vector class"""
import math
from typing import Any


class Vector:
    """A three element vector used in 3D graphics for multiple purposes"""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self) -> str:
        return f"{self.x} {self.y} {self.z}"

    def dot_product(self, other: Any) -> Any:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self) -> float:
        return math.sqrt(self.dot_product(self))

    def normalize(self) -> Any:
        return self / self.magnitude()

    def __add__(self, other: Any) -> Any:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Any) -> Any:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: Any) -> Any:
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> Any:
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)
