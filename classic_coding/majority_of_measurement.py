
def majority_and_index(results):
    """
    majority indicates the most frequent list member and returns it
    :param results: is list of outputs of quantum measurement
    :return: the one measurement that is most frequent in the results
    """

    max_value = 0
    max_times = 0
    value_dict = {}
    major_index = -1

    for index, res in enumerate(results):
        value_dict[res] = (value_dict.get(res, 0) + 1)

        if max_times < value_dict[res]:
            max_times = value_dict[res]
            max_value = res
            major_index = index

    return max_value, major_index
