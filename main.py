import random

class Knoten:
    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.naechste = None
        return

    def besitzt_Wert(self, wert):
        if self.inhalt == wert:
            return True
        else:
            return False

class VerketteteListe:
    def __init__(self):
        self.kopf = None
        self.position = None
        return

    def ungeordnete_Suche(self, value):
        derzeitiger_Knoten = self.kopf
        Knoten_Id = 1
        ergebnis = []

        while derzeitiger_Knoten is not None:
            if derzeitiger_Knoten.besitzt_Wert(value):
                ergebnis.append(Knoten_Id)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_Id = Knoten_Id + 1

        return ergebnis

    def suche(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        print(list.ungeordnete_Suche(item_value))

    def hintenHinzufügen(self, zahl):
        if not isinstance(zahl, Knoten):
            zahl = Knoten(zahl)
        if self.kopf is None:
            self.kopf = zahl
        else:
            self.position.naechste = zahl
        self.position = zahl
        return

    def randomHinzufügen(self):
        length = int (input("länge "))
        for i in range(length):
            zahl = random.randint(0, 100)
            list.hintenHinzufügen(zahl)

    def listen_länge(self):
        count = 0
        derzeitiger_Knoten = self.kopf

        while derzeitiger_Knoten is not None:
            count = count + 1
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
        return count

    def ausgabe_liste(self):
        derzeitiger_Knoten = self.kopf
        ausgabe = []
        while derzeitiger_Knoten is not None:
            ausgabe.append(derzeitiger_Knoten.inhalt)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
        print(ausgabe)

    def ausgabe(self):
        print("Länge : %i" % list.listen_länge())
        list.ausgabe_liste()

if __name__ == '__main__':
    list = VerketteteListe()
    list.randomHinzufügen()
    list.ausgabe()
    list.suche()


