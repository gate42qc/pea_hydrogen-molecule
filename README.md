# Demonstration of Phase Estimation Algorithm for Hydrogen Molecule



## Synopsis

Calculating the energy spectra for hydrogen molecule's ground and first 3 excited states by using simulator of quantum computer (pyQuil). Here we are using quantum phase estimation algorithm (PEA), that allows one to calculate phase of the eignstate of the desired unitary operator. For measuring the energy of a molecule one should use PEA for unitary operator U = exp(iHt), where H is the Hamiltonian of the molecule, t is the time parameter. Eigenvalue of corresponding |state>  of this molecule is equal to exp(iEt), where E is the energy of the molecule. We can rewrite it in the following way exp(iEt) = exp(i2π phase), where phase = Et/2π. Actually the PHE measures the phase, after which we can obtain the energy of desired |state>.

## Installation

The following tools are needed to install and run the app:

* pyQuil 1.9 (https://github.com/rigetticomputing/pyQuil). Not working with pyQuil 2.0
* OpenFermion
* pyscf
* forestopenfermion
* openfermionpyscf

or run the following comand in your terminal:

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

