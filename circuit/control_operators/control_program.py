from pyquil.quil import Program
from pyquil.quilbase import Gate
from pyquil.gates import CNOT, CCNOT, CPHASE
from Exceptions.errors import NotGateException
from circuit.control_operators.control_gates import *


def control_program(source_program, target_program, ancillary):
    """
    Creates a pyquil program that is controlled version of some other
    pyquil program

    :param source_program: we need controlled version from this pyquil Program
    :param target_program: in this program we will build the controlled version
    :param ancillary: the controlling qubit number
    :return: nothing, but change the target_program that will become controll
             version of the source_program
    """
    for gate in source_program:
        control_gate(target_program, gate, ancillary)


def control_gate(target_program, gate, ancillary):
    """
    Adds to the target_program controlled version of the gate

    :param target_program: pyquil Program
    :param gate: pyquil Gate
    :param ancillary: controlling qubit number

    :return: noting. Changes the target_program
    """

    # gate should be pyquil Gate
    if not isinstance(gate, Gate):
        raise NotGateException('Not a Gate!!')

    # target_program should be pyquil Program
    if not isinstance(target_program, Program):
        raise ValueError('Not a program!!')

    qubits = list(gate.get_qubits())
    params = gate.params

    if gate.name == "X":
        target_program.inst(CNOT(ancillary, qubits[0]))
        return

    if gate.name == "CNOT":
        target_program.inst(CCNOT(ancillary, qubits[0], qubits[1]))
        return

    if gate.name == "PHASE":
        target_program.inst(CPHASE(params[0], ancillary, qubits[0]))
        return

    if gate.name == "H":
        def_CH = create_CH()
        CH = def_CH.get_constructor()
        target_program.inst(CH(ancillary, qubits[0]))
        return

    if gate.name == "RX":
        def_CRX = create_CRX()
        CRX = def_CRX.get_constructor()
        target_program.inst(CRX(params[0])(ancillary, qubits[0]))
        return

    if gate.name == "RZ":
        def_CRZ = create_CRZ()
        CRZ = def_CRZ.get_constructor()
        target_program.inst(CRZ(params[0])(ancillary, qubits[0]))
        return

    raise ValueError("wrong Gate or don't have controlled version")
