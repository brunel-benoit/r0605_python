
from vaches.exception import InvalidVacheException

AGE_MAX = 25
POIDS_MIN = 2
POIDS_MAX = 10000
PANSE_MAX = 50

class Vache:



    def __init__(self, petitNom:str, poids:float, age:int):

        if not petitNom or petitNom.strip() == "":
            raise InvalidVacheException("le nom peut pas etre vide")

        if  age < 0 or age > AGE_MAX:
            raise InvalidVacheException("l'age doit etre entre 0 et 25 ans")

        if poids < POIDS_MIN:
            raise InvalidVacheException("erreur dans le poids")

        self.petitNom = petitNom
        self.poids = poids
        self.age = age
        self.panse = 0


    def brouter(self, quantite: float,  nourriture=None):

        if nourriture is not None:
            raise InvalidVacheException("La vache ne peut pas brouter de nourriture ")


        if quantite <= 0:
            raise InvalidVacheException("La quantite doit etre positive.")
        self.panse += quantite