from vector import Vector


class Ray:
    def __init__(self, origin, direction) -> None:
        self.origin = origin
        self.direction = direction.normalize()


class Sphere:
    def __init__(self, ballpos, radius, color) -> None:
        self.ballpos = ballpos
        self.radius = radius
        self.color = color

    def transform_color(self):
        x = int(self.color[1:3], 16)
        y = int(self.color[3:5], 16)
        z = int(self.color[5:7], 16)
        return (x, y, z)

    def find_intersection():
        pass


if __name__ == "__main__":
    width = 320
    height = 200
    first_row = f"P3 {width} {height}"
    camera_position = Vector(x=0, y=0, z=-1)
    sphere_radius = 0.5

    # 0, 0,0 and radius is at 0.5
    # find interesecting point
    sphere = Sphere(Vector(x=0, y=0, z=0), sphere_radius, color="#FFFFFF")
    ray = Ray(camera_position, Vector(x=0, y=0, z=1))

    # on ray and sphere intersecting, the image is being created
    # and color is scattered based on that

    # sphere-ray intersection comes into play
    with open(file="test_mera.ppm", mode="a") as file:
        file.write(first_row)
        file.writelines("\r\n255\r\n")

    for _ in range(width):
        temp = ""
        for _ in range(height):
            r, g, b = int(input()), int(input()), int(input())
            temp += f"{r} {g} {b} "
        with open(file="test_mera.ppm", mode="a") as file:
            temp += "\r\n"
            file.writelines(temp)
