from vpython import *
#GlowScript 3.0 VPython
## PHYS 2212 Online
## Magnetic Field of a Bar Magnet
## Last updated: 2021-01-11 EAM


## ===================
## PHYSICAL CONSTANTS
## ===================

u0over4pi = 1e-7



## ==================================
## CREATING THE MAGNET AT THE ORIGIN
## ==================================

magnet = cylinder(pos = vector(0,0.0,0), axis = vector(0.025,0,0), radius = 0.0065)
muhat = magnet.axis / (mag(magnet.axis))

# Magnitude of the magnetic moment -- EDIT THE NEXT ONE LINE TO MATCH YOUR MEASUREMENTS
mumag = 3.788417821
magnet.mu = mumag*muhat



## =================================================
## EDIT TO CREATE A FUNCTION FOR THE MAGNETIC FIELD
## =================================================

def dipoleB(mu, r):
    rmag = mag(r)
    rhat = norm(r)
    B = u0over4pi * 1/(rmag ** 3) * (3 * dot(mu, rhat) * rhat - mu)
    return(B)



## ======================================
## VISUALIZING THE MAGNETIC FIELD:
## ON AXIS AND PERPENDICULAR TO THE AXIS
## ======================================

# Scaling the arrows so they fit on the screen -- EDIT THIS ONE LINE
B_scale = 1e2


# This value determines how far away from the origin (in meters) the arrows will be placed
# EDIT THIS LINE TO SEE THE FIELD AT DIFFERENT DISTANCES
distance = 0.1


# Observation locations: two on-axis, four perpendicular to the axis
# EDIT THE LINES THAT NEED EDITING (those that are set to zero vectors)
obs_axis1 = vector(distance, 0, 0)
obs_axis2 = vector(-distance, 0, 0)
obs_perp1 = vector(0, distance, 0)
obs_perp2 = vector(0, -distance, 0)
obs_perp3 = vector(0, 0, distance)
obs_perp4 = vector(0, 0, -distance)


# Draw TWO arrows to represent the magnetic field on-axis
# EDIT THE NEXT THREE LINES TO MAKE THE FIRST ARROW
# THEN ADD MORE LINES TO CREATE THE OTHER ARROW
r_axis1 = obs_axis1 - magnet.pos
B_axis1 = dipoleB(magnet.mu, r_axis1)
arrow(pos = obs_axis1, color = color.orange, axis = B_axis1 * B_scale)
print("B_axis1 = ", B_axis1)

r_axis2 = obs_axis2 - magnet.pos
B_axis2 = dipoleB(magnet.mu, r_axis2)
arrow(pos = obs_axis2, color = color.orange, axis = B_axis2 * B_scale)
print("B_axis2 = ", B_axis2)


# Draw FOUR arrows to represent the magnetic field perpendicular to the axis
# EDIT THE NEXT THREE LINES TO MAKE THE FIRST ARROW
# THEN ADD MORE LINES TO CREATE THE OTHER THREE ARROWS
r_perp1 = obs_perp1 - magnet.pos
B_perp1 = dipoleB(magnet.mu, r_perp1)
arrow(pos = obs_perp1, color = color.cyan, axis = B_perp1 * B_scale)
print("B_perp1 = ", B_perp1)

r_perp2 = obs_perp2 - magnet.pos
B_perp2 = dipoleB(magnet.mu, r_perp2)
arrow(pos = obs_perp2, color = color.cyan, axis = B_perp2 * B_scale)
print("B_perp2 = ", B_perp2)

r_perp3 = obs_perp3 - magnet.pos
B_perp3 = dipoleB(magnet.mu, r_perp3)
arrow(pos = obs_perp3, color = color.cyan, axis = B_perp3 * B_scale)
print("B_perp3 = ", B_perp3)

r_perp4 = obs_perp4 - magnet.pos
B_perp4 = dipoleB(magnet.mu, r_perp4)
arrow(pos = obs_perp4, color = color.cyan, axis = B_perp4 * B_scale)
print("B_perp4 = ", B_perp4)



## ================================
## VISUALIZING THE MAGNETIC FIELD:
## 45 DEGREES OFF-AXIS
## ================================

# Average d_perp from your experiment
# EDIT THE NEXT ONE LINE TO MATCH YOUR MEASUREMENTS
d_perp = 0.1893333
d = d_perp*sqrt(2)
print("d = ", d)

# Observation location at 45 degrees from the axis
# You can change this observation location to create arrows at other 45-degree locations
obs_45deg = vector(d_perp,d_perp,0)

# Draw an arrow to represent the magnetic field 45 degrees from the axis
# EDIT THE NEXT THREE LINES
r_45deg = obs_45deg
B_45deg = dipoleB(magnet.mu, r_45deg)
arrow(pos = obs_45deg, color = color.magenta, axis = B_45deg * B_scale * 1e1)
print("B at 45deg at distance d = ", B_45deg)

print("All done!")