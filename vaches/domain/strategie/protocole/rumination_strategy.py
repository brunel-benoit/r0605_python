from typing import Protocol

class RuminationStrategy(Protocol) :

    def calculer_lait(self, vache: "Vache", panse_avant: float) -> float :
        ...

    def stocker_lait(self, vache: "Vache", lait: float) -> None :
        ...

    def post_rumination(self, vache: "Vache", panse_avant: float, lait: float) -> None :
        ...

