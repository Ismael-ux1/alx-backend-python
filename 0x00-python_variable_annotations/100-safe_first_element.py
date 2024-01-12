#!/usr/bin/env python3

""" 
This function returns the value of a key in a dictionary if it exists,
otherwise it returns a default value. 
"""

from typing import TypeVar, Dict, Optional


# Define TypeVars for key and value types
KT = TypeVar('KT')
VT = TypeVar('VT')

def safely_get_value(dct: Dict[KT, VT], key: KT, default: Optional[VT] = None) -> Optional[VT]:
    """
    This function returns the value of a key in a dictionary if it exists,
    otherwise it returns a default value.

    Parameters:
    dct (Dict[KT, VT]): The dictionary to search.
    key (KT): The key to look for in the dictionary.
    default (Optional[VT]): The default value to return if the key is not found.

    Returns:
    Optional[VT]: The value of the key in the dictionary or the default value.
    """
    # Check if the key is in the dictionary
    if key in dct:
        # If the key is found, return its value
        return dct[key]
    else:
        # If the key is not found, return the default value
        return default
