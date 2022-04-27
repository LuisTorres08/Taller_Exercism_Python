"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers to prepare.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers to prepare as an argument and
    returns how many minutes it will take to prepare that many layers based
    on the `PREPARATION_TIME`.
    """

    return number_of_layers * PREPARATION_TIME




def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param layers: int - number of layers prepared.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed time (in minutes) derived from 'PREPARATION_TIME' and 'layers'.

    Function that takes the number of layers prepared and the minutes the lasagna
    has been in the oven as arguments and returns how many minutes it has been
    in the oven based on the `PREPARATION_TIME` and the number of layers prepared.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


