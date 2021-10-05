import logging
from color import Color


class TestColor:
    def setup(self):
        self.black = Color(x=0, y=0, z=0)
        self.white = Color(x=255, y=255, z=255)

    def test_black(self):
        assert self.black.x == 0
        assert self.black.y == 0
        assert self.black.z == 0

    def test_white(self):
        assert self.white.x == 255, "value not passed correctly"
        assert self.white.y == 255
        assert self.white.z == 255

    def test_black_hexcolor(self):
        temp = self.black.from_hex("#0000000")
        logging.info(temp)
        assert temp.x == 0.0
        assert temp.y == 0.0
        assert temp.z == 0.0

    def test_white_hexcolor(self):
        temp = Color.from_hex("#FF0000")
        assert temp.x == 1.0
        assert temp.y == 0.0
        assert temp.z == 0.0

    def test_transform_classproperty(self):
        temp = self.white.from_hex("#FF0000")
        assert temp.x == 1.0
        assert temp.y == 0.0
        assert temp.z == 0.0
