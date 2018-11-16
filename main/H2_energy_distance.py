import matplotlib.pyplot as plt
from main.complementary_code.energy import energy_in_infinity, calc_total_energy
from main.complementary_code.energy_for_plot import state_el_energy_distance
import pickle

trails = 7
t = 4
start_distance = 0.43
end_distance = 2.65
dots = 1
trotter_order = 2
state = [0, 1, 2, 3]

energy0 = energy_in_infinity()

el_energy_0, atomic_distance_pm0 = state_el_energy_distance(state[0], start_distance, end_distance, dots)
el_energy_1, atomic_distance_pm1 = state_el_energy_distance(state[1], start_distance, end_distance, dots)
el_energy_2, atomic_distance_pm2 = state_el_energy_distance(state[2], start_distance, end_distance, dots)
el_energy_3, atomic_distance_pm3 = state_el_energy_distance(state[3], start_distance, end_distance, dots)

# saving
with open("last_saved_data/el_energy_0.txt", 'w') as f:
    for s in el_energy_0:
        f.write(str(s) + '\n')
with open("last_saved_data/el_energy_1.txt", 'w') as f:
    for s in el_energy_1:
        f.write(str(s) + '\n')
with open("last_saved_data/el_energy_2.txt", 'w') as f:
    for s in el_energy_2:
        f.write(str(s) + '\n')
with open("last_saved_data/el_energy_3.txt", 'w') as f:
    for s in el_energy_3:
        f.write(str(s) + '\n')

plt.figure(0)
plt.plot(atomic_distance_pm0, el_energy_0, 'bs', atomic_distance_pm1, el_energy_1, 'gD',
         atomic_distance_pm2, el_energy_2, 'm^', atomic_distance_pm3, el_energy_3, 'rs')
plt.xlabel('Distance (pm)')
plt.ylabel('Energy of H2 in Hartee')
plt.title("Electronic energy")

plt.figure(1)
plt.plot(atomic_distance_pm0, el_energy_0, 'bs')
plt.xlabel('Distance (pm)')
plt.ylabel('Energy of H2 in Hartee')
plt.title("Electronic energy of ground state")

total_energy_0 = calc_total_energy(el_energy_0, atomic_distance_pm0, energy0)
total_energy_1 = calc_total_energy(el_energy_1, atomic_distance_pm1, energy0)
total_energy_2 = calc_total_energy(el_energy_2, atomic_distance_pm2, energy0)
total_energy_3 = calc_total_energy(el_energy_3, atomic_distance_pm3, energy0)

plt.figure(2)
plt.plot(atomic_distance_pm0, total_energy_0, 'bs', atomic_distance_pm1, total_energy_1, 'gD',
         atomic_distance_pm2, total_energy_2, 'm^', atomic_distance_pm3, total_energy_3, 'rs')
plt.xlabel('Distance (pm)')
plt.ylabel('Energy of H2 in MJ mol^{-1}')
plt.title("Total energy of ground state")

plt.figure(3)
plt.plot(atomic_distance_pm0, total_energy_0, 'bs')
plt.xlabel('Distance (pm)')
plt.ylabel('Energy of H2 in MJ mol^{-1}')
plt.title("Total energy of ground state")

plt.show()
