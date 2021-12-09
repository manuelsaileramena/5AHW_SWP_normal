from Abteilungen import Abteilungen

class Person(Abteilungen):
    def __init__(self, firma, abteilung, vorname, nachname, geschlecht):
        super().__init__(firma, abteilung)
        self.vorname = vorname
        self.nachname = nachname
        self.geschlecht = geschlecht

