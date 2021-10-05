"""Class for loading an images"""


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, col):
        self.pixels[y][x] = col

    def write_ppm(self, img_file):
        Image.write_ppm_header(img_file, self.height, self.width)
        self.write_ppm_raw(img_file)

    @staticmethod
    def write_ppm_header(img_fileobj, height=None, width=None):
        """Writes only the header of PPM file"""
        img_fileobj.write("P3 {} {} \n255\n".format(width, height))

    def write_ppm_raw(self, img_file):
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        for row in self.pixels:
            for color in row:
                img_file.write(
                    "{} {} {} ".format(
                        to_byte(color.x), to_byte(color.y), to_byte(color.z)
                    )
                )
            img_file.write("\n")
