import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
import wpilib.drive
from wpilib.drive import MecanumDrive

import subsystems
import robotmap
from commands.mecdriveteleopdefaultfps import MecDriveTeleopDefaultFPS

class MecDrive(Subsystem):

    def __init__(self):
        print('MecDrive: init called')
        super().__init__('MecDrive')
        self.logPrefix = "MecDrive: "


        self.leftFrontSpdCtrl = wpilib.Talon(robotmap.driveLine.leftFrontMotorPort)
        if robotmap.driveLine.invertLeftFront:
            self.leftFrontSpdCtrl.setInverted(True)

        self.rightFrontSpdCtrl = wpilib.Talon(robotmap.driveLine.rightFrontMotorPort)
        if robotmap.driveLine.invertRightFront:
            self.rightFrontSpdCtrl.setInverted(True)

        
        self.leftRearSpdCtrl = wpilib.Talon(robotmap.driveLine.leftRearMotorPort)
        if robotmap.driveLine.invertLeftRear:
            self.leftRearSpdCtrl.setInverted(True)

        self.rightRearSpdCtrl = wpilib.Talon(robotmap.driveLine.rightRearMotorPort)
        if robotmap.driveLine.invertRightRear:
            self.rightRearSpdCtrl.setInverted(True)

        #https://robotpy.readthedocs.io/projects/wpilib/en/latest/wpilib.drive/MecanumDrive.html#wpilib.drive.mecanumdrive.MecanumDrive
        self.mecanumDrive = MecanumDrive(self.leftFrontSpdCtrl, self.leftRearSpdCtrl, self.rightFrontSpdCtrl, self.rightRearSpdCtrl)



    # ------------------------------------------------------------------------------------------------------------------
    def initDefaultCommand(self):
            self.setDefaultCommand(MecDriveTeleopDefaultFPS())
            print("{}Default command set to MecDriveTeleopDefaultFPS".format(self.logPrefix))

    def stop(self):
        self.mecanumDrive.stopMotor()
