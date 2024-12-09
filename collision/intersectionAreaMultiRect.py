from .isCorrectRect import isCorrectRect  # используем относительный импорт для получения функции isCorrectRect из текущего пакета
from .intersectionAreaRect import intersectionAreaRect  # используем относительный импорт для получения функции intersectionAreaRect из текущего пакета
def intersectionAreaMultiRect(rectangles):
    # Проверка корректности всех прямоугольников:
    # функция all() проверяет, что все прямоугольники корректны, вызывая функцию isCorrectRect для каждого прямоугольника в списке rectangles
    # если хотя бы один из прямоугольников некорректен, вызывается исключение ValueError
    if not all(isCorrectRect(rect) for rect in rectangles):
        raise ValueError("Один или несколько прямоугольников некоректны")
    total_area = 0  # инициализируем переменную для общей площади пересечения
    # вычисление общей площади пересечения всех прямоугольников:
    # перебираем все пары прямоугольников (rect1 и rect2) в списке rectangles
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            # lля каждой пары прямоугольников вызываем функцию intersectionAreaRect,чтобы получить площадь их пересечения
            total_area += intersectionAreaRect(rectangles[i], rectangles[j])
    # возвращаем общую площадь пересечения всех прямоугольников
    return total_area