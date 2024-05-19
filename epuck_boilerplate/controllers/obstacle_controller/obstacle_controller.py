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

# Get and enable the forward ultrasonic sensors
ps0 = robot.getDevice('ps0')
ps1 = robot.getDevice('ps1')

ps0.enable(TIME_STEP)
ps1.enable(TIME_STEP)

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Read sensor values
    ps0_value = ps0.getValue()
    ps1_value = ps1.getValue()
    
    # Threshold for obstacle detection
    threshold = 80.0  # Adjust this value based on your needs

    # Initialize motor speeds
    left_speed = speed
    right_speed = speed

    # Simple obstacle avoidance logic
    if ps0_value > threshold and ps1_value > threshold:
        # Obstacle detected directly in front, turn right
        left_speed = speed * 0.5
        right_speed = -speed * 0.5
    elif ps0_value > threshold:
        # Obstacle detected on the right, turn left
        left_speed = speed * 0.5
        right_speed = -speed * 0.5
    elif ps1_value > threshold:
        # Obstacle detected on the left, turn right
        left_speed = -speed * 0.5
        right_speed = speed * 0.5

    # Set the motor speeds
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
