from grove.qft.fourier import inverse_qft
from pyquil.quil import Program
from pyquil.gates import H

from circuit.control_operators.control_gates import *
from circuit.control_operators.control_program import control_program
from common_tools.operation import repeat_program
from quantum_chemistry.hydrogen_molecule import exp_hamiltoniantrot_H2


def pea_program(ancillary_start, ancillary_num, time, H2_distance, trotter_order):
    """
    Creates a pyquil Program for the phase estimation algorithm (PEA)

    :param ancillary_start: index of the first ancillary qubit.
    :param ancillary_num: how many ancillaries to use corresponds
            to precision in PEA algorithm
    :param time: t in exp(-iHt), where H is the Hamiltonian
    :param H2_distance: the distance between to H atoms in H2 molecule

    :return: a pyquil Program for PEA algorithm
    """

    phase_estimation_program = Program()
    unitary = exp_hamiltoniantrot_H2(time, H2_distance, trotter_order)
    phase_estimation_program.inst(create_CRX(), create_CRZ(), create_CH())

    Hadamard_ancilaries = Program()

    for index in range(0, ancillary_num):
        Hadamard_ancilaries.inst(H(ancillary_start + index))

    phase_estimation_program += Hadamard_ancilaries

    for index in range(0, ancillary_num):
        cont_first_order = Program()
        control_program(unitary, cont_first_order, ancillary_start + index)
        control_unitary = repeat_program(cont_first_order, 2**index)
        phase_estimation_program += control_unitary

    ancilary_list = list(range(ancillary_start, ancillary_start + ancillary_num))

    inv_qft_prog = inverse_qft(ancilary_list)

    phase_estimation_program += inv_qft_prog

    return phase_estimation_program
