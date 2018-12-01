from Exceptions.errors import RIGETTI_SERVER_ERROR
from circuit.pea import H2_energy_estimation
from common_tools.units_transformation import hartree_to_MJmol


def energy_in_infinity():
    """
    Finds the energy in infinity by putting the distance of H atoms in
    H2 molecule big enough

    :return: time that we used here, were time is t in exp(-iHt).
                and the energy that we will use as zero energy
    """

    precision = 7
    distance_infinity = 10  # in angstroms. An approximation for infinity distance
    trail = 7
    state = 0
    time = 4

    electron_energy = 0

    # try several times. Maybe the Rigetti server is not working.
    try_times = 5
    find_etalon = False
    for trying in range(0, try_times):
        energy_sample = H2_energy_estimation(4, precision, time, distance_infinity, state, trail, False)
        if energy_sample is not None:
            electron_energy = energy_sample
            find_etalon = True
            print("Zero Energy is found")
            break
    if not find_etalon:
        raise RIGETTI_SERVER_ERROR("Rigetti server is not working")

    total_energy = electron_energy + proton_proton(distance_infinity)

    return total_energy


def calc_total_energy(electron_energy, atomic_distance, energy0):
    """
    Calculates the total energy of H2 molecule from electron_energy by
    adding proton-proton Coulomb energy and defining the zero energy
    energy0. The formula:
                        E = E_el + E_p - E_0
    where e is the total energy, E_el is the electronic energy
    E_p = 1 / R, where R is atomic distance and E_0 is the chosen
    zero energy.

    :param electron_energy: list of energies of H2 molecule without
            proton-proton Coulomb energy
    :param atomic_distance: list of distances between two H atoms
            of H2 molecule
    :param energy0: The energy that we take as zero energy

    :return: list of total energy of H2 molecule in MJ mol^{-1}
    """

    total_energy = [0]*len(electron_energy)

    for dot in range(len(electron_energy)):
        # proton-proton Coulomb energy
        proton_energy = proton_proton(atomic_distance[dot])
        total_energy_hartree = electron_energy[dot] + proton_energy - energy0
        total_energy[dot] = hartree_to_MJmol(total_energy_hartree)

    return total_energy


def proton_proton(atomic_distance):
    """
    Calculates proton–proton Coulomb energy for atomic_distance separation
    of H atoms in H2 molecule

    :param atomic_distance: the distance between to H atoms in angstroms

    :return: proton–proton Coulomb energy
    """

    # should us atomic units
    bohr_rad = 0.53  # in angstroms
    distance_in_ai = atomic_distance / bohr_rad
    proton_proton = 1 / distance_in_ai

    return proton_proton

