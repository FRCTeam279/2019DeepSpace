import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib import Solenoid 

import subsystems
import robotmap

class HatchGrab(Subsystem):
    def __init__(self):
        print('HatchGrab: init called')
        super().__init__('HatchGrab')
        self.logPrefix = "HatchGrab: "
        self.hatchGrabSolenoid = wpilib.Solenoid(1,robotmap.hatchgrab.solenoid)
    
    self.servo1 = wpilib.PWM(robotmap.cargograb)

    self.servo2 = wpilib.PWM(robotmap.cargograb
    def HatchOpen(self):
        self.hatchGrabSolenoid.set(1)

    def retractRamp(self): 
        self.hatchGrabSolenoid.set(2)


def initDefaultCommand(self):
    self.setDefaultCommand(CargoTeleopDefault)
    print("{}Default command set to CargoGrab".format(self.logPrefix)) 