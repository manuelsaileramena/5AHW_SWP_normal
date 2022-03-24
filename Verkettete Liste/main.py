import random
from array import array
from time import perf_counter_ns as timestamp


class Knoten:
    def __init__(self, inhalt):
        self.vorher = None
        self.inhalt = inhalt
        self.naechste = None


class VerketteteListe:
    def __init__(self):
        self.ende = None
        self.kopf = None
        self.position = None
        return

    def ungeordnete_Suche(self, value):
        derzeitiger_Knoten = self.kopf
        Knoten_Id = 1
        ergebnis = []

        while derzeitiger_Knoten is not None:
            if derzeitiger_Knoten.inhalt == value:
                ergebnis.append(Knoten_Id)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_Id = Knoten_Id + 1

        return ergebnis

    def suche(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        print(list.ungeordnete_Suche(item_value))

    def knotenHinzufügen(self, zahl):
        if isinstance(zahl, [].__class__):
            for i in zahl:
                self.knotenHinzufügen(i)
            return
        Knoten_neu = Knoten(zahl)
        if self.kopf is None:
            self.kopf = Knoten_neu
            self.ende = Knoten_neu
            return

        self.ende.naechste = Knoten_neu
        Knoten_neu.vorher = self.ende
        self.ende = Knoten_neu

    def vorneHinzufügen(self, zahl, zahl_id):
        if not isinstance(zahl, Knoten):
            zahl = Knoten(zahl)
        Knoten_id = 1
        derzeitiger_Knoten = self.kopf

        while derzeitiger_Knoten is not None:
            if Knoten_id == zahl_id:
                zahl.vorher = derzeitiger_Knoten.vorher
                zahl.naechste = derzeitiger_Knoten
                derzeitiger_Knoten.vorher.naechste = zahl
                derzeitiger_Knoten.vorher = zahl

            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_id = Knoten_id + 1

    def vorneLöschen(self, zahl_id):
        Knoten_id = 1
        derzeitiger_Knoten = self.kopf

        while derzeitiger_Knoten is not None:
            if Knoten_id == zahl_id:
                vorKnoten = derzeitiger_Knoten.vorher
                if vorKnoten is self.kopf:
                    self.kopf = derzeitiger_Knoten
                    derzeitiger_Knoten.vorher = None
                    return
                vorKnoten.vorher.naechste = derzeitiger_Knoten
                derzeitiger_Knoten.vorher = vorKnoten.vorher

            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_id = Knoten_id + 1

    def hintenHinzufügen(self, zahl, zahl_id):
        if not isinstance(zahl, Knoten):
            zahl = Knoten(zahl)
        Knoten_id = 1
        derzeitiger_Knoten = self.kopf

        while derzeitiger_Knoten is not None:
            if Knoten_id == zahl_id:
                zahl.vorher = derzeitiger_Knoten
                zahl.naechste = derzeitiger_Knoten.naechste
                derzeitiger_Knoten.naechste.vorher = zahl
                derzeitiger_Knoten.naechste = zahl

            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_id = Knoten_id + 1

    def hintenLöschen(self, zahl_id):
        Knoten_id = 1
        derzeitiger_Knoten = self.kopf

        while derzeitiger_Knoten is not None:
            if Knoten_id == zahl_id:
                naeKnoten = derzeitiger_Knoten.naechste
                if naeKnoten.naechste is self.kopf:
                    naeKnoten.naechste.vorher = derzeitiger_Knoten
                derzeitiger_Knoten.naechste = naeKnoten.naechste

            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_id = Knoten_id + 1

    def ausgabeKnotenHinzufügen(self):
        length = int(input("Geben Sie bitte die gewünschte Länge ein: \n"))
        for i in range(length):
            zahl = random.randint(0, 100)
            self.knotenHinzufügen(zahl)

    def ausgabeVorneHinzufügen(self):
        zahl = int(input("Geben Sie bitte die Zahl, welche vorne hinzugefügt werden soll ein: \n"))
        zahl_ind_vorher = int(input("Vor welchem Index soll diese Zahl eingefügt werden: \n"))
        self.vorneHinzufügen(zahl, zahl_ind_vorher)

    def ausgabeVorneLöschen(self):
        zahl = int(input("Geben Sie bitte den Index, welcher vor diesem Index gelöscht werden soll ein: \n"))
        list.vorneLöschen(zahl)

    def ausgabeHintenHinzufügen(self):
        zahl = int(input("Index vor welchem die Zahl gelöscht werden soll: \n"))
        zahl_ind_naechste = int(input("Hinter welchem Index soll diese Zahl eingefügt werden: \n"))
        list.hintenHinzufügen(zahl, zahl_ind_naechste)

    def ausgabeHintenLöschen(self):
        zahl = int(input("Index hinter welchem die Zahl gelöscht werden soll: \n"))
        list.hintenLöschen(zahl)

    def datenAustaschen(self, zahl1, zahl2):
        zahl = zahl1.inhalt
        zahl1.inhalt = zahl2.inhalt
        zahl2.inhalt = zahl

    """def insertionsortASC(self):
        vorne = self.kopf
        hinten = None
        while vorne != None:
            hinten = vorne.naechste
            while hinten != None and hinten.vorher != None and hinten.inhalt < hinten.vorher.inhalt:
                list.datenAustaschen(hinten, hinten.vorher)
                hinten = hinten.vorher
            vorne = vorne.naechste"""

    def insertionsortASC(self):
        front = self.kopf
        back = None
        while (front != None):
            back = front.naechste
            while (back != None and back.vorher != None and back.inhalt < back.vorher.inhalt):
                self.datenAustaschen(back, back.vorher)
                back = back.vorher
            front = front.naechste

    def insertionsortDESC(self):
        vorne = self.kopf
        hinten = None
        while (vorne != None):
            hinten = vorne.naechste
            while (hinten != None and hinten.vorher != None and hinten.inhalt > hinten.vorher.inhalt):
                self.datenAustaschen(hinten, hinten.vorher)
                hinten = hinten.vorher
            vorne = vorne.naechste

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

    def zufälligeZahlen(self):
        import random
        zahlen = []
        for i in range(10000):
            zahlen.append(random.randint(0, 10000))
        return zahlen


class ArrayList:
    def __init__(self):
        self.arr = []

    def elementHinzufügen(self, zahl):
        arraylist = self.arr
        for i in range(len(zahl)):
            arraylist.append(zahl[i])
        return arraylist

    def sortASC(self):
        array = self.arr
        for i in range(1, len(array)):
            schlüssel = array[i]
            j = i - 1
            while j >= 0 and schlüssel < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = schlüssel
        return array

    def sortDESC(self):
        array = self.arr
        for i in range(1, len(array)):
            schlüssel = array[i]
            j = i - 1
            while j >= 0 and schlüssel > array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = schlüssel
        return array

    def ausgabeArray(self):
        print("Länge : %i" % self.länge_liste())
        arraylist = self.arr
        ausgabe = []
        for i in range(len(arraylist)):
            ausgabe.append(arraylist[i])
        print(ausgabe)

    def länge_liste(self):
        zaehler = 0
        arraylist = self.arr
        for i in range(len(arraylist)):
            zaehler = zaehler + 1
        return zaehler

    def zufälligeZahlen(self):
        import random
        zahlen = []
        for i in range(10000):
            zahlen.append(random.randint(0, 10000))
        return zahlen


if __name__ == '__main__':
    list = VerketteteListe()
    zahl1 = list.zufälligeZahlen()
    list.knotenHinzufügen(zahl1)
    startL = timestamp()
    list.insertionsortASC()
    endeL = timestamp()
    zeitL = endeL - startL
    print("Zeitmessung LinkedList: {:.2f} Sekunden".format(zeitL / 1_000_000_000))

    ar = ArrayList()
    zahl2 = ar.zufälligeZahlen()
    ar.elementHinzufügen(zahl2)
    startA = timestamp()
    ar.sortASC()
    endeA = timestamp()
    zeitA = endeA - startA
    print("Zeitmessung ArrayList: {:.2f} Sekunden".format(zeitA / 1_000_000_000))

    if zeitA < zeitL:
        print("Die Array List war schneller. ")
    else:
        print("Die Linked List war schneller. ")
