from vector import Vector


class Color(Vector):
    """Stores Color with RGB. Inheriting from Vector class"""

    @classmethod
    def from_hex(cls, hexcolor: str = "#000000") -> Vector:
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        return cls(x, y, z)
