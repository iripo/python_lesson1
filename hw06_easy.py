# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round((abs((b_x - a_x)**2 + (b_y - a_y)**2))**0.5,2)
        self.AC = round((abs((c_x - a_x)**2 + (c_y - a_y)**2))**0.5,2)
        self.BC = round((abs((c_x - b_x)**2 + (c_y - b_y)**2))**0.5,2)

    def Pabc(self):
        self.Pabc = round((self.AB+self.AC+self.BC),2)
        return (self.Pabc)

    def Sabc(self):
        p = self.Pabc/2
        self.Sabc = round((p*(p-self.AB)**(p-self.AC)**(p-self.BC))**0.5,2)
        return (self.Sabc)


    def height(self):
        self.height = round(self.Sabc*2/ self.AC,2)
        return (self.height)


coord = Triangle(1,2,3,4,5,6)


print('Длина сторон треугольника АВ = {}, AС = {}, BС = {}'.format(coord.AB, coord.AC,coord.BC))
print('Периметр треугольника АВС равен {}'.format(coord.Pabc()))
print('Площадь треугольника АВС равна {}'.format(coord.Sabc()))
print('Высота треугольника АВС (из точки В) равна {}'.format(coord.height()))



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        self.AB = round((abs((b_x - a_x)**2 + (b_y - a_y)**2))**0.5,2)
        self.AC = round((abs((c_x - a_x)**2 + (c_y - a_y)**2))**0.5,2)
        self.BC = round((abs((c_x - b_x)**2 + (c_y - b_y)**2))**0.5,2)
        self.CD = round((abs((d_x - c_x)**2 + (d_y - c_y)**2))**0.5,2)
        self.AD = round((abs((d_x - a_x)**2 + (d_y - a_y)**2))**0.5,2)
        self.BD = round((abs((d_x - b_x)**2 + (d_y - b_y)**2))**0.5,2)

    def RavineTrapeze(self):
        if self.AC == self.BD:
            return True
        return False

    def Pabcd(self):
        self.Pabcd = round((self.AB+self.BC+self.CD+self.AD),2)
        return (self.Pabcd)
 
    def Sabcd(self):
        self.Pabc = round((self.AB+self.AC+self.BC),2)
        p = self.Pabc/2
        self.Sabc = round((p*(p-self.AB)**(p-self.AC)**(p-self.BC))**0.5,2)
        self.Pacd = round((self.AD+self.AC+self.BD),2)
        p = self.Pacd/2
        self.Sacd = round((p*(p-self.AD)**(p-self.AC)**(p-self.BD))**0.5,2)
        self.Sabcd = (self.Sabc + self.Sacd)
        return (self.Sabcd)
 

coordT = Trapeze(5,5,4,4,6,6,8,8)


print('Является ли трапеция равнобочной {}'.format(coordT.RavineTrapeze()))
print('Длина сторон трапеции АВ = {}, BС = {}, СD = {}, AD = {}'.format(coordT.AB, coordT.BC,coordT.CD,coordT.AD))
print('Периметр трапеции АВСD равен {}'.format(coordT.Pabcd()))
print('Площадь трапеции АВСВ равна {}'.format(coordT.Sabcd()))


