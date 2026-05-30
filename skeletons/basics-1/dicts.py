#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Słowniki
#
# -----------------------------------------------------------------------------

from typing import Dict, Any, List, Tuple, Optional, Set


def dict_intro() -> None:
    dict = {"Adam": 2 , "Bogdan": 4, "Cezary": 1}

    for k, v in dict.items():
        print(k, "=", v)


# Alias `Menu` na typ `Dict[str, float]` poprawia czytelność kodu
# oraz upraszcza wprowadzanie ewentualnych zmian w programie.
Menu = Dict[str, float]


def update_price(menu: Menu, dish: str) -> None:
    menu[dish] += 50


def fix_key(dct: Dict[str, Any], incorrect_key: str, correct_key: str) -> Dict[str, Any]:

    #tym mozna kopiowac slownik
    rep = dict(dct)
    if incorrect_key in rep:
        rep[correct_key] = rep[incorrect_key]
        del rep[incorrect_key]
    return rep



def update_all_prices(menu: Menu) -> None:
    for dish in menu:
        menu[dish] += 50

# TODO: Zdefiniuj alias `ClassRegister` na typ umożliwiający przechowywanie
#   informacji o ocenach poszczególnych uczniów, tj. mapowanie nazwy
#   ucznia na listę ocen (będących liczbami zmiennoprzecinkowymi).
ClassRegister = Dict[str,List[float]]


def average_grades_1(register: ClassRegister) -> Dict[str, float]:
    av_dict = dict(register)
    for student, grades in register.items() :
        av_dict[student]=sum(grades)/len(grades)
    return av_dict
    


def average_grades_2(register: ClassRegister) -> Dict[str, Optional[float]]:
    av_dict = {} 
    for student, grades in register.items() :
        if grades :
            av_dict[student]=sum(grades)/len(grades)
        else: 
            av_dict[student]= None
    return av_dict
    


def letters_frequencies(s: str) -> Dict[str, int]:
    litery = list(s)
    freq = {}
    for i in litery:   #nawet wystarczy char in s w pythonei
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    return freq

def letters_frequency_2(s: str) -> Tuple[Dict[str, int], int]:
    return (letters_frequencies(s), len(letters_frequencies(s).keys()))


def census(register: Dict[str, Dict[str, Any]]) -> Tuple[Dict[str, int], float]:
    freq = {}
    for _, dane in register.items(): # '_' uzywa sie do oznaczenia param ktorego nie uzywam
        country = dane['address']['country']
        if country not in freq:
            freq[country] = 0
        freq[country]+= 1
        av_age = sum(register[d]['age'] for d in register)/len(register) 
        #jak chcialem dac len(dane) to sie nie zgadzalo bo 
    return freq, av_age


# lista zakupowa - mapowanie nazwy produktu na liczbę sztuk (do kupienia)
ShoppingList = Dict[str, int]


def sum_shopping_lists(list1: ShoppingList, list2: ShoppingList) -> ShoppingList:
    lista_c = dict(list1)
    for i in list2 : 
        if i not in list1 : 
            lista_c[i] = 0
        lista_c[i] += list2[i]
    return lista_c


def sum_shopping_lists_nonempty(list1: ShoppingList, list2: ShoppingList) -> ShoppingList:
    lista_c = sum_shopping_lists(list1, list2)
    for product in lista_c :
        if lista_c[product] == 0:
            del lista_c[product]
    return lista_c

def filter_pesels_by_name_initial(persons: Dict[str, str], name_initial: str) -> Set[str]:
    return {pesel for pesel, name in persons.items() if name[0]==name_initial}

print("__file__", __file__)