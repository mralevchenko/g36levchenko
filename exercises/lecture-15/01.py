# test_get_area_rectangle.py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height must be non-negative")
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class TestGetAreaRectangle:
    def test_normal_case(self):
        """Test area calculation for positive dimensions"""
        rectangle = Rectangle(2, 3)
        assert rectangle.get_area() == 6, "incorrect area"

    def test_negative_case(self):
        """Expect exception for negative dimensions"""
        rectangle = Rectangle(-1, 2)
        try:
            rectangle.get_area()
            assert False, "Expected ValueError for negative dimensions"
        except ValueError as e:
            assert str(e) == "Width and height must be non-negative"

