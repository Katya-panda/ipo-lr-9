#from collision.isCorrectRect import isCorrectRect  # импортируем функцию isCorrectRect из модуля collision для проверки корректности прямоугольника
#from collision.intersectionAreaRect import intersectionAreaRect  # импортируем функцию intersectionAreaRect для вычисления площади пересечения двух прямоугольников
#def intersectionAreaRect(rect1, rect2):
    # проверка корректности первого и второго прямоугольников
    # используем функцию isCorrectRect, чтобы убедиться, что координаты прямоугольников корректны
    # если координаты некорректны, вызываем исключение ValueError с сообщением об ошибке
  #  if not isCorrectRect(rect1):
 #       raise ValueError("1й прямоугольник некоректный")
#    if not isCorrectRect(rect2):
   #     raise ValueError("2й прямоугольник некоректный")
    # распаковка координат из списка:
    # извлекаем координаты левого нижнего и верхнего правого углов первого прямоугольника
  #  (x1_min, y1_min), (x1_max, y1_max) = rect1
    # извлекаем координаты левого нижнего и верхнего правого углов второго прямоугольника.
 #   (x2_min, y2_min), (x2_max, y2_max) = rect2
    # вычисление перекрывающейся области по оси x:
    # определяем левую границу перекрытия как максимальную из минимальных координат по x (наибольшее из x1_min и x2_min)
    # определяем правую границу перекрытия как минимальную из максимальных координат по x (наименьшее из x1_max и x2_max)
    # если левая граница больше правой, значит перекрытия нет, и перекрывающаяся область по x равна 0
#    x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min))
    # вычисление перекрывающейся области по оси y:
    # определяем нижнюю границу перекрытия как максимальную из минимальных координат по y (наибольшее из y1_min и y2_min)
    # определяем верхнюю границу перекрытия как минимальную из максимальных координат по y (наименьшее из y1_max и y2_max)
    # если нижняя граница больше верхней, значит перекрытия нет, и перекрывающаяся область по y равна 0
#    y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min))
   # площадь пересечения (площадь перекрывающейся области = произведению перекрывающихся областей по осям x и y):
#    return x_overlap * y_overlap



from collision.isCorrectRect import isCorrectRect  # Используем относительный импорт
from .intersectionAreaRect import intersectionAreaRect  # Используем относительный импорт

def intersectionAreaMultiRect(rectangles):
    # Проверка корректности всех прямоугольников
    if not all(isCorrectRect(rect) for rect in rectangles):
        raise ValueError("Один или несколько прямоугольников некоректны")

    total_area = 0
    # Вычисление общей площади пересечения всех прямоугольников
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            total_area += intersectionAreaRect(rectangles[i], rectangles[j])

    return total_area