#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Krotki
#
# -----------------------------------------------------------------------------

from typing import List, Any, Tuple, Union


def tuple_from_numbers(a: int, b: int) -> Union[Tuple[()], Tuple[int, int]]:
    return (a,b) if a!=b else ()

def tuple_from_elements(lst: List[int]) -> Union[Tuple[int, ...], Tuple[None, ...]]:
    if len(lst) >=3 :
        return tuple(lst[:3])
    else:
        return 3*(None,)

def append_tuple_to_list(lst: List[Any], tpl: Tuple[Any, Any]) -> List[Any]:
    lst.extend(tpl) #metody jak .extend(), .append() itp zmieniaja obiekt ale zwracaja None
    return lst      #dlatego nie mozna bylo zrobic return lst.extend(tpl)