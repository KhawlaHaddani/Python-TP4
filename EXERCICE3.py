class AbstractEmploye:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
    # getters
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    # setters 
    def set_nom(self, nom):
        self.__nom = nom
    def set_prenom(self, prenom):
        self.__prenom = prenom
    def gains(self):
        pass
    def __str__(self):
        return f"Employé : {self.__prenom} {self.__nom}"
class Patron(AbstractEmploye):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.__salaire = salaire
    # getter
    def get_salaire(self):
        return self.__salaire
    # setter
    def set_salaire(self, sal):
        self.__salaire = sal
    def gains(self):
        return self.__salaire
    def __str__(self):
        return f"Patron : {self.get_prenom()} {self.get_nom()} avec un salaire de {self.gains()}"

class TravailleurCommission(AbstractEmploye):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.__salaire = salaire
        self.__commission = commission
        self.__quantite = quantite
    # getters
    def get_salaire(self):
        return self.__salaire
    def get_quantite(self):
        return self.__quantite
    def get_commission(self):
        return self.__commission
    # setters
    def set_salaire(self, s):
        self.__salaire = s
    def set_commission(self, commission):
        self.__commission = commission
    def set_quantite(self, qte):
        self.__quantite = qte
    def gains(self):
        return self.__salaire + (self.__commission * self.__quantite)
    def __str__(self):
        return f"Travailleur à la commission: {self.get_prenom()} {self.get_nom()} avec un salaire de {self.gains()}"

class TravailleurHoraire(AbstractEmploye):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.__retribution = retribution
        self.__heures = heures
    # getters
    def get_retribution(self):
        return self.__retribution
    def get_heures(self):
        return self.__heures
    
    # setters
    def set_retribution(self, rest):
        self.__retribution = rest
    def set_heures(self, h):
        self.__heures = h
    def gains(self):
        return self.__retribution * self.__heures
    def __str__(self):
        return f"Travailleur horaire: {self.get_prenom()} {self.get_nom()} avec un salaire de {self.gains()}"
    
patron = Patron("Haddani", "khawla", 1000000)
travaille_commission = TravailleurCommission("Alaoui", "laila", 1000, 5, 100)
travaille_h = TravailleurHoraire("Alaoui", "salma", 20, 160)

employes = [patron, travaille_commission, travaille_h]

for employe in employes:
    print(employe)
    #print(f"Gains : ${employe.gains()}")
    print()