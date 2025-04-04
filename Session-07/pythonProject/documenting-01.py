"""Documenting Code Example 1"""
import random


# Author:   Javad Tehrani
# Date:     2025-03-28

def higher_or_lower(guss_number, target_number):
    """
    Deretmines if the guss is higher or lower than the traget number.
    
    Parameters
    ------------
    guss_number: an integer number
    target_number: an integer number
    
    Returns
    __________
    :return: string
    A string with "H" for higher , "L" for Lower
    
    Example 
    -------
    
    >>> higher_or_lower(0,1)
    'L'
    >>> higher_or_lower(1,0)
    'H'
    >>> higher_or_lower(0,0)
    'E'
    >>> higher_or_lower(-1,1)
    'L'
    """
    if guss_number < target_number:
        return "L"
    if guss_number > target_number:
        return "H"
    return "E"

import doctest
doctest.testmod()

#target = random.randint(0,100)
#guess =


