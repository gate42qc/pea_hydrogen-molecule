from openfermion.hamiltonians import MolecularData
from openfermionpyscf import run_pyscf
from openfermion.transforms import get_fermion_operator, jordan_wigner
from forestopenfermion import qubitop_to_pyquilpauli
from pyquil.quil import Program
from pyquil.paulis import exponentiate

from program_operations.operation import repeat_program


def exp_hamiltoniantrot_H2(time, atomic_distance, trotter_order):
    """
    Here we are using some packages related to quantum chemistry to obtain
    hamiltonian of H2 molecule. The we are translating this hamiltonian into
    sequence of pyquil gates. And finally, we are trotterazing the exponent
    of the hamiltonian (exp(-iHt)) of our system and returning the obtained
    pyquil program

    :param time: is t in the exp(iHt). Note the + sign.
    :param atomic_distance: the distance between to H atoms in H2 molecule

    :return: program of the Trotter-Suzuki decomposition of
             hamiltonian exp(iHt) for H2 molecule
    """

    geometry = [['H', [0, 0, 0]],
                ['H', [0, 0, atomic_distance]]]  # H--H distance = 0.74angstrom
    basis = 'sto-3g'
    multiplicity = 1  # (2S+1)
    charge = 0
    h2_molecule = MolecularData(geometry, basis, multiplicity, charge)
    h2_molecule = run_pyscf(h2_molecule)

    h2_qubit_hamiltonian = jordan_wigner(get_fermion_operator(h2_molecule.get_molecular_hamiltonian()))
    pyquil_h2_qubit_hamiltonian = qubitop_to_pyquilpauli(h2_qubit_hamiltonian)

    return trotterization(pyquil_h2_qubit_hamiltonian, float(time), trotter_order)


def trotterization(hamiltonian, time, trotter_order):
    """
    Uses first order Trotter-Suzuki decomposition:
        exp(iHt) = (exp(ih_1 t)exp(ih_2 t)exp(ih_n t))^N + O(t*delta_t),
    where H = h_1 * h_2 * ... * h_n, delta_t is t/N

    :param hamiltonian: is the Hamiltonian (H in the formula)
    :param time: is t in the formula
    :param trotter_order: is N in the formula.

    :return: Trotterized exponentiated Hamiltonian
    """

    delta_time = time / trotter_order

    trotter_order1_program = Program()
    for term in hamiltonian.terms:
        # Note that exponentiate(term) returns exp(-1j * term)
        trotter_order1_program += exponentiate(-delta_time * term)

    return repeat_program(trotter_order1_program, int(trotter_order))




