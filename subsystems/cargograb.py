# Two servos acting as a claw, picking up and carrying cargo
# Connected to elevator
import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from commands.cargoteleopdefault import CargoTeleopDefault

import subsystems
import robotmap

class CargoGrab(Subsystem):
   
    def __init__(self):
        print('CargoGrab: init called')
        super().__init__('CargoGrab')
        self.logPrefix = "CargoGrab: "
    
        try:
            self.leftservo = wpilib.Servo(robotmap.cargograb.leftServoPort)
        except Exception as e:
            print("{}Exception caught instantiating left servo. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        try:
            self.rightservo = wpilib.Servo(robotmap.cargograb.rightServoPort)
        except Exception as e:
            print("{}Exception caught instantiating right servo. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

#-----------------------------------------------------------------------------------------


def initDefaultCommand(self):
    self.setDefaultCommand(CargoTeleopDefault)
    print("{}Default command set to CargoGrab".format(self.logPrefix)) 


def openCargoHold(self,openbit):
    self.leftservo.setAngle(openbit)
    self.rightservo.setAngle(openbit)

def closeCargoHold(self,closebit):
    self.leftservo.setAngle(closebit)
    self.rightservo.setAngle(closebit)

#def cargoGrabStop(self)
#    self.leftservo.
#    self.rightservo.
        

