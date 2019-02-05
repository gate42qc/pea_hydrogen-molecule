# Demonstration of Phase Estimation Algorithm for Hydrogen Molecule



## Synopsis

Calculating the energy spectra for hydrogen molecule's ground and first 3 excited states by using simulator of quantum computer (pyQuil). Here we are using quantum phase estimation algorithm (PEA), that allows one to calculate phase of the eignstate of the desired unitary operator. For measuring the energy of a molecule one should use PEA for unitary operator U = exp(iHt), where H is the Hamiltonian of the molecule, t is the time parameter. Eigenvalue of corresponding |state>  of this molecule is equal to exp(iEt), where E is the energy of the molecule. We can rewrite it in the following way exp(iEt) = exp(i2π phase), where phase = Et/2π. Actually the PHE measures the phase, after which we can obtain the energy of desired |state>.

The result of the circuit is shown in the following figure, where we have obtained spectra for the first four energy levels of hydrogen molecule (dependence of energy on interatomic distance of two hydrogen atoms):

![pea plot](https://github.com/gate42qc/pea_hydrogen-molecule/blob/master/fourLevels.jpg)

## Installation

The following tools are needed to install and run the app:

* pyQuil 1.9 (https://github.com/rigetticomputing/pyQuil).
* OpenFermion
* pyscf
* forestopenfermion
* openfermionpyscf

or run the following command in your terminal:

`install -r requirements.txt`

## Author & Contributor List

---------
Davit Khachatryan

Hakob Avetisyan

Arshak Hovhannisyan

Misha Aghamalyan

------

## License

This project is licensed under the terms of the MIT license. See the "LICENSE" file.

