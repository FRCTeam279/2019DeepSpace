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

        try:
            self.rampSolenoid = wpilib.DoubleSolenoid(1, robotmap.ramp.solenoidExtendPort, robotmap.ramp.solenoidRetractPort)
        except Exception as e:
            print("{}Exception caught instantiating ramp solenoid. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

    def extendRamp(self):
        self.rampSolenoid.set(1)   # 1: extend, 2: retract, 0: off

    def retractRamp(self): 
        self.rampSolenoid.set(2)   # 1: extend, 2: retract, 0: off