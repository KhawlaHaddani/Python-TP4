class Batiment:
    def __init__(self , adr):
        self.__adresse = adr
    # getter
    def get_adresse(self):
        return self.__adresse
    # setter
    def set_adresse(self , a):
        self.__adresse = a
    def __str__(self):
        return f"l'adresse du batiment est :  {self.__adresse}"

class Maison(Batiment):
    def __init__(self , adr , nbr):
        super().__init__(adr)
        self.__nbPieces = nbr
    def get_nbPieces(self):
        return self.__nbPieces
    def set_nbPieces(self , n):
        self.__nbPieces = n
    def __str__(self):
        return f"adresse de maison est : {self.get_adresse()} et nombre de piceces est : {self.__nbPieces}"

class Immeuble(Batiment):
    def __init__(self , adr , nbr):
        super().__init__(adr)
        self.__nbAppart = nbr
    def get_nbAppart(self):
        return self.__nbAppart
    def set_nbAppart(self , n):
        self.__nbAppart = n
    def __str__(self):
        return f"Adresse de l'immeuble est : {self.get_adresse()} et nombre d'appartements est : {self.__nbAppart}"
    
# Test des classes
Bat = Batiment("550 Rue de batiment")
print(Bat)

maison1 = Maison("123 Rue de la Maison", 5)
print(maison1)

immeuble1 = Immeuble("456 Rue de l'Immeuble", 10)
print(immeuble1)