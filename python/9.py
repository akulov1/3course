import math


class Figure:
    def __init__(self, ident):
        self.ident = ident

    def get_name(self):
        return self.ident

    def move(self,dx,dy):
        try:
            if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
                raise Exception('Координаты должны быть числами')

            self.points = [(x + dx, y + dy) for x, y in self.points]
            print(f'{self.ident} перемещен на {dx} по Х, на {dy} по Y')
        except Exception as e:
            print(f"Ошибка сдвига {self.ident}: {e}")

    def area(self):
        raise NotImplementedError('Этот метод должен быть реализован в классах-потомках!')

    def get_coords(self):
        return self.points



class Triangle(Figure):
    def __init__(self,ident,points):
        super().__init__(ident)
        if len(points) != 3:
            raise Exception("У треугольника должно быть 3 точки")
        self.points = points

    def area(self):
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        x3, y3 = self.points[2]
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

class Quad(Figure):
    def __init__(self, ident, points):
        super().__init__(ident)
        if len(points) != 4:
            raise Exception("У квадрата должно быть 4 точки")
        self.points = points

    def area(self):
        x1, y1 = self.points[0]
        x2, y2 = self.points[1]
        a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return a*a

triangle = Triangle('triangle', ((1,0), (2,3), (3,-1)))
square = Quad('quad',((0,0),(0,2),(2,2),(2,0)))

triangle.get_name()

def compare(t1,t2):
    area1 = t1.area()
    area2 = t2.area()
    if area1>area2:
        return f'{t1.get_name()} больше {t2.get_name()}'
    elif area2>area1:
        return f'{t2.get_name()} больше {t1.get_name()}'
    else:
        return f'{t1.get_name()} и {t2.get_name()} равны между собой'

print(compare(triangle,square))

print()

print(triangle.get_coords())
triangle.move(1,2)
print(triangle.get_coords())

print()

print(square.get_coords())
square.move(2,3)
print(square.get_coords())