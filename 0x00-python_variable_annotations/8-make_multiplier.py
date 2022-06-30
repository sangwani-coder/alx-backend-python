#!/usr/bin/env python3
""" Defines a type annotated function make_multiplier"""
import typing


def mult(x: float) -> float:
    """ returns the square of the x float"""
    return x * x


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
        Write a type-annotated function make_multiplier that takes
        param: (multiplier: float)
            and
        returns: a function that multiplies a float by multiplier
    """

    return mult
