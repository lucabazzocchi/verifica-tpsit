class ImpiantoSolare():
   def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None
       self.codice = codice
       self.modello = modello
       self.localita = localita
       self.potenza_massima_kw = potenza_massima_kw
       self.stato = stato
       self.pannelli = list[PannelloFotovoltaico] = []
       return None
    
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None
        if pannello.potenza_kw > self.potenza_massima_kw
            raise ValueError("potenza massima superata")
        if pannello.codice in self.pannelli
            raise ValueError("codice gia presente")
        self.pannelli.append(pannello)
        return None
    
    def potenza_pannelli(self) -> float
        float sum = 0.0
        for pannello in self.pannelli
            sum += pannello.potenza_kw
        return sum
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico
        for pannello in self.pannelli
            if pannello.codice == codice
            return pannello
        return None
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico
        for pannello in self.pannelli
            pannello_eliminato = cerca_pannello(codice)
            if pannello_eliminato == None
                return None
            self.pannelli.remove(pannello_eliminato)
            return pannello_eliminato
    
    def pannelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]
        result = list[PannelloFotovoltaico] = []
        for pannello in self.pannelli
            if pannello.potenza_kw <= potenza_massima
                result.append(pannello)
        return result
    #prova per commit
    