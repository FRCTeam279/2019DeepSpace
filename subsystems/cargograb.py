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
            self.rightServo = wpilib.Servo(robotmap.cargograb.rightServoPort)
        except Exception as e:
            print("{}Exception caught instantiating right servo. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        try:
            self.leftServo = wpilib.Servo(robotmap.cargograb.leftServoPort)
        except Exception as e:
            print("{}Exception caught instantiating left servo. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        self.cargoToggle = False
        self.openAngleRight = robotmap.cargograb.openAngleRight
        self.closeAngleRight = robotmap.cargograb.closeAngleRight

        self.openAngleLeft = robotmap.cargograb.openAngleLeft
        self.closeAngleLeft = robotmap.cargograb.closeAngleLeft
        
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
        self.rightServo.setAngle(self.openAngleRight + self.angleInitRight)
        self.leftServo.setAngle(self.openAngleLeft + self.angleInitLeft)
       
    def closeCargoHold(self):
        self.rightServo.setAngle(self.closeAngleRight + self.angleInitRight)
        self.leftServo.setAngle(self.closeAngleLeft + self.angleInitLeft)
      
    def zeroAngleRight(self):
        self.angleInitRight = self.rightServo.getAngle()
        return self.angleInitRight

    def zeroAngleLeft(self):
        self.angleInitLeft = self.leftServo.getAngle()
        return self.angleInitLeft
        
