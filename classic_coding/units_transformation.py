def hartree_to_MJmol(hartree):
    """
    transforms energy value from Hartree (a.u) to MJ mol^{-1} (SI)

    :param hartree: energy in hartree
    :return: energy in MJ mol^{-1}
    """

    one_hartree_J = 4.3597e-18
    avogadro = 6.0221e23
    MJ_to_J = 1e6
    hartree_MJ_mol = one_hartree_J * hartree * avogadro / MJ_to_J

    return hartree_MJ_mol
