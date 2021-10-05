#!/usr/bin/env python3
from typing import Any
import math


class Vector:
    """A three elements of vector used in 3D graphics for multiple purposes"""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def dotproduct(self, other: Any) -> Any:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def magnitude(self) -> float:
        return math.sqrt(self.dotproduct(self))

    def normalize(self) -> Any:
        return self / self.magnitude()

    def __add__(self, other: Any) -> Vector:
        return Vector(self.x + other.x, self.y + other.y + self.z + other.z)

    def __sub__(self, other: Any) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: int) -> Vector:
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> Vector:
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)


if __name__ == "__main__":
    v = Vector(1, 3, 4)
    t = 2 * v
    print(t.magnitude())
