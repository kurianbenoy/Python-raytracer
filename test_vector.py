from vector import Vector


class TestVectors:
    def setup(self):
        self.x = Vector(1, -2, -2)
        self.y = Vector(3, 6, 9)

    def test_vector(self):
        assert self.x is not None

    def test_dotproduct(self):
        assert self.x.dot_product(self.y) == -27

    def test_magnitude(self):
        assert self.x.magnitude() == 3

    def test_mutiplication(self):
        sum = self.x * 2
        assert sum.x == 2
        assert sum.magnitude() == 6

    def test_division(self):
        answer = self.y / 3
        assert answer.x == 1
        assert answer.y == 2
        # assert sum == Vector(2, -4, -4)

        # test1 = 2* self.y
        # assert test1 == Vector(6, 12, 18)
