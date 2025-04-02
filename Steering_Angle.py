import numpy as np


#User Parameters
wheel2cg = 33.28    #Inches
minimum_corner_diameter = 9     #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
autox_track_width = 3           #INPUT IN METERS AS IS STATED IN FSAE EV RULES!!!!!!!! NOT INCHES
tyre_width = 8 #Inches
car_track_width = 45.8  #Inches

inner_slip_angle = 4 #Measured in degrees
outer_slip_angle = 5.5 #Measured in degrees

fos = 1.15

minimum_radius = (minimum_corner_diameter/2)-autox_track_width

minimum_radius *= 39.37     #Convert to inches

print(minimum_radius)


#Calculate Outer Tire Radius
outer_radius = minimum_radius + car_track_width

#Calculate inner and outer tire angles (True Ackerman)
inside_angle = np.rad2deg((np.pi/2) - np.arccos(wheel2cg/(minimum_radius + 0.5*tyre_width)))


outside_angle = np.rad2deg((np.pi/2) - np.arccos(wheel2cg/(outer_radius + 0.5*tyre_width)))

#Account for slip angle
inside_angle += inner_slip_angle
outside_angle += outer_slip_angle

print(inside_angle, outside_angle)


