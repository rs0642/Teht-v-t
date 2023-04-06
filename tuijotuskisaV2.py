import random
import time

#Käyttää Peikkoa lähteenä

class Olento(): 
    def __init__(self, nimi, katseen_voima, rohkeus):
        self.nimi = nimi
        self.rohkeus = rohkeus + random.randint(4, 8)
        self.katseen_voima = katseen_voima + random.randint(2, 4)


class Peikko(Olento): 
    """Luokka, joka kuvaa Peikon.

    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int

    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("UUUH", "JAAHH", "BRUHH", "HUG", "HUUUUU", "ZAZA", "barra", "Bazz", "Raggf", "Rudzii")
    RIEMUTAVUT = ("Aghrr", "Ughrrr", "Ourghrrr", "Drarsaa", "Braraa", "Dzaaa", "Graaa", "Guraa", "Rahaa", "Urghaa", "Raaa")

    def __init__(self, rohkeus = 4, katseen_voima = 4):
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = rohkeus 
        katseen_voima = katseen_voima
        super().__init__(nimi, rohkeus, katseen_voima)

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

#Uusi luokka, perii Peikon

class Vuorenpeikko(Peikko):
    def __init__(self, rohkeus = 3, katseen_voima = 6):
        super().__init__(rohkeus, katseen_voima)

    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    #Uusi luokka, perii Peikon

class Luolapeikko(Peikko):

    def __init__(self, rohkeus = 8, katseen_voima = 8):
        super().__init__(katseen_voima, rohkeus)

    NIMITAVUT = ("Kana", "Possu", "Porkkana", "Sipuli", "Kananmuna", "IsoBritannia", "Barbababa", "Bazhhh", "Raghfueashfhb", "Rudzfhsfh")
    RIEMUTAVUT = ("Aghahhah", "Ughahahah", "Ourghahahha", "Drarhahah", "Brarhahha", "ahahaha", "ahahaha", "Gurahahaha", "Rahahah", "Urghahaha", "Raahaha")

class Sankari(Olento):
    def __init__(self, nimi):
        self.nimi = nimi
        self.rohkeus = random.randint(3, 10)
        self.katseen_voima = random.randint(2, 8)
        """Tässä koodi pyytää nimeä ja arpoo rohkeuden ja voiman"""

    def arvo_hurraus(self):
        hurraukset = ["Jee", "Wohoo", "Jeii","Mahtavaa", "Hyvä"]
        return random.choice(hurraukset)
    """Tässä koodi ottaa satunnaisen hurrauksen"""

def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.

    :param olio: hurraava olio
    """
    print('%s: "%s!"' % (olio.nimi, olio.arvo_hurraus()))

def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.

    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print("ja %s räpäyttää!" % rapayttaja.nimi)
        else:
            print("ja %s karkaa!" % rapayttaja.nimi)
    else:
        print("eikä kummankaan silmä rävähdä!")

def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea

sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print("Sankarimme %s kävelee kohti seikkailua." % sankarin_tiedot)
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.
    # Arpoo ketä peikkoa vastaan taistellaan
    peikkolajit = [Peikko, Luolapeikko, Vuorenpeikko]
    valittu_peikko = random.choice(peikkolajit)
    peikko = valittu_peikko()
    peikon_tiedot = peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print("Vastaan tulee hurja %s!" % peikon_tiedot)
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print("%s herää sängystään hikisenä - onneksi se oli vain unta!" % sankari.nimi)
