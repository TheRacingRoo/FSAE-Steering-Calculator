

import numpy as np
import Steering_Forces
from Steering_Forces import pinion_gear_sizing

def lateral_force(Fnorm, mus):
    Flat = Fnorm * mus
    return Flat

def required_torque(fnorm, mus, rs, mechtrail, pneutrail, tsa):

    flat = lateral_force(fnorm, mus)

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
    ### DATA INPUT REGARDING VEHICLE GEOMETRY AND LOADING

    comp_minimum_corner_diameter = 9     #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
    autox_track_width = 3.5           #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
    tyre_width = 8 #Inches

    car_track_width = 45.8  #Inches
    wheelbase = 66.56   #Inches
    inner_slip_angle = 4 #Measured in degrees
    outer_slip_angle = 5.8 #Measured in degrees
    fos = 1      #Steering angle factor of safety

    Mechtrail = 0.609  # Mechanical Trail(in)
    Pneutrail = 1  # Pneumatic Trail(in)
    Tsa = 0  # Self aligning torque
    Rs = 3.2558  # Scrub Radius (in)
    Lsa = 3.018  # Steering Arm Length (in)

    Fnorm = 214.47  # Normal Tire Force (lbs)
    MUs = 1.2  # Static Coefficient of Friction

    Dgear = [0.938, 1, 1.125, 1.25, 1.31, 1.5, 1.625, 1.75]  # Gear Diameter
    Fsteer = 40  # Steering force input by the driver (lbs)
    Rwheel = 5  # Radius of the steering wheel (in)

    ###################################################################
    #Calculate minimum steering radius to meet minimum radius

    comp_minimum_outer_radius = (comp_minimum_corner_diameter / 2) * 39.37        #Minimum Outer Radius

    center_radius = comp_minimum_outer_radius - ((autox_track_width / 2.0) * 39.37)

    inner_radius = center_radius - (car_track_width / 2)
    outer_radius = center_radius + (car_track_width / 2)

    #Inside Tire
    inside_angle = np.rad2deg(np.pi / 2) - np.rad2deg(np.arccos((wheelbase / 2.0) / (inner_radius + 0.5 * tyre_width)))
    inside_angle = (inside_angle + inner_slip_angle) * fos



    #Outer Tire
    outside_angle = np.rad2deg((np.pi / 2) - np.arccos((wheelbase / 2.0) / (outer_radius + 0.5 * tyre_width)))
    print(outside_angle)
    outside_angle = (outside_angle + outer_slip_angle) * fos



    print("Inner required steering angle = " + str(inside_angle))
    print("Outside required steering angle = " + str(outside_angle))



    #STEERING FORCES
    Treq = required_torque(Fnorm, MUs,Rs, Mechtrail, Pneutrail, Tsa)
    Tapp = steering_torque(Rwheel, Fsteer, Dgear, Lsa)

    for i in range(Tapp.size):
        if Tapp[i]<=Treq:
            print("Smallest Possible Gear Diameter = " + str(Dgear[i - 1]))
            index = i
            break
        else:
            print("Required Torque = " + str(Treq), "Applied Torque = " + str(Tapp[i]))
            print(str(Dgear[i]) + "is too large")

    print("Required steering torque is " + str(Treq))
    print("Applied torque = " + str(Tapp[index-1]))
    answer = input("Are you satisfied? Y/N -> ")
    if answer == "Y" or answer == "y":
        print("Enjoy your race car\n\n\n")

    else:
        print("You done goofed, or I done goofed. Both are possible")

    return


if __name__ == "__main__":
    main()