from vpython import *
#Web VPython 3.2

# Constants
oofpez = 9e9
qproton = 1.6e-19
scalefactor = 1e-20
distance = 3e-10

# Objects
particle = sphere(pos = vec(1e-10, 0, 0), radius = 2e-11, color = color.blue)
particle.charge = qproton

# Initial Values
obslocation = vec(3.1e-10, -2.1e-10, 0)

# Calculations
r = obslocation - particle.pos
print('The relative position vector is r=', r)

ra = arrow(pos = particle.pos, axis = r, color = color.green)

rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
print('The magnitude of r is |r|=', rmag)

rhat = norm(r)
print('The unit vector is rhat=', rhat)

E = oofpez * particle.charge * rhat / (rmag**2)
print('The electric field vector is E=', E)

ea = arrow(pos = obslocation, axis = scalefactor * E, color = color.orange)

obslocation1 = particle.pos + vec(distance, 0, 0)
E1 = Efield(particle, obslocation1)
ea1 = arrow(pos = obslocation1, axis = scalefactor * E1, color = color.orange)

obslocation2 = particle.pos + vec(-distance, 0, 0)
E2 = Efield(particle, obslocation2)
ea2 = arrow(pos = obslocation2, axis = scalefactor * E2, color = color.orange)

obslocation3 = particle.pos + vec(0, distance, 0)
E3 = Efield(particle, obslocation3)
ea3 = arrow(pos = obslocation3, axis = scalefactor * E3, color = color.orange)

obslocation4 = particle.pos + vec(0, -distance, 0)
E4 = Efield(particle, obslocation4)
ea4 = arrow(pos = obslocation4, axis = scalefactor * E4, color = color.orange)

obslocation5 = particle.pos + vec(0, 0, distance)
E5 = Efield(particle, obslocation5)
ea5 = arrow(pos = obslocation5, axis = scalefactor * E5, color = color.orange)

obslocation6 = particle.pos + vec(0, 0, -distance)
E6 = Efield(particle, obslocation6)
ea6 = arrow(pos = obslocation6, axis = scalefactor * E6, color = color.orange)

# Function
def Efield(chargedParticle, observationLocation):
    q = chargedParticle.charge
    r = observationLocation - chargedParticle.pos
    E = oofpez * chargedParticle.charge * norm(r) / (r.x**2 + r.y**2 + r.z**2)
    return E