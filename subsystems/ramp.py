import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput
from commands.rampteleopdefault import RampTeleopDefault

import subsystems
import robotmap
import oi

class Ramp(Subsystem):
    def __init__(self):
        print("Ramp: init called")
        super().__init__('Ramp')
        self.logPrefix= 'Ramp: '

        self.rampToggle = False     # Default

        try:
            self.rampSolenoid = wpilib.DoubleSolenoid(1, robotmap.ramp.solenoidExtendPort, robotmap.ramp.solenoidRetractPort)
        except Exception as e:
            print("{}Exception caught instantiating ramp solenoid. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        #def rampTogFunction(self):
        if oi.btnRampTog:
            if self.rampToggle == False:
                self.rampToggle = True
            else:
                self.rampToggle = False
                
        #return self.rampToggle

    def extendRamp(self):
        self.rampSolenoid.set(1)   # 1: extend, 2: retract, 0: off

    def retractRamp(self): 
        self.rampSolenoid.set(2)   # 1: extend, 2: retract, 0: off

    def initDefaultCommand(self):
        self.setDefaultCommand(RampTeleopDefault())
        print("{}Default command set to HatchGrabTeleopDefault".format(self.logPrefix))
