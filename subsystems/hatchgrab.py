import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib import Solenoid
from commands.hatchgrabteleopdefault import HatchGrabTeleopDefault

import subsystems
import robotmap
import oi

class HatchGrab(Subsystem):
    def __init__(self):
        print('HatchGrab: init called')
        super().__init__('HatchGrab')
        self.logPrefix = "HatchGrab: "

        try:
            self.hatchGrabSolenoid = wpilib.DoubleSolenoid(1, robotmap.hatchgrab.solenoidExtendPort, robotmap.hatchgrab.solenoidRetractPort)
        except Exception as e:
            print("{}Exception caught instantiating hatch grabber solenoid. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise       

        self.hatchToggle = False

    def hatchTogFunction(self):
        if oi.btnHatchGrabTog:
            if self.hatchToggle == False:
                self.hatchToggle = True
            else:
                self.hatchToggle = False
            
        return self.hatchToggle

    def HatchOpen(self):
        self.hatchGrabSolenoid.set(1)   # 1: extend, 2: retract, 0: off

    def HatchClose(self): 
        self.hatchGrabSolenoid.set(2)   # 1: extend, 2: retract, 0: off

    def initDefaultCommand(self):
        self.setDefaultCommand(HatchGrabTeleopDefault())
        print("{}Default command set to HatchGrabTeleopDefault".format(self.logPrefix)) 