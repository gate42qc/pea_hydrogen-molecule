import matplotlib.pyplot as plot

from main.energy_calculators.energy import energy_in_infinity, calc_total_energy
from main.energy_calculators.energy_for_plot import state_el_energy_distance

START_DISTANCE = 0.43
END_DISTANCE = 2.65
DOTS_AMOUNT = 50
ENERGY_STATES = [0, 1, 2, 3]

ENERGY_ZERO = energy_in_infinity()

electronic_energy_0, atomic_distance_pm0 = state_el_energy_distance(
    ENERGY_STATES[0], START_DISTANCE, END_DISTANCE, DOTS_AMOUNT)
with open("last_saved_data/electronic_energy_0.txt", 'w') as f:
    for s in electronic_energy_0:
        f.write(str(s) + '\n')

electronic_energy_1, atomic_distance_pm1 = state_el_energy_distance(
    ENERGY_STATES[1], START_DISTANCE, END_DISTANCE, DOTS_AMOUNT)
with open("last_saved_data/electronic_energy_1.txt", 'w') as f:
    for s in electronic_energy_1:
        f.write(str(s) + '\n')

electronic_energy_2, atomic_distance_pm2 = state_el_energy_distance(
    ENERGY_STATES[2], START_DISTANCE, END_DISTANCE, DOTS_AMOUNT)
with open("last_saved_data/electronic_energy_2.txt", 'w') as f:
    for s in electronic_energy_2:
        f.write(str(s) + '\n')

electronic_energy_3, atomic_distance_pm3 = state_el_energy_distance(
    ENERGY_STATES[3], START_DISTANCE, END_DISTANCE, DOTS_AMOUNT)
with open("last_saved_data/electronic_energy_3.txt", 'w') as f:
    for s in electronic_energy_3:
        f.write(str(s) + '\n')

plot.figure(0)
plot.plot(atomic_distance_pm0, electronic_energy_0, 'bs', atomic_distance_pm1, electronic_energy_1, 'gD',
          atomic_distance_pm2, electronic_energy_2, 'm^', atomic_distance_pm3, electronic_energy_3, 'rs')
plot.xlabel('Distance (pm)')
plot.ylabel('Energy of H2 in Hartee')
plot.title("Electronic energy")

plot.figure(1)
plot.plot(atomic_distance_pm0, electronic_energy_0, 'bs')
plot.xlabel('Distance (pm)')
plot.ylabel('Energy of H2 in Hartee')
plot.title("Electronic energy of ground state")

total_energy_0 = calc_total_energy(electronic_energy_0, atomic_distance_pm0, ENERGY_ZERO)
total_energy_1 = calc_total_energy(electronic_energy_1, atomic_distance_pm1, ENERGY_ZERO)
total_energy_2 = calc_total_energy(electronic_energy_2, atomic_distance_pm2, ENERGY_ZERO)
total_energy_3 = calc_total_energy(electronic_energy_3, atomic_distance_pm3, ENERGY_ZERO)

plot.figure(2)
plot.plot(atomic_distance_pm0, total_energy_0, 'bs', atomic_distance_pm1, total_energy_1, 'gD',
          atomic_distance_pm2, total_energy_2, 'm^', atomic_distance_pm3, total_energy_3, 'rs')
plot.xlabel('Distance (pm)')
plot.ylabel('Energy of H2 in MJ mol^{-1}')
plot.title("Total energy of ground state")

plot.figure(3)
plot.plot(atomic_distance_pm0, total_energy_0, 'bs')
plot.xlabel('Distance (pm)')
plot.ylabel('Energy of H2 in MJ mol^{-1}')
plot.title("Total energy of ground state")

plot.show()
