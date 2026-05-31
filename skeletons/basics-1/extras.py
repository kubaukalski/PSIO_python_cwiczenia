#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Zagadnienia dodatkowe
#
# -----------------------------------------------------------------------------

from typing import List, Set, Dict, Tuple, Optional, Callable


def get_unique_letters(s: str) -> Set[str]:
    z = set()
    if len(s)>=3:
        for i in s:
            if i not in z:
                z.add(i)
    return z
    #set(list(s)) robi to z automatu

# lista zakupowa - mapowanie nazwy produktu na liczbę sztuk (do kupienia)
ShoppingList = Dict[str, int]


def products_to_buy(list1: ShoppingList, list2: ShoppingList) -> Set[str]:
    #set(dict) zwroci tylko klucze, mozna tez dla bezpieczenstwa set(dict.keys())
    return set(list1) | set(list2)


def products_only_on_one_list(list1: ShoppingList, list2: ShoppingList) -> int:
    return len(set(list1.keys()) ^ set(list2.keys()))

def two_dice_rolls_combinations() -> Dict[int, Set[Tuple[int, int]]]:
    wynik: Dict[int, Set[Tuple[int, int]]] = {suma: set() for suma in range(2, 13)}
    for d1 in range(1,7):
        for d2 in range(1,7) :
            suma = d1 +d2
            wynik[suma].add((d1,d2))
    return wynik

def append_and_sort(lst: List[str]) -> List[str]:
    ret = lst[:]
    ret.append('abc')
    ret.sort()
    return ret

def ints_to_str(lst: List[int]) -> str:
    s = ""
    stringowana = [str(i) for i in lst]
    return s.join(x for x in stringowana)

def ints_to_str_max_length(lst: List[int], max_length: Optional[int] = None) -> str:
    return ints_to_str(lst[:max_length])

def division_guardian(x: float, y: float) -> bool:
    return y!=0 and x/y>1

def f_compose(f: Callable[[float], float], x0: float) -> float:
    return f(f(x0))