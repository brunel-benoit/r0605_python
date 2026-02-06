
from vaches.domain.errors.exception import InvalidVacheException

AGE_MAX = 25
AGE_MINI_NAISSANCE = 0
POIDS_MIN = 2
POIDS_MAX = 1000.0

RENDEMENT_RUMINATION = 0.25



class Vache:

    def __init__(self, petitNom:str, poids:float):

        if not petitNom or petitNom.strip() == "":
            raise InvalidVacheException("le nom peut pas etre vide")

        if poids < POIDS_MIN:
            raise InvalidVacheException("erreur dans le poids")

        self.petitNom = petitNom
        self.poids = poids
        self.age = AGE_MINI_NAISSANCE
        self.panse = 0


    def brouter(self, quantite: float,  nourriture=None):

        if nourriture is not None:
            raise InvalidVacheException("La vache ne peut pas brouter de nourriture ")


        if quantite <= 0:
            raise InvalidVacheException("La quantite doit etre positive.")


        if self.panse + quantite > Vache.PANSE_MAX:
            raise InvalidVacheException("Erreur sur la panse")

        self.panse += quantite

    def ruminer(self):

        if self.panse <= 0:
            raise InvalidVacheException("Erreur")

        gain = RENDEMENT_RUMINATION*self.panse
        self.poids+=gain
        self.panse= 0.0

    def veillir(self) :
        if self.age>=AGE_MAX:
            raise InvalidVacheException('')
        else :
            self.age+=1



