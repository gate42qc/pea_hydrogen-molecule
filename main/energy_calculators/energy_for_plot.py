from circuit.pea import H2_energy_estimation


def state_el_energy_distance(state, start_distance, end_distance, dots):
    if state == 1:
        middle_distance = 0.48
    elif state == 2:
        middle_distance = 0.56
    elif state == 3:
        middle_distance =1.02
    elif state != 0:
        raise ValueError("Wrong state. State should be 0, 1, 2, 3.")

    trails = 7
    t = 4
    trotter_order = 2

    if state == 0:
        return electron_energy_distance(state, t, trails, trotter_order, start_distance, end_distance, dots, False)
    else:
        if start_distance > middle_distance:
            return electron_energy_distance(state, t, trails, trotter_order, start_distance, end_distance, dots, False)
        elif end_distance < middle_distance:
            return electron_energy_distance(state, t, trails, trotter_order, start_distance, end_distance, dots, True)
        else:
            dots_pos = int(dots * (middle_distance - start_distance) / (end_distance - start_distance))
            dots_neg = dots - dots_pos
            neg_energy, neg_atomic_distance_pm = electron_energy_distance(state, t, trails, trotter_order, start_distance,
                                                                          middle_distance, dots_pos, True)
            pos_energy, pos_atomic_distance_pm = electron_energy_distance(state, t, trails, trotter_order, middle_distance,
                                                                          end_distance, dots_neg, False)

            return (neg_energy + pos_energy), (neg_atomic_distance_pm + pos_atomic_distance_pm)


def electron_energy_distance(state, time, trails, trotter_order, start_distance, end_distance, dots, pozitive_energy):
    precision = 6

    # list of distances of H atoms in H2 molecule
    atomic_distance = [0] * dots
    atomic_distance_pm = [0] * dots
    if dots == 1:
        distance_step = 0
    else:
        distance_step = (end_distance - start_distance) / (dots - 1)

    for dot_index in range(0, dots):
        atomic_distance[dot_index] = start_distance + dot_index * distance_step
        angs_to_pm = 100
        atomic_distance_pm[dot_index] = angs_to_pm * atomic_distance[dot_index]
    electron_energy = [0] * dots

    for dot_index in range(0, dots):
        print("distance = " + str("%.2f" % atomic_distance[dot_index]) + "pm" +
              ". Done = " + str("%.2f" % (100 * dot_index / len(atomic_distance))) + "%")

        electron_energy[dot_index] = H2_energy_estimation(4, precision, time, atomic_distance[dot_index],
                                                          state, trails, pozitive_energy, trotter_order)

    return electron_energy, atomic_distance_pm
