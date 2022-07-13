from vpython import *
#GlowScript 3.0 VPython
## PHYS 2212 Online
## Lines of Charge
## Last updated: 2021-01-11 EAM


## ===================
## PHYSICAL CONSTANTS
## ===================

oofpez = 9e9 
g = 9.81 



## =================================
## EDIT TO ADD YOUR OBSERVED VALUES
## =================================

# Mass of one tape (in kg) -- EDIT THIS NEXT LINE
M = 0.2 / 1000

# Estimated net charge on one tape (in C) -- EDIT THIS NEXT LINE
Q = 1.0176e-7



## =================================================
## EDIT TO CREATE A FUNCTION FOR THE ELECTRIC FIELD
## (you can copy your work from Lab 0)
## =================================================

def Efield(chargedParticle, observationLocation):
    q = chargedParticle.charge
    r = observationLocation - chargedParticle.pos
    E = oofpez * chargedParticle.charge * norm(r) / (r.x**2 + r.y**2 + r.z**2)
    return E



## ========================================
## THIS FUNCTION CREATES A LINE OF CHARGE
##  v v v DO NOT ALTER THIS FUNCTION v v v 
## ========================================

def lineCharge(startPos, axis, mass, charge, N, color=color.red):
    # Creates a line of N uniform point charges with a given total charge and 
    # mass arranged at equal intervals on a line segment starting at startPos
    # and extending along axis
    line = []
    line.axis = axis
    line.pos = startPos
    spacing = axis/(N-1)   # vector separating adjacent charges
    q = Q/N     # magnitude of each point charge
    m = M/N     # mass of each point charge
    for ii in range(N):
        # There will be N point charges in this tape
        dq = sphere(pos=startPos+(ii*spacing), radius=mag(axis)/N, color=color)
        dq.charge = q
        dq.mass = m
        line.append(dq)
    return(line)

## ==============================================
##  ^ ^ ^  DO NOT ALTER THE ABOVE FUNCTION ^ ^ ^ 
## ==============================================



## ===========================================================================================================================================
## CREATING THE TAPES
## Create objects to represent the two tapes with each tape modeled as a collection of point charges placed side-by-side in a line.
## EDIT the y components of startPos attributes to represent correctly the vertical locations of the tapes in your experimental observations.
## You may also EDIT N to change the number of charges that you are using to model your tapes; be sure that N >= 1.
## ===========================================================================================================================================

# Position vector's units are cm
TopTape = lineCharge(startPos=vector(0,0.5,0), axis=vector(0.2,0,0), mass=M, charge=Q, N=10, color=color.magenta)
BottomTape = lineCharge(startPos=vector(0,0,0), axis=vector(0.2,0,0), mass=M, charge=Q, N=10, color=color.cyan)



## ============================================================================================
## CALCULATING THE ELECTRIC FIELD AND THE ELECTRIC FORCE
## (E at the location of TopTape produced by BottomTape, and F_E on TopTape due to BottomTape)
## ============================================================================================
##  * * * * * !!! MAKE SURE TO READ THE COMMENTS TO UNDERSTAND WHAT IS HAPPENING !!! * * * * *
## ============================================================================================


# WHAT IS HAPPENING HERE: 
# Each tape is simulated as a line of point charges (dq's). TopTape is the system, BottomTape is part of the surroundings. 
# At the location of each dq in TopTape, there is an electric field produced by the collection of charges that make up BottomTape. 
# We will create N arrows for these electric field vectors, placing their tails at each dq in TopTape.

E_scale = 5e-5     # arrowscale for electric field vector arrows -- EDIT THIS ONE LINE


# MORE ABOUT WHAT IS HAPPENING HERE:
# We will calculate the electric force on TopTape due to BottomTape (F_E_on_top) 
# by adding up the forces from each dq in BottomTape as they interact with each dq in TopTape. 
# Important: we ignore interactions between the dq's within each separate tape.

F_E_on_top = vector(0,0,0)  # net electric force on TopTape initialized at zero
F_E_scale = 1e2               # arrowscale for electric force arrow -- EDIT THIS ONE LINE
F_G_scale = F_E_scale       # arrowscale for gravity force arrow


for dq_top in TopTape:  # iterate through each piece of charge in TopTape
    E_at_dq_top = vector(0,0,0)     # initializing the net electric field at dq_top
    E_at_dq_top_arrow = arrow(pos=dq_top.pos, axis=E_scale*E_at_dq_top, color=color.green)
    
    for dq_bottom in BottomTape:    # iterate through each piece of charge in BottomTape

        # Calculate E-field at the location of dq_top due to dq_bottom
        dE_at_dq_top_by_dq_bottom = Efield(dq_bottom,dq_top.pos)
        E_at_dq_top = E_at_dq_top + dE_at_dq_top_by_dq_bottom

        # Calculate the electric force on dq_top due to dq_bottom -- EDIT THE NEXT LINE
        F_E_on_dq_top_by_dq_bottom = E_at_dq_top * dq_top.charge
        F_E_on_top = F_E_on_top + F_E_on_dq_top_by_dq_bottom

    # Create the arrow for the net electric field at dq_top due to BottomTape -- EDIT THIS NEXT LINE
    E_at_dq_top_arrow = arrow(pos=dq_top.pos, axis=E_scale*E_at_dq_top, color=color.green)
    


## ===========================================
## NET ELECTRIC FORCE AND GRAVITATIONAL FORCE
## ===========================================

# We will now create arrows to represent the net electric force on TopTape and the gravitational force on TopTape.
middleTop = TopTape.pos + 0.5*TopTape.axis    # place the tails of the arrows in the middle of TopTape

# Electric force vector -- EDIT THE AXIS TO CREATE THE ARROW
F_E_arrow = arrow(pos=middleTop, axis=F_E_scale * F_E_on_top, color=color.white)

# Gravitational force vector -- EDIT THE AXIS TO CREATE THE ARROW
F_G_arrow = arrow(pos=middleTop, axis=F_G_scale * M * g * vec(0, -1, 0), color=color.yellow)

print("Magnitude of electric force:", mag(F_E_on_top))
print("Magnitude of gravitational force:", M*g)

print("All done!")