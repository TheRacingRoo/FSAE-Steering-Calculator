import numpy as np


def min_radius(minimum_corner_diameter,autox_track_width):
    minimum_radius = (minimum_corner_diameter / 2) - autox_track_width

    minimum_radius *= 39.37  # Convert to inches

    return minimum_radius

def outer_min_angle(minimum_radius,car_track_width,tyre_width,wheel2cg,outer_slip_angle,fos):
    # Calculate Outer Tire Radius
    outer_radius = minimum_radius + car_track_width

    outside_angle = np.rad2deg((np.pi / 2) - np.arccos(wheel2cg / (outer_radius + 0.5 * tyre_width)))

    outside_angle += outer_slip_angle

    outside_angle *= fos

    return outside_angle

def inner_min_angle(minimum_radius,tyre_width,wheel2cg, inner_slip_angle,fos):
    inside_angle = np.rad2deg((np.pi / 2) - np.arccos(wheel2cg / (minimum_radius + 0.5 * tyre_width)))

    inside_angle += inner_slip_angle
    inside_angle *= fos
    return inside_angle

def main():
    #User Parameters
    wheel2cg = 33.28    #Inches
    minimum_corner_diameter = 9     #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
    autox_track_width = 3           #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
    tyre_width = 8 #Inches
    car_track_width = 45.8  #Inches

    inner_slip_angle = 4 #Measured in degrees
    outer_slip_angle = 5.5 #Measured in degrees

    fos = 1

    minimum_radius = min_radius(minimum_corner_diameter,autox_track_width)

    outside_angle = outer_min_angle(minimum_radius,car_track_width,tyre_width,wheel2cg,outer_slip_angle,fos)

    inside_angle = inner_min_angle(minimum_radius,tyre_width,wheel2cg,inner_slip_angle,fos)

    print(inside_angle,outside_angle)


if __name__ == "__main__":
    main()