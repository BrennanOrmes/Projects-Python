#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CNYS
#
# Created:     27/08/2014
# Copyright:   (c) CNYS 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def check_length(sequence):
    """ (str) -> bool

    Return whether the length of the resistor sequence is valid.

    >>> check_length('NKOD')
    True
    >>> check_length('NKO')
    False
    """
    if len(sequence) == 4:
        return True
    else:
        return False


def check_colours(sequence):
    """ (str) -> bool

    Return True if and only if the sequence contains the letters G K L N O R V W Y Z.

    >>> check_colours('NKOD')
    True
    >>> check_colours('NKOF')
    False
    """
    valid = True
    valid_letters = ("DGKLNORSUVWYZ")
    for i in sequence:
        if i in valid_letters:
            print i
        else:
            valid = False
    return valid


def get_numbers(sequence):
    """ (str) -> str

    Return the numbers part of the sequence as a string.

    >>> get_numbers('NKOD')
    NK
    >>>get_numbers ('RRKS')
    RR
    """
    number_string = sequence[0] + sequence[1]
    return number_string


def is_valid_multiplier (sequence):
    """ (str) -> bool

    Return True if and only if the multiplier has the value D G K L N O R S V or Y

    >>> is_valid_multiplier('RRRS')
    True
    >>> is_valid_multiplier('RRZG')
    False

    """
    check_digit = sequence[2]
    valid_letters = "DGKLNORSVY"
    if check_digit in valid_letters:
        return True
    else:
        return False

def is_valid_tolerance (sequence):
    """ Return True if and only if the tolerance (last character)
    consists of a D, G, L, N, R, S, V, Z.
    (note that this list is slightly different from the earlier ones).

    >>> is_valid_tolerance('RRZG')
    True
    >>> is_valid_tolerance('RRZO')
    False
    """
    check_digit = sequence[3]
    valid_letters = "DGKLNRSVZ"
    if check_digit in valid_letters:
        return True
    else:
        return False

def calculate_raw_value (sequence):
    """The first parameter is the two character value string.
     Convert the two characters to a numeric value and return it.

    >>> calculate_raw_value ('NKOD')
    10
    >>> calculate_raw_value ('RYZG')
    24
    """
    numbers = get_numbers(sequence)
    letterlist = "KNROYGLVZW"
    valueslist = [0,1,2,3,4,5,6,7,8,9]
    count = 0

    for i in letterlist:
        if i == sequence[0]:
            position1 = count
        count += 1

    count = 0

    for i in letterlist:
        if i == sequence[1]:
            position2 = count
        count += 1

    position1 = position1 * 10
    value = position1 + position2

    return value

def calculate_multiplied_value (rawvalue, multiplier):
    """The parameters are the raw number just calculated, plus the multiplier.
     Multiply the raw value by the multiplier return the whole value.
     >>> calculate_multiplied_value (20, 'Y')
     200,000
     >>> calculate_multiplied_value (45, 'R')
     4500"""

    letterlist = "DGKLNORSVY"
    values_list = [0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 10000000, 100000000]

    count = 0
    for i in letterlist:
        if i == multiplier:
            position = count
        count += 1

    value_to_multiply = values_list[position]
    print value_to_multiply
    final =  rawvalue * value_to_multiply
    return final




def main():
    sequence = raw_input ("Enter your resistor colour sequence here, use UPPERCASE only  >>")
    valid_length = check_length(sequence)
    if valid_length:
        print ("The length is good!")
    else:
        print ("Your sequence is invalid!")

    valid_colours = check_colours(sequence)
    if valid_colours:
        print ("The sequence is valid")
    else:
        print ("The sequence contains invalid characters.")

    print get_numbers(sequence)

    if is_valid_multiplier (sequence):
        multiplier = sequence[2]

    print is_valid_tolerance (sequence)

    raw_value = calculate_raw_value (sequence)
    print raw_value
    multiplied_value = calculate_multiplied_value(raw_value, multiplier)
    print multiplied_value



if __name__ == '__main__':
    main()
