from vpython import *
#Web VPython 3.2

def Efield(chargedParticle, observationLocation):
    q = chargedParticle.charge
    r = observationLocation - chargedParticle.pos
    E = 9e9 * chargedParticle.charge * norm(r) / (r.x**2 + r.y**2 + r.z**2)
    return E
    
# Position's units are cm and mass's units are g
tape1 = sphere(pos = vec(0, 0, 0), radius = 0.05, color = color.cyan, mass = 0.2)
tape2 = sphere(pos = vec(0, -0.5, 0), radius = 0.05, color = color.magenta, mass = 0.2)

grav = tape1.mass / 1000 * 9.81
grav_arrow = arrow(pos = tape1.pos, axis = vec(0, grav * -1e2, 0), color = color.blue)
print('Magnitude of gravitational force on tape1 is', grav)

charge = sqrt(grav * ((tape2.pos.y / 100) ** 2) / 9e9)
print('Charge on each tape is', charge)

tape1.charge = charge
tape2.charge = charge

f1 = tape2.charge * Efield(tape1, tape2.pos)
fa1 = arrow(pos = tape2.pos, axis = 1e6 * f1, color = color.cyan)

f2 = tape1.charge * Efield(tape2, tape1.pos)
fa2 = arrow(pos = tape1.pos, axis = 1e6 * f2, color = color.magenta)

num_electron = abs(charge / (-1.6E-19))
print('Number of deficit electrons on each tape is', num_electron)

area = 0.2 * 0.018
num_atom = area / (3.1416926 * ((1e-10) ** 2 ))
ratio = num_electron / num_atom
print('Ratio of deficit electrons to number of atoms is', ratio)