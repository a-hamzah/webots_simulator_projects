# Import necessary modules
from controller import Robot

# Define the time step of the simulation (in milliseconds)
TIME_STEP = 64

# Initialize the Robot instance
robot = Robot()

# Define the maximum speed of the e-puck motors
MAX_SPEED = 6.28

# Set the desired speed (in fraction of MAX_SPEED)
desired_speed_fraction = 0.5
speed = desired_speed_fraction * MAX_SPEED

# Get references to the robot's motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set the initial speed of the motors
left_motor.setVelocity(speed)
right_motor.setVelocity(speed)

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Nothing needs to be done here, the robot is already moving forward
    pass

# This code will make the e-puck move forward indefinitely
