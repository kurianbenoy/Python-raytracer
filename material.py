"""Material class for function"""


from typing import Any
from color import Color


class Material:
    """Material has color and properties which tells how its react to light"""

    def __init__(
        self,
        color: Any = Color.from_hex("#FFFFFF"),
        ambient: float = 0.05,
        diffuse: float = 1.0,
        specular: float = 1.0,
        reflection: float = 0.5,
    ):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self, position):
        return self.color

    # def color_at(self, obj_hit, hit_pos, scene):
    #     return obj_hit.material


class ChequeredMaterial:
    """Material which has a chessboard pattern based in two colors"""

    def __init__(
        self,
        color1: Any = Color.from_hex("#FFFFFF"),
        color2: Any = Color.from_hex("#000000"),
        ambient: float = 0.05,
        diffuse: float = 1.0,
        specular: float = 1.0,
        reflection: float = 0.5,
    ) -> None:
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self, position):
        # This pattern was originally was there in Arun's book
        if int((position.x + 5.0) * 3.0) % 2 == int(position.z * 3.0) % 2:
            return self.color1
        else:
            return self.color2
