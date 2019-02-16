import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput

import subsystems
import robotmap

class Ramp(Subsystem):
    def __init__(self):
        print("Ramp: init called")
        super().__init__('Ramp')
        self.logPrefix= 'Ramp: '
        self.rampSolenoid = wpilib.DoubleSolenoid(1, robotmap.ramp.solenoidExtendPort, robotmap.ramp.solenoidRetractPort)
 

    def extendRamp(self):
        self.rampSolenoid.set(1)

    def retractRamp(self): 
        self.rampSolenoid.set(2)