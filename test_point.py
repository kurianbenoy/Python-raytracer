from point import Point

class TestPoint:
    def setup(self):
        self.pt1 = Point(x=25, y=10, z=100)
        self.pt2 = Point(x=1, y=12, z=12)

    def test_point1(self):
        assert self.pt1 is not None
        assert self.pt1.x == 25

    def test_point2(self):
        assert self.pt2 is not None
        assert self.pt2.x == 1
        assert self.pt2.y == 12
        assert self.pt2.z == 12
