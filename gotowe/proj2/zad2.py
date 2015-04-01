import random
from time import sleep

class Samolot:
        kat = 0

        def korekta(self,zadany):

                if self.kat+5<=zadany:
                        print "Korekcja w prawo o \033[93m  %d \033[0m  stopni" % 5
                        self.kat+=5
                elif self.kat+5>zadany and self.kat<zadany:
                        print "Korekcja w prawo o  \033[93m  %d \033[0m  stopni" % (zadany-self.kat)
                        self.kat = zadany
                elif self.kat == zadany:
                        print "\033[92m Wszytsko jest ok \033[0m"
                elif self.kat-5>=zadany:
                        print "Korekcja w lewo o \033[93m  %d \033[0m  stopni" % 5
                        self.kat-=5
                elif self.kat-5<zadany and self.kat>zadany:
                        print "Korekcja w lewo o \033[93m  %d \033[0m  stopni" % (self.kat-zadany)
                        self.kat = zadany

class Dane:
        def odczyt(self):
                blad =  random.randint(-20,20)
                self.zadany = blad
                if blad > 0:
                        print "Nowy kat prawo \033[91m %d \033[0m stopni" % blad
                elif blad < 0:
                        print "Nowy kat lewo o \033[91m %d \033[0m stopni" % -blad
                return blad
                

Awionetka = Samolot()
Urzadzenie = Dane()

kat_zadany = 10
while 1:
        sleep(0.5)
        kat_zadany = Urzadzenie.odczyt()
        sleep(0.5)
        Awionetka.korekta(kat_zadany)
        sleep(0.5)
        Awionetka.korekta(kat_zadany)
        sleep(0.5)
        Awionetka.korekta(kat_zadany)
        sleep(0.5)
        Awionetka.korekta(kat_zadany)

