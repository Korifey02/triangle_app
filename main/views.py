from django.shortcuts import render, redirect

from .utils.triangle import RightTriangle
from .models import Triangle
from .enums import ActionType


def get_home_page(request):
    return render(request, 'home.html')


def get_calculator_page(request):
    return render(request, 'calculator.html')


def get_triangles_from_db(request):
    triangles_from_db = Triangle.objects.all()
    # Создаем экземпляры класса RightTriangle для каждого объекта из базы данных
    triangles = [RightTriangle(triangle.first_side, triangle.second_side) for triangle in triangles_from_db]
    return render(request, 'triangles_from_db.html', {'triangles': triangles})


def get_calculated_results(request):
    if request.method == 'POST':
        side_a = float(request.POST.get('side_a'))
        side_b = float(request.POST.get('side_b'))
        triangle = RightTriangle(side_a, side_b)

        if request.POST.get('form_mode') == ActionType.CALCULATE.value:
            return render(request, 'calculator.html', {
                'hypotenuse': triangle.hypotenuse,
                'area': triangle.area,
                'perimeter': triangle.perimeter,
            })

        # Создаем экземпляр треугольника и сохраняем в базе данных
        Triangle.objects.create(first_side=side_a, second_side=side_b)
        return redirect('triangles_from_db')

    return render(request, 'calculator.html', {
        'hypotenuse': None,
        'area': None,
        'perimeter': None,
    })
