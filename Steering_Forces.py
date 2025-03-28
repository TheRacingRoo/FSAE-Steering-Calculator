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
    fr = np.zeros(len(dgear))

    applied_aligning_torque = np.zeros(np.size(dgear))  #Create array for storing aligning torque values

    for i in range(np.size(dgear)):
        #print("Count " + str(i))       #Check
        #print("Dgear " + str(dgear))   #Check
        fr[i] = tsi / (dgear[i] / 2) # Calculate the force applied on the linear rack
        #print(fr[i])   #Check

        #print(applied_aligning_torque) #Checks
        applied_aligning_torque[i] = fr[i] * lsa #Aligning torque applied by the steering wheel. This force must be equal or greater than the required torque
        #print(applied_aligning_torque) #Checks

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
    Dgear = [0.938, 1, 1.125, 1.25, 1.31 , 1.5, 1.625, 1.75]# Gear Diameter
    Fsteer = 40  # Steering force input by the driver (lbs)
    Rwheel = 5  # Radius of the steering wheel (in)



    #Calculate the aligning torque present in the vehicle
    Treq = required_torque(Fnorm, MUs,Rs, Mechtrail, Pneutrail, Tsa)
    Tapp = steering_torque(Rwheel, Fsteer, Dgear, Lsa)
    #print(Tapp)

    for i in range(Tapp.size):
        if Tapp[i]<=Treq:
            print("Smallest Possible Gear Diameter = " + str(Dgear[i]))
            index = i
            break
        else:
            print(str(Dgear[i]) + "is too small")




    print("Required steering torque is " + str(Treq))
    print("Applied torque = " + str(Tapp[i]))
    answer = input("Are you satisfied? Y/N -> ")
    if answer == "Y" or answer == "y":
        print("Enjoy your race car")

    else:
        print("You done goofed, or I done goofed. Both are possible")

    return

if __name__ == "__main__":
    main()