def bitstring_to_value(bit_list):
    """
    After measuring our ancillary qubit in the phase estimation
    algorithm we obtain some bitstring (bit_list) and we need to
    convert it to decimal number that will be the phase that we
    looking for in phase estimation algorithm

    :param bit_list: list of bit values obtained from quantum measurement

    :return: the corresponding phase of the bit_list
    """

    phase = 0.
    bit_length = len(bit_list)
    for i, cindex in enumerate(bit_list):
        phase += float(cindex)/(2**(bit_length - i))

    return phase
