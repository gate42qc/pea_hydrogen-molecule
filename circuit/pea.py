from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *
from math import pi

from circuit.pea_pyquil_program import pea_program
from common_tools.bit_manipulation import bitstring_to_value
from common_tools.majority_of_measurement import majority_and_index


def H2_energy_estimation(ancilary_start, ancilary_num, time, atomic_distance, state,
                         trails=5, pozitive_energy=True, trotter_order = 2):
    """
    takes phase obtained from phase_estimation method and  converts it to energy by
    using the equation:
                            E = 2pi * phase / t
    where t is the time, E is the energy.

    P.S Without proton-proton Coulomb energy

    :param ancilary_start: first ancillary qubit
    :param ancilary_num: how many ancillaries to use corresponds
            to precision in PEA algorithm
    :param time: t in exp(-iHt), where H is the Hamiltonian
    :param atomic_distance: the distance between to H atoms in H2 molecule
    :param state: ground state (0) or some excited state (1, 2, 3)
    :param trails: how many measurement to make in order to estimate the most
                    frequent result

    :return: the energy of corresponding state of H2 molecule
    """

    # calculating the phase
    phase = phase_estimation(ancilary_start, ancilary_num, time, atomic_distance, state, trails, trotter_order)
    if phase is None:
        return 0
    if phase > 1. or phase < 0.:
        raise ValueError("Phase should be in a range (0,1). The error phase is " + str(phase))

    # calculating resulting energy in atomic units (Hartree)
    if pozitive_energy:
        eneregy_phase = 2 * pi * phase / time
    else:
        eneregy_phase = 2 * pi * (phase - 1) / time
    energy = eneregy_phase
    return energy


def phase_estimation(ancillary_start, ancillary_num, time, atomic_distance, state, trails = 5, trotter_order = 2):
    """
    Measures the phase by using the phase estimation algorithm (PEA)

    :param ancillary_start: first ancillary qubit
    :param ancillary_num: how many ancillaries to use corresponds
            to precision in PEA algorithm
    :param time: t in exp(-iHt), where H is the Hamiltonian
    :param atomic_distance:  the distance between to H atoms in H2 molecule
    :param state: ground state (0) or some excited state (1, 2, 3)
    :param trails: how many measurement to make in order to estimate the most
                    frequent result

    :return: the phase from exp(-iHt) |psi> = exp(-i2pi phase) |psi> (Schrodinger)
    """

    # initialization of the state
    init_qubit = Program()
    if state == 0:
        init_qubit.inst(X(0)).inst(X(1))
    elif state == 1:
        init_qubit.inst(X(0)).inst(X(2))
    elif state == 2:
        init_qubit.inst(X(0)).inst(X(3))
    elif state == 3:
        init_qubit.inst(X(2)).inst(X(3))
    else:
        print("Wrong input of state. State should be 0, 1, 2, 3. Your input is " + str(state))
        raise ValueError
    prog = init_qubit + pea_program(ancillary_start, ancillary_num, time, atomic_distance, trotter_order)

    ro = prog.declare('ro', memory_type='BIT', memory_size=ancillary_num)
    # measurement of ancillary qubits
    for cindex, qindex in enumerate(range(ancillary_start, ancillary_start + ancillary_num)):
        prog += MEASURE(qindex, ro[cindex])

    qvm = QVMConnection()
    cregister = list(range(0, ancillary_num))
    m_reg = qvm.run(prog, cregister, trails)

    # taking most frequent result from the phase elements. The number of the elements are defined by the trails
    phase, major_index = majority_and_index([bitstring_to_value(bitst) for bitst in m_reg])
    print(str(phase) + "  =  " + str(m_reg[major_index]))

    return phase




