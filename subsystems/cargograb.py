import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from commands.cargoteleopdefault import CargoTeleopDefault

import subsystems
import robotmap
import oi

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
        
        self.cargoToggle = False
        self.openAngle = robotmap.cargograb.openAngle
        self.closeAngle = robotmap.cargograb.closeAngle

#-----------------------------------------------------------------------------------------
    def cargoTogFunction(self):
        if self.cargoToggle == False:
            self.cargoToggle = True
        else:
            self.cargoToggle = False
            
        return self.cargoToggle

    def initDefaultCommand(self):
        self.setDefaultCommand(CargoTeleopDefault())
        print("{}Default command set to CargoGrab".format(self.logPrefix)) 

    def openCargoHold(self):
        self.leftservo.setAngle(self.openAngle)
        self.rightservo.setAngle(self.openAngle)

    def closeCargoHold(self):
        self.leftservo.setAngle(self.closeAngle)
        self.rightservo.setAngle(self.closeAngle)

    #def cargoGrabStop(self)
    #    self.leftservo.
    #    self.rightservo.
            

