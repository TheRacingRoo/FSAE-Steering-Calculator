import numpy as np


def Lateral_Force(Fnorm, mus):
    Flat = Fnorm * mus
    return Flat

def required_torque(fnorm, mus, rs, mechtrail, pneutrail, tsa):

    flat = Lateral_Force(fnorm, mus)

    xta = np.sqrt((rs**2)+((mechtrail + pneutrail)**2))

    self_aligning_torque = xta * flat + tsa

    return self_aligning_torque


def steering_torque(rwheel, fwheel, dgear, lsa):

    tsi = rwheel * fwheel #Calculate the steering wheel input torque
    fr = tsi / (dgear / 2) # Calculate the force applied on the linear rack
    applied_aligning_torque = fr * lsa #Aligning torque applied by the steering wheel. This force must be equal or greater than the required torque

    return applied_aligning_torque



def main():
    ### Input the following constant data here from suspension geometry or tire data

    Fnorm = 214.47  # Normal Tire Force (lbs)
    MUs = 1.2  # Static Coefficient of Friction
    Rs = 3.2558  # Scrub Radius (in)
    Mechtrail = 0.609  # Mechanical Trail(in)
    Pneutrail = 1  # Pneumatic Trail(in)
    Tsa = 0  # Self aligning torque

    Lsa = 3.018  # Steering Arm Length (in)
    Dgear = 1.31  # Gear Diameter
    Fsteer = 40  # Steering force input by the driver (lbs)
    Rwheel = 5  # Radius of the steering wheel (in)



    #Calculate the aligning torque present in the vehicle
    Treq = required_torque(Fnorm, MUs,Rs, Mechtrail, Pneutrail, Tsa)

    Tapp = steering_torque(Rwheel, Fsteer, Dgear, Lsa)

    if Tapp >= Treq:
        statement = True

    else:
        statement = False


    print("Required steering torque is " + Treq)
    print("Applied torque = " + Tapp)







    return



