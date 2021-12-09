from Firma import Firma

class Abteilungen(Firma):
    def __init__(self, firma, abteilung):
        super().__init__(firma)
        self.abteilung = abteilung