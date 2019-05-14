# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#####Длины сторон |AB|=(xB−xA)2+(yB−yA)2−−−−−−−−−−−−−−−−−−−√,|AC|=(xC−xA)2+(yC−yA)2−−−−−−−−−−−−−−−−−−−√,|BC|=(xC−xB)2+(yC−yB)2−−−−−−−−−−−−−−−−−−−√.
#####Площадь SABC=|(xB−xA)(yC−yA)−(xC−xA)(yB−yA)|2

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = math.sqrt(int(math.abs(((b_x - a_x)**2) + ((b_y - a_y)**2))))
        self.AC = math.sqrt(int(math.abs(((c_x - a_x)**2) + ((c_y - a_y)**2))))
        self.BC = math.sqrt(int(math.abs(((c_x - b_x)**2) + ((c_y - b_y)**2))))

    def Pabc(self):
        self.Pabc = round(math.sum(self.AB,self.AC,self.BC),2)
        return (self.Pabc)

    def Sabc(self):
        self.Sabc =  (round(math.abs((b_x-a_x)*(c_y-a_y)-(c_x-a_x)*(b_y-a_y))/2,2)
        return (self.Sabc)


    def height(self):
        self.height = round(Sabc*2/ self.AC,2)
        return (self.height)


coord = Triangle(5,5,4,4,6,6)


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
        self.AB = math.sqrt(int(math.abs(((b_x - a_x)**2) + ((b_y - a_y)**2))))
        self.BC = math.sqrt(int(math.abs(((c_x - b_x)**2) + ((c_y - b_y)**2))))
		self.CD = math.sqrt(int(math.abs(((d_x - c_x)**2) + ((d_y - c_y)**2))))
        self.AD = math.sqrt(int(math.abs(((d_x - a_x)**2) + ((d_y - a_y)**2))))
		self.AС = math.sqrt(int(math.abs(((с_x - a_x)**2) + ((с_y - a_y)**2))))
		self.BD = math.sqrt(int(math.abs(((d_x - b_x)**2) + ((d_y - b_y)**2))))

    def RavineTrapeze(self):
        if self.AC == self.BD:
            return True
        return False

	def Pabcd(self):
        self.Pabcd = round(math.sum(self.AB,self.BC,self.CD,self.AD),2)
        return (self.Pabcd)
 
    def Sabcd(self):
        self.Sabc =  (round(math.abs((b_x-a_x)*(c_y-a_y)-(c_x-a_x)*(b_y-a_y))/2,2)
		self.Sacd =  (round(math.abs((c_x-a_x)*(d_y-a_y)-(d_x-a_x)*(c_y-a_y))/2,2)
		self.Sabcd = sum(self.Sabc + self.Sacd)
        return (self.Sabcd)
 

coordT = Trapeze(5,5,4,4,6,6,8,8)


print('Является ли трапеция равнобочной {}'.format(coordT.RavineTrapeze()))
print('Длина сторон трапеции АВ = {}, BС = {}, СD = {}, AD = {}'.format(coordT.AB, coordT.BC,coordT.CD,coordT.AD))
print('Периметр трапеции АВСD равен {}'.format(coordT.Pabcd()))
print('Площадь трапеции АВСВ равна {}'.format(coordT.Sabcd()))


