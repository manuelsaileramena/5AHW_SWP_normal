from Person import Person

class Gruppenleiter(Person):
    def __init__(self, firma, abteilung, vorname, nachname, geschlecht, gruppe, gruppenleiterId):
        super().__init__(firma, abteilung, vorname, nachname, geschlecht, gruppe)
        self.gruppenleiterId = gruppenleiterId

