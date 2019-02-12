import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
import wpilib.drive
import oi

import subsystems
import robotmap
#from commands.tankdriveteleopdefaultskid import TankDriveTeleopDefaultSkid as TankDriveTeleopDefaultSkid
from commands.tankdriveteleopdefaultnfs import TankDriveTeleopDefaultNFS as TankDriveTeleopDefaultNFS

class TankDrive(Subsystem):

    def __init__(self):
        print('TankDrive: init called')
        super().__init__('TankDrive')
        self.logPrefix = "TankDrive: "


        self.leftSpdCtrl = wpilib.Talon(robotmap.driveLine.leftMotorPort)
        if robotmap.driveLine.invertLeft:
            self.leftSpdCtrl.setInverted(True)

        self.rightSpdCtrl = wpilib.Talon(robotmap.driveLine.rightMotorPort)
        if robotmap.driveLine.invertRight:
            self.rightSpdCtrl.setInverted(True)
        
        self.rSensor = wpilib.AnalogInput(robotmap.driveLine.RtSensPort)
        self.lSensor = wpilib.AnalogInput(robotmap.driveLine.LftSensPort)
    # ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
            self.setDefaultCommand(TankDriveTeleopDefaultNFS()) #skid
            print("{}Default command set to DriveTeleopDefaultNFS".format(self.logPrefix))

    def driveRaw(self, left, right):
        forward = left > 0 and right > 0 
        spdLeft = left
        spdRight = right
        if oi.btnEnableLightSensor.get():
            r = self.rSensor.getVoltage()
            l = self.lSensor.getVoltage()
            tilted = "no tilt"

            if abs(l - r) > 0.1 and abs(l - r) <= 0.88 and forward:
                tilted = "small"
            elif abs(l - r) > 0.88 and abs(l - r) <= 1.4 and forward:
                tilted = "medium"
            elif abs(l - r) > 1.4 and abs(l - r) <= 2.1 and forward:
                tilted = "large"

            if tilted == "small":
                if (r > l):       # small tilt towards right
                    spdRight = max(1,right*(1+robotmap.driveLine.spdCompSmall))
                    spdLeft = left
                else:
                    spdRight = right
                    spdLeft = max(1,left*(1+robotmap.driveLine.spdCompSmall))
            if tilted == "medium":   
                if (r > l):       # medium tilt towards right
                    spdRight = max(1,right*(1+robotmap.driveLine.spdCompMedium))
                    spdLeft = left
                else:
                    spdRight = right
                    spdLeft = max(1,left*(1+robotmap.driveLine.spdCompMedium))
            if tilted == "large":  
                if (r > l):       # large tilt towards right
                    spdRight = max(1,right*(1+robotmap.driveLine.spdCompLarge))
                    spdLeft = left
                else:
                    spdRight = right
                    spdLeft = max(1,left*(1+robotmap.driveLine.spdCompLarge))
        
        self.leftSpdCtrl.set(spdLeft)
        self.rightSpdCtrl.set(spdRight)
    
    def stop(self):
        self.leftSpdCtrl.set(0.0)
        self.rightSpdCtrl.set(0.0)
