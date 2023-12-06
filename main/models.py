from django.db import models


class Triangle(models.Model):
    first_side = models.FloatField('Первый катет')
    second_side = models.FloatField('Второй катет')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def hypotenuse(self):
        return (self.first_side ** 2 + self.second_side ** 2) ** 0.5

    @property
    def area(self):
        return self.first_side * self.second_side / 2

    @property
    def perimeter(self):
        return self.first_side + self.second_side + self.hypotenuse

    def __str__(self):
        return f'A={self.first_side} B={self.second_side} C={self.hypotenuse}'
