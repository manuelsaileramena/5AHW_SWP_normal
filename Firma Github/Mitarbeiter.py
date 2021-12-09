from Person import Person

class Mitarbeiter(Person):
    def __init__(self, firma, abteilung, vorname, nachname, geschlecht, gruppe):
        super().__init__(firma, abteilung, vorname, nachname, geschlecht)
        self.gruppe = gruppe

