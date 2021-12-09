from Firma import Firma
from Abteilungen import Abteilungen
from Person import Person
from Mitarbeiter import Mitarbeiter
from Gruppenleiter import Gruppenleiter

def firmaErstellen(firma):
    fir = Firma(firma)
    return fir

def abteilungErstellen(firma, abteilung):
    abt = Abteilungen(firma, abteilung)
    return abt

def abteilungHinzufügen(benutzerF, benutzerA):
    a = abteilungErstellen(benutzerF, benutzerA)
    abteilungen.append(a.abteilung)

def anzahlAbteilungen(d):
    n = len(d)
    print("Anzahl der Abteilungen: " + str(n))
    return d

def personErstellen(firma, abteilung, vorname, nachname, geschlecht):
    pers = Person(firma, abteilung, vorname, nachname, geschlecht)
    return pers

def personHinzufügen(a, b, c, d, e):
    b = personErstellen(a, b, c, d, e)
    personen.append(b.geschlecht)

def anzahlGeschlecht(e):
    n = len(e)
    f = 0
    m = 0
    for i in range(n):
        g = e[i]
        if g == "m":
            m += 1
        else:
            f += 1
    print("Männer: " + str((m / n) * 100) + " %")
    print("Frauen: " + str((f / n) * 100) + " %")

def mitarbeiterErstellen(a, b, c, d, e, f):
    mitarbeiter = Mitarbeiter(a, b, c, d, e, f)
    return mitarbeiter

def mitarbeiterHinzufügen(a, b, c, d, e, f):
    c = Person(a, b, c, d, e, f)
    personen.append(c.geschlecht)
    personen.append(c.firma)

def anzahlMitarbeiter(f):
    n = len(f)
    print("Anzahl Mitarbeiter: " + str(n))

def gruppenleiterErstellen(a, b, c, d, e, f, g):
    gruppenleiter = Gruppenleiter(a, b, c, d, e, f, g)
    return gruppenleiter

def gruppenleiterHinzufügen(a, b, c, d, e, f, g):
    gl = gruppenleiterErstellen(a, b, c, d, e, f, g)
    personen.append(gl.geschlecht)
    mitarbeiter.append(gl.firma)
    gruppenleiters.append(gl.gruppenleiterId)

def anzahlGruppenleiter(g):
    n = len(g)
    print("Anzahl Gruppenleiter: " + str(n))

if __name__ == '__main__':
    abteilungen = []
    personen = []
    mitarbeiter = []
    gruppenleiters = []
    benutzerF = input("Name der Firma: ")
    cc = firmaErstellen(benutzerF)
    pers = False
    while pers == False:
        person = input("Eine Person hinzufügen: Ja[j], Nein[n]: ")
        if person.lower() == "j":
            personenAbteilung = input("Abteilung in der die Person arbeitet: ")
            personenVorname = input("Vorname der Person: ")
            personenNachname = input("Nachname der Person: ")
            personenGeschlecht = input("Gender of the person: ")
            personHinzufügen(benutzerF, personenAbteilung, personenVorname, personenNachname, personenGeschlecht)
        if person.lower() == "n":
            pers = True
    mit = False
    while mit == False:
        mitarbeiter = input("Mitarbeiter hinzufügen: Ja[j], Nein[n]: ")
        if mitarbeiter.lower() == "j":
            mitarbeiterAbteilung = input("Abteilung in der der Mitarbeiter arbeitet: ")
            mitarbeiterVorname = input("Vorname des Mitarbeiters: ")
            mitarbeiterNachname = input("Nachname des Mitarbeiters: ")
            mitarbeiterGeschlecht = input("Geschlecht des Mitarbeiters: ")
            mitarbeiterGruppe = int(input("Gruppe des Mitarbeiters: "))
            mitarbeiterHinzufügen(benutzerF, mitarbeiterAbteilung, mitarbeiterVorname, mitarbeiterNachname, mitarbeiterGeschlecht, mitarbeiterGruppe)
        if mitarbeiter.lower() == "n":
            mit = True
    gl = False
    while gl == False:
        gruppenleiter = input("Gruppenleiter hinzufügen: Ja[j], Nein[n]: ")
        if gruppenleiter.lower() == "j":
            gruppenleiterAbteilung = input("Abteilung in der der Gruppenleiter arbeitet: ")
            gruppenleiterVorname = input("Vorname des Gruppenleiters: ")
            gruppenleiterNachname = input("Nachname des Gruppenleiters: ")
            gruppenleiterGeschlecht = input("Geschlecht des Gruppenleiters: ")
            gruppenleiterGruppe = int(input("Gruppe des Gruppenleiters: "))
            gruppenleiterId = int(input("Gruppenleiter ID ist: "))
            gruppenleiterHinzufügen(benutzerF, gruppenleiterAbteilung, gruppenleiterVorname, gruppenleiterNachname, gruppenleiterGeschlecht, gruppenleiterGeschlecht, gruppenleiterGruppe, gruppenleiterId)
        if gruppenleiter.lower() == "n":
            gl = True


    anzahlMitarbeiter(mitarbeiter)
    anzahlGruppenleiter(gruppenleiters)
    anzahlAbteilungen(abteilungen)
    anzahlGeschlecht(personen)








