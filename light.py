from typing import Any
from color import Color
from point import Point


class Light:
    """Light represents a point light source of a certain color"""

    def __init__(self, position: Point, color: Any = Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
