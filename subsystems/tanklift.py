import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput
from commands.tankliftteleopdefault import TankLiftTeleopDefault

import subsystems
import robotmap

class TankLift(Subsystem):

    def __init__(self):
        print('TankLift: init called')
        super().__init__('TankLift')
        self.logPrefix = "TankLift: "

        self.frontCylinder = wpilib.DoubleSolenoid(1,0,1) # 1st arg= CAN ID=1, then takes ports on pcm to energize solenoid
        self.backCylinder =  wpilib.DoubleSolenoid(1,2,3) # 1st arg= CAN ID=1, ...
        self.frontIR = wpilib.DigitalInput(robotmap.driveLine.frontIRPort)
        self.backIR = wpilib.DigitalInput(robotmap.driveLine.backIRPort)

    # ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
        self.setDefaultCommand(TankLiftTeleopDefault())
        print("{}Default command set to TankLiftTeleopDefault".format(self.logPrefix))
 
    def extendAll(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(1)
   
    def retractAll(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(2)

    def extendFront(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(2)

    def extendBack(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(1)
        #this may not be needed in the actual sequence of final robot since the front will always be extended when the back extends
 
    def retractFront(self):      
        if self.frontIR.get() == False:
            self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
    
    def retractBack(self):
        if self.backIR.get() == False:
            self.backCylinder.set(2)    # 1: extend, 2: retract, 0: off
    
    # more functions for sophisticated functionality

