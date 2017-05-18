#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jednoduchá hra, inspirovaná seriálem Teorie velkého třesku.
Základem je hra, Kámen, Nůžky, Papír.
Tato hra je obohacená o nové možnosti, ve složce je přiřazený obrázek s pravidly.
"""

# import pouzitych modulu
import random

#Funkce
def nazev(cislo):
    if cislo == 0:
        nazev = "Kámen"
    elif cislo == 1:
        nazev = "Spock"
    elif cislo == 2:
        nazev = "Papír"
    elif cislo == 3:
        nazev = "Tapír"
    elif cislo == 4:
        nazev = "Nůžky"
    else:
        nazev = "Neznámá možnost"
    return nazev


pokracovat = True
while pokracovat:

    print "\n"

    """
    Začátek hry
    """
    # Vytiskne možnosti
    print "-" * 60
    print "\n Zde jsou vypsány všechny možnosti, které můžete použít"
    print "\n 0 = Kámen\n 1 = Spock\n 2 = Papír\n 3 = Tapír\n 4 = Nůžky\n"
    print "-" * 60

    # Volba hráče
    cislo_hrace = input('Zvolte možnost:\n')
    nazev_hrace = nazev(cislo_hrace)

    # Volba počítače
    cislo_compu = random.randrange(5)
    nazev_compu = nazev(cislo_compu)


    # Vytiskne volbu, počítače a hráče
    print "\n"
    print "Hráč zvolil %s" %nazev_hrace
    print "Počítač zvolil %s" %nazev_compu

    # Vypsání výsledku
    print "\n"
    print "*" * 20

    # Určení vítěze
    if(cislo_compu + 1) % 5 == cislo_hrace:
        print "Vítězí hráč"
    elif(cislo_compu + 2) % 5 == cislo_hrace:
        print "Vítězí hráč"
    elif cislo_compu == cislo_hrace:
        print "Nerozhodně"
    else:
        print "Vítězí počítač"


    print "*" * 20

    print "\n1 = Ano\n2 = Ne"
    pokracovat = int(input('Chcete hrát dál ?\n'))

    if pokracovat == 1:
        pokracovat = True
    elif pokracovat == 2:
        print "\nProgram ukončen :)"
        pokracovat = False

