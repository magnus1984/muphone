#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def code(length=6, alphabet='0123456789'):
    """ Returns a randomly generated validation code

    Arguments:
        lenght int -- nbr of char in the code
        alphabet string -- char to pick from when generating the code

    Returns:
        string -- a random validation code
    """

    return "".join([ random.choice(alphabet) for _ in range(length) ])
