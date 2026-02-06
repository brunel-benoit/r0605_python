from vaches.domain.Vache import Vache
from vaches.domain.errors.exception import InvalidVacheException

class VacheALait(Vache):

    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 50.0

    def __init__(self, petitNom: str, poids: float):
        super().__init__(petitNom, poids)

        self.lait_disponible = 0.0
        self.lait_total_produit = 0.0
        self.lait_total_traite = 0.0


    def ruminer(self):

        if self.panse <= 0:
            raise InvalidVacheException()

        lait_produit = self.panse * VacheALait.RENDEMENT_LAIT


        if self.lait_disponible + lait_produit > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException()

        self.lait_disponible += lait_produit
        self.lait_total_produit += lait_produit
        self.panse = 0.0

        return lait_produit


    def traire(self, litres: float):

        if litres <= 0:
            raise InvalidVacheException()

        if litres > self.lait_disponible:
            raise InvalidVacheException()

        self.lait_disponible -= litres
        self.lait_total_traite += litres

        return litres

    def brouter(self, quantite: float, nourriture=None):

        if nourriture is not None:
            raise InvalidVacheException()

        super().brouter(quantite)


    def __str__(self):

        base = (
            f"Nom : {self.petitNom}\n"
            f"Poids : {self.poids} kg\n"
            f"Panse : {self.panse}\n"
        )

        lait = (
            f"Lait disponible : {self.lait_disponible} L\n"
            f"Lait total produit : {self.lait_total_produit} L\n"
            f"Lait total trait : {self.lait_total_traite} L"
        )

        return base + lait

