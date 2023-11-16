class Point:
    def __init__(self , abs , ord):
        self.__x  , self.__y = abs , ord
    # getters
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    # setters
    def set_x(self , x):
        self.__x = x
    def set_y(self , y):
        self.__y = y
    def __str__(self):
        return 'Point({} , {})'.format(self.__x , self.__y) #return f"Point({self.__x}, {self.__y})"
    

class Rectangle(Point):
    def __init__(self , x , y , long , larg ):
        super().__init__(x , y)
        self.__largeur = larg
        self.__longueur = long
    # getters
    def get_largeur(self):
        return self.__largeur
    def get_longueur(self):
        return self.__longueur
    # setters
    def set_largeur(self , largeur):
        self.__largeur = largeur
    def set_longueur(self , longueur):
        self.__longueur = longueur
    def aire(self):
        return self.__largeur * self.__longueur
    def __str__(self):
        return f"Rectangle({self.get_x()}, {self.get_y()}, Longueur: {self.__longueur}, Largeur: {self.__largeur}, Aire: {self.aire()})"
    

class Parallelepipede(Rectangle):
    def __init__(self , x , y ,L , l , h):
        super().__init__(x , y , L , l)
        self.__hauteur = h
    # getter
    def get_hauteur(self):
        return self.__hauteur
    # setter
    def set_hauteur(self , heuteur):
        self.__hauteur = heuteur
    def aire(self):
        return 2 * (super().aire() + self.__hauteur * (self.get_largeur() + self.get_longueur()))
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur
    def __str__(self):
        return f"Parallelepipede({self.get_x()}, {self.get_y()}, Longueur: {self.get_longueur()}, Largeur: {self.get_largeur()}, Hauteur: {self.__hauteur}, Aire: {self.aire()}, Volume: {self.volume()})"


# Tester les classes
point = Point(1, 2)
print(point)

rectangle = Rectangle(1, 2, 3, 4)
print(rectangle)
print("Aire du rectangle : ", rectangle.aire())

parallelepiped = Parallelepipede(1, 2, 3, 4, 5)
print(parallelepiped)
print("Aire du parallelepiped : ", parallelepiped.aire())
print("Volume du parallelepiped : ", parallelepiped.volume())
    
