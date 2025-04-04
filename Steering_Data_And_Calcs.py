import Steering_Forces as sf
import Steering_Angle as sa

def main():
    ### DATA INPUT REGARDING VEHICLE GEOMETRY AND LOADING

    minimum_corner_diameter = 9     #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
    autox_track_width = 3           #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
    tyre_width = 8 #Inches

    car_track_width = 45.8  #Inches
    wheel2cg = 33.28    #Inches - Make sure this is the correct value
    inner_slip_angle = 4 #Measured in degrees
    outer_slip_angle = 5.5 #Measured in degrees
    fos = 1.15

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






    return
if __name__ == "__main__":
    main()