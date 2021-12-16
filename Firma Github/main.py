
if __name__ == '__main__':
    class Person:
        def __init__(self, vorname, nachname, alter, männlich):
            self.vorname = vorname
            self.nachname = nachname
            self.alter = alter
            self.männlich = männlich


    class Mitarbeiter(Person):
        def __init__(self, vorname, nachname, alter, geschlecht, gehalt):
            super().__init__(vorname, nachname, alter, geschlecht)
            self.gehalt = gehalt


    class Gruppenleiter(Mitarbeiter):
        def __init__(self, vorname, nachname, alter, geschlecht, gehalt, gruppe):
            super().__init__(vorname, nachname, alter, geschlecht, gehalt)
            self.gruppe = gruppe


    class Abteilung:
        def __init__(self, name):
            self.name = name

        gruppenleiter = Gruppenleiter("", "", 0, True, 0, "")
        mitarbeiter = []


    class Firma:
        abteilungen = []


    m1 = Mitarbeiter("Sabrina", "Laichner", 20, False, 2300)
    m2 = Mitarbeiter("Martin", "Muglach", 23, True, 2600)
    g1 = Gruppenleiter("Julian", "Egger", 32, True, 3500, "C")
    a1 = Abteilung("Einkauf")
    a1.gruppenleiter = g1
    a1.mitarbeiter.append([m1, m2])
    f1 = Firma()
    f1.abteilungen.append([a1])

    def anzahlAbteilungen(fir=Firma()):
        return fir.abteilungen.count()

    def anzahlMitarbeiter(fir=Firma()):
        anzahl = 0
        for a in fir.abteilungen:
            for b in a:
                for c in b.mitarbeiter:
                    anzahl += len(c)
        return anzahl

    def anzahlGruppenleiter(fir=Firma()):
        anzahl = 0
        for a in fir.abteilungen:
            anzahl = [anzahl for b in a if b.gruppenleiter is not None]
            anzahl = len(anzahl)
            #for b in a:
                #if b.gruppenleiter is not None:
                    #anzahl += 1
        return anzahl

    def grössteAbteilung(fir=Firma()):
        anzahl = 0
        grösAnzahl = 0
        abt = None
        for a in fir.abteilungen:
            for b in a:
                if b.gruppenleiter is not None:
                    anzahl += 1
                for c in b.mitarbeiter:
                    anzahl += len(c)
                if grösAnzahl < anzahl:
                    grösAnzahl = anzahl
                    abt = b
                anzahl = 0
        return abt.name

    def anzahlMänner(fir=Firma()):
        gesamt = 0
        anzahl = 0
        for a in fir.abteilungen:
            for b in a:
                if b.gruppenleiter is not None:
                    if b.gruppenleiter.männlich:
                        anzahl += 1
                    gesamt += 1
                for c in b.mitarbeiter:
                    for d in c:
                        if d.männlich:
                            anzahl += 1
                        gesamt += 1

        return anzahl / gesamt * 100


    print("Mitarbeiter: ", anzahlMitarbeiter(f1))
    print("Gruppenleiter: ", anzahlGruppenleiter(f1))
    print("Größte Abteilung: ", grössteAbteilung(f1))
    print("männlicher Anteil: ", anzahlMänner(f1), "%")



