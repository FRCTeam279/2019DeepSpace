import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib import Solenoid
#from commands.hatchgrabteleopdefault import HatchGrabTeleopDefault    # This doesnt exist

import subsystems
import robotmap

class HatchGrab(Subsystem):
    def __init__(self):
        print('HatchGrab: init called')
        super().__init__('HatchGrab')
        self.logPrefix = "HatchGrab: "
        self.hatchGrabSolenoid = wpilib.DoubleSolenoid(1, robotmap.hatchgrab.solenoidExtendPort, robotmap.hatchgrab.solenoidRetractPort)
        
    def HatchOpen(self):
        self.hatchGrabSolenoid.set(1)

    def retractRamp(self): 
        self.hatchGrabSolenoid.set(2)

    #def initDefaultCommand(self):
    #    self.setDefaultCommand(HatchGrabTeleopDefault())
    #    print("{}Default command set to CargoGrab".format(self.logPrefix)) 