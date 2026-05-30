#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Listy
#
# -----------------------------------------------------------------------------

from typing import List, Any, Optional


def is_element_on_list(lst: List[Any], e: Any) -> bool:
    for elem in lst:
        if elem == e :
            return True 
    return False
            
def element_xor(lst: List[Any], e1: Any, e2: Any) -> bool:
    if (e1 in lst) and (e2 not in lst):
        return True
    else:
        return False 


def print_every_second_elem(lst: List[str]) -> None:
    for i in range(0,len(lst)) :
        if i%2 == 0:
            print(i,'->',lst[i], '\n')

    

def arg_condition(arg: Optional[List[Any]]) -> bool:
    #nie trzeba nawet pisac True if arg (...)
    #przez short_ciruiting nam sie nie wywala len(None) bo wtedy juz nie sprawdza python
    #dlatego kolejnosc warunkow jest tutaj wazna
    return arg is None or len(arg) >2


def list_condition_1(lst: List[int]) -> bool:
    return len(lst) >= 2 and lst[1] == 5 
   
def list_condition_2(lst: List[int]) -> bool:
    return len(lst) >= 2 and len(lst) <= 4 and lst[-2] == 3


def remove_first_three_elements(lst: List[Any]) -> None:
    # [:4] bierze wycinek 4 pierwszych elementow listy
    del lst[:3]


def replace_last_two_elements(lst: List[int]) -> List[int]:
    lst_cp = lst[:]
    if len(lst_cp) >= 2 :
        lst_cp[-2:]=[9]
    return lst_cp


def merge_ends(lst: Optional[List[Any]] = None) -> List[Any]:
    if lst == [] or lst == None :
        return []
    elif 1<= len(lst) <= 3 :
        ret = lst[:1]
        ret.append(ret[0])
    elif 4 <= len(lst) :
        ret = lst[:4]
        ret[-2:]=lst[-2:]
    return ret

    #if not lst:  None lub []
    #    return []
    #elif len(lst) < 4:
    #    return 2 * [lst[0]] #arytmetyka dzialania na listach!!
    #else:
    #    return lst[:2] + lst[-2:] #tak mozna tez dodawac

def remove_element_if_exists(lst: List[Any], e: Any) -> List[Any]:
    ret = lst[:]
    if e in ret: 
        ret.remove(e)
    return ret

def is_palindrome(s: str) -> bool:
    return s == s[::-1] #-1 czyta od tyłu
    #slicing w pytonie: string[start:stop:step], jak jest s[ : : step] to bierze cały napis od rauz