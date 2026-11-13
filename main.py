from impianto import ImpiantoSolare
from pannello import PannelloFotovoltaico

class Main()
    def __init__(self, impianti: list[ImpiantoSolare]) -> None
        self.impianti = impianti
        return None
    
    def registro_impianto(self, impianto: ImpiantoSolare) -> None
        if impianto in self.impianti
            raise ValueError("impianto gia presente")
        impianto.append(impianto)
        return None
    def 