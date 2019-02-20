import math
import wpilib


class ConfigHolder:
    """Dummy class to add config parameters too"""
    pass


# flag if we are at competition and want to use development features in the code
# Robot.init() will set this based on FMS being attached
devMode = False



# ----------------------------------------------------------
# Driveline Subsystem Config
# ----------------------------------------------------------
driveLine = ConfigHolder()

driveLine.leftMotorPort = 0
driveLine.rightMotorPort = 1
driveLine.speedControllerType = "TALON" # or "VICTORSP"
driveLine.controlStyle = "nfs"          # or "skid"

driveLine.frontIRPort = 0       # IN ANALOG I/O        
driveLine.backIRPort = 1        # IN ANALOG I/O   
     
driveLine.spdCompSmall = .4
driveLine.spdCompMedium = .6
driveLine.spdCompLarge = .8
driveLine.RtSensPort = 3        # Line detect analog input right-sensor port 
driveLine.LftSensPort = 2       # Line detect analog input left-sensor port

#Driveline solenoid lifts
driveLine.solenoidExtendFrontPort = 1
driveLine.solenoidRetractFrontPort = 0
driveLine.solenoidExtendBackPort = 3
driveLine.solenoidRetractBackPort = 2

# the new MecanumDrive library from WPILIP inverts the right motors by default, so inversion is often not needed.
# Be sure to view the wheel direction when moving side to side and forward/backward on mounts before testing on ground to verify
# and remember that the rollers on the wheels should form an X when looked at from the top/bottom
#  (ie right rear and left front wheels rolers are aligned in same direction, etc..)
driveLine.invertLeft = False
driveLine.invertRight = False
#driveLine.invertRightRear = False

# ----------------------------------------------------------
# NFS Driving Config
# ----------------------------------------------------------
nfs = ConfigHolder()
nfs.debugTurning = False

"""
Turn scaling is used to reduce the maximum ammount of turn as the throttle increases to improve stability and
make the feel closer to that of driving a car

Heavy scalling is used while driving "slow", and lighter scaling is used during normal driving
Thus:
lowTurnScale -> normal driving
highTurnScale -> "slow" driving (while holding left trigger)

"""
nfs.lowTurnScale = 0.3                  # How much to reduce turn speed when driving at full throttle at
nfs.highTurnScale = 0.2
nfs.slowDriveSpeedFactor = 0.7          # Max speed when driving in slow mode

"""
minTimeFullThrottleChange
The minimum amount of time that the tank drive will allow the motors to switch from -1.0 to +1.0
Example: a value of 1 means that it will take 1 sec for the speed controllers to be updated from -1.0 to +1.0

The maximum speed controller change per periodic call is thus 
maxThrottleChange = totalThrottleRange (2) * callSpeed (0.02sec) / time (minTimeFullThrottleChange)

0.02 = 50 times per second (the updated packets to the robot
"""
nfs.minTimeFullThrottleChange = 1.5
nfs.maxSpeedChange = (2 * 0.02) / nfs.minTimeFullThrottleChange

# ----------------------------------------------------------
# elevator Subsystem Config
# ----------------------------------------------------------

#reconfigure these ports
elevator = ConfigHolder()
elevator.btmLimitSwitchPort = 6     # DIO port
elevator.motorPort = 2              # in pwm 2, to the spark relay
#elevator.btmLimitNormalClosed = False   # switch is normally cosed
elevator.scaleSpdUp = 0.8
elevator.scaleSpdDown = 0.8
elevator.holdSpeed = 0

elevator.maxHeight = 230        # encoder counts
elevator.hatchHeight = 22       # inches
elevator.margin = 0.5           # elevator automatic movement tolerance
elevator.elevatorDeadZone = .05
elevator.inchesPerTick = .117   # or 8.56 TICKS per inch

elevator.encAPort = 4
elevator.encBPort = 5
elevator.encType = wpilib.Encoder.EncodingType.k4X
elevator.encReverse = True
#100 ticks per revolution, a 2 inch diameter pulley (1.0in radius)

#---------------------------------------------------------------------------------------------
# ramp Subsystem Config
#---------------------------------------------------------------------------------------------
ramp = ConfigHolder()
ramp.solenoidExtendPort = 4
ramp.solenoidRetractPort = 5

# ----------------------------------------------------------
# General Sensors Config
# ----------------------------------------------------------
sensors = ConfigHolder()
sensors.hasAHRS = True

#------------------------------------------------------------
# Cargo Grab Config
#------------------------------------------------------------
cargograb = ConfigHolder()
cargograb.rightServoPort = 5
cargograb.leftServoPort = 6
cargograb.openAngle = 90        # RECONFIGURE
cargograb.closeAngle = 0        # RECONFIGURE

#-----------------------------------------------------------
# Hatch Grab Config
#-----------------------------------------------------------
hatchgrab = ConfigHolder()
hatchgrab.solenoidExtendPort = 6
hatchgrab.solenoidRetractPort = 7

print("RobotMap module completed load")