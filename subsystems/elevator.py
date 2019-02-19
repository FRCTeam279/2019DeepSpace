import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
#from commands.elevatormoveup import ElevatorMoveUp
#from commands.elevatormovedown import ElevatorMoveDown
from commands.elevatorteleopdefault import ElevatorTeleopDefault

import subsystems
import robotmap

class Elevator(Subsystem):
 
    def __init__(self):
        print('Elevator: init called')
        super().__init__('Elevator')
        self.logPrefix = "Elevator: "

        try:
            self.elevatorSpdCtrl = wpilib.Spark(robotmap.elevator.motorPort)
        except Exception as e:
            print("{}Exception caught instantiating elevator speed controller. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        try:
            self.elevatorEncoder = wpilib.Encoder(robotmap.elevator.encAPort, robotmap.elevator.encBPort, robotmap.elevator.encReverse, robotmap.elevator.encType)
            self.elevatorEncoder.setDistancePerPulse(robotmap.elevator.inchesPerTick)
        except Exception as e:
            print("{}Exception caught instantiating elevator encoder. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        self.elevatorHeight = self.elevatorEncoder.get()*robotmap.elevator.inchesPerTick
        self.btmLimitSwitch = wpilib.DigitalInput(robotmap.elevator.btmLimitSwitchPort)

# ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
        self.setDefaultCommand(ElevatorTeleopDefault())
        print("{}Default command set to ElevatorTeleopDefault".format(self.logPrefix))

    def stopElevator(self):
        self.elevatorSpdCtrl.set(0.0)

    def holdElevator(self):
        if self.btmLimitSwitch.get():
            self.elevatorSpdCtrl.set(0.0)
            #self.elevatorEncoder.reset()
        else:
            self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed)

# -----------------------------------------------------------------------------

    def rawMove(self, speed):
        self.elevatorSpdCtrl.set(speed)

    def move(self, speed):
        btmLimit = self.btmLimitSwitch.get()

        if btmLimit == True:
            self.elevatorEncoder.reset()

        dist = self.elevatorHeight   # encoder counts for now
        topLimit = dist >= robotmap.elevator.maxHeight

        if (btmLimit and speed <= 0.0):
            self.elevatorSpdCtrl.set(0)
        elif (topLimit and speed > 0.0):
            self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed)
        else:
            if speed > 0:
                self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed + abs(robotmap.elevator.scaleSpdUp*speed))
            else:
                self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed - abs(robotmap.elevator.scaleSpdDown*speed))

    def elevatorMoveHatchHeight(self):
        if self.btmLimitSwitch.get() == True:
            self.elevatorEncoder.reset()

        if self.elevatorHeight > robotmap.elevator.hatchHeight + robotmap.elevator.margin:
            self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed - abs(robotmap.elevator.scaleSpdDown*-0.75))
        elif self.elevatorHeight < robotmap.elevator.hatchHeight - robotmap.elevator.margin:
            self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed + abs(robotmap.elevator.scaleSpdDown*0.75))
        else:
            self.elevatorSpdCtrl.set(robotmap.elevator.holdSpeed)

    def elevatorMoveUp(self, speed):
        if self.btmLimitSwitch.get() == True:
            self.elevatorEncoder.reset()

        self.elevatorSpdCtrl.set(speed)

    def elevatorMoveDown(self, speed):
        if self.btmLimitSwitch.get() == True:
            self.elevatorEncoder.reset()
            
        if not self.btmLimitSwitch:
            self.elevatorSpdCtrl.set(speed)

        else:
            self.elevatorSpdCtrl.set(0.0)

    def resetEncoders(self):
        self.elevatorEncoder.reset()
