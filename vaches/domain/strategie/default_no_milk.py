import vaches.domain.strategie.protocole.rumination_strategy

class NoMilkStrategy:

    def calculer_lait(self, vache:"Vache", panse_avant:float) -> float:
        return 0.0

    def stocker_lait(self, vache:"vache", lait:float) -> None:
        return

    def post_rumination(self, vache:"vache", panse_avant:float, lait:float) -> None:
        return


