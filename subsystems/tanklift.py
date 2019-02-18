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

        try:
            self.frontCylinder = wpilib.DoubleSolenoid(1, robotmap.driveLine.solenoidRetractFrontPort, robotmap.driveLine.solenoidExtendFrontPort) # 1st arg= CAN ID=1, then takes ports on pcm to energize solenoid
        except Exception as e:
            print("{}Exception caught instantiating front lift cylinder. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        try:
            self.backCylinder =  wpilib.DoubleSolenoid(1, robotmap.driveLine.solenoidRetractBackPort, robotmap.driveLine.solenoidExtendBackPort)
        except Exception as e:
            print("{}Exception caught instantiating back lift cylinder. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        try:
            self.frontIR = wpilib.AnalogInput(robotmap.driveLine.frontIRPort)
        except Exception as e:
            print("{}Exception caught instantiating front IR sensor. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        try:
            self.backIR = wpilib.AnalogInput(robotmap.driveLine.backIRPort)
        except Exception as e:
            print("{}Exception caught instantiating back IR sensor. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

        self.allSolToggle = False
        self.frontSolToggle = False
        self.backSolToggle = False

    # ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
        self.setDefaultCommand(TankLiftTeleopDefault())
        print("{}Default command set to TankLiftTeleopDefault".format(self.logPrefix))
 
    def extendAll(self):
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(1)
   
    def retractAll(self):
        self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(2)

    def extendFront(self):
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(2)

    def extendBack(self):
        self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
        self.backCylinder.set(1)

 
    def retractFront(self):      
        if self.frontIR.getVoltage() == 1:
            self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
    
    def retractBack(self):
        if self.backIR.getVoltage() == 1:
            self.backCylinder.set(2)    # 1: extend, 2: retract, 0: off