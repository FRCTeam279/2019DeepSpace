import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
import wpilib.drive
import oi

import subsystems
import robotmap
from commands.tankdriveteleopdefaultskid import TankDriveTeleopDefaultSkid as TankDriveTeleopDefaultSkid
from commands.tankdriveteleopdefaultnfs import TankDriveTeleopDefaultNFS as TankDriveTeleopDefaultNFS

class TankDrive(Subsystem):

    def __init__(self):
        print('TankDrive: init called')
        super().__init__('TankDrive')
        self.logPrefix = "TankDrive: "


    # Speed Controllers
        if robotmap.driveLine.speedControllerType == "TALON":
            try:
                self.leftSpdCtrl = wpilib.Talon(robotmap.driveLine.leftMotorPort)
                if robotmap.driveLine.invertLeft:
                    self.leftSpdCtrl.setInverted(True)
            except Exception as e:
                print("{}Exception caught instantiating left speed controller. {}".format(self.logPrefix, e))
                if not wpilib.DriverStation.getInstance().isFmsAttached():
                    raise
        
        else:
            try:
                self.leftSpdCtrl = wpilib.VictorSP(robotmap.driveLine.leftMotorPort)
                if robotmap.driveLine.invertLeft:
                    self.leftSpdCtrl.setInverted(True)
            except Exception as e:
                print("{}Exception caught instantiating left speed controller. {}".format(self.logPrefix, e))
                if not wpilib.DriverStation.getInstance().isFmsAttached():
                    raise

        if robotmap.driveLine.speedControllerType == "TALON":
            try:
                self.rightSpdCtrl = wpilib.Talon(robotmap.driveLine.rightMotorPort)
                if robotmap.driveLine.invertRight:
                    self.rightSpdCtrl.setInverted(True)
            except Exception as e:
                print("{}Exception caught instantiating right speed controller. {}".format(self.logPrefix, e))
                if not wpilib.DriverStation.getInstance().isFmsAttached():
                    raise
        
        else:
            try:
                self.rightSpdCtrl = wpilib.VictorSP(robotmap.driveLine.rightMotorPort)
                if robotmap.driveLine.invertRight:
                    self.rightSpdCtrl.setInverted(True)
            except Exception as e:
                print("{}Exception caught instantiating right speed controller. {}".format(self.logPrefix, e))
                if not wpilib.DriverStation.getInstance().isFmsAttached():
                    raise
        
    # IR Sensors
        try:
            self.rSensor = wpilib.AnalogInput(robotmap.driveLine.RtSensPort)
        except Exception as e:
            print("{}Exception caught instantiating right line sensor. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise
        
        try:
            self.lSensor = wpilib.AnalogInput(robotmap.driveLine.LftSensPort)
        except Exception as e:
            print("{}Exception caught instantiating left line sensor. {}".format(self.logPrefix, e))
            if not wpilib.DriverStation.getInstance().isFmsAttached():
                raise

    # ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
        if robotmap.driveLine.controlStyle == "nfs":
            self.setDefaultCommand(TankDriveTeleopDefaultNFS())
            print("{}Default command set to DriveTeleopDefaultNFS".format(self.logPrefix))

        else:
            self.setDefaultCommand(TankDriveTeleopDefaultSkid())
            print("{}Default command set to DriveTeleopDefaultSkid".format(self.logPrefix))

    def driveRaw(self, left, right):
        forward = left > 0 and right > 0 
        spdLeft = left
        spdRight = right

        if oi.btnEnableLightSensor.get():
            r = self.rSensor.getVoltage()
            l = self.lSensor.getVoltage()
            spdReduce = 0.5
            spdCorr1 = 1  #0.8
            spdCorr2 = 1  #.7
            spdCorr3 = 1  #.5
            if forward:
                spdLeft = spdReduce*spdLeft
                spdRight = spdReduce*spdRight
            
            if abs(l - r) > 0.1 and abs(l - r) <= 0.88 and forward:   # small tilt
                if (r > l):       # small tilt towards right
                    spdRight = min(1,spdRight*(1+robotmap.driveLine.spdCompSmall))
                    spdLeft = spdLeft*spdCorr1
                else:
                    spdRight = spdRight*spdCorr1
                    spdLeft = min(1,spdLeft*(1+robotmap.driveLine.spdCompSmall))
                    
            elif abs(l - r) > 0.88 and abs(l - r) <= 1.4 and forward:  # medium tilt
                if (r > l):       # medium tilt towards right
                    spdRight = min(1,spdRight*(1+robotmap.driveLine.spdCompMedium))
                    spdLeft = spdLeft*spdCorr2
                else:
                    spdRight = spdRight*spdCorr2
                    spdLeft = min(1,spdLeft*(1+robotmap.driveLine.spdCompMedium))

            elif abs(l - r) > 1.4 and abs(l - r) <= 2.1 and forward:  # large tilt
                if (r > l):       # large tilt towards right
                    spdRight = min(1,spdRight*(1+robotmap.driveLine.spdCompLarge))
                    spdLeft = spdLeft*spdCorr3
                else:
                    spdRight = spdRight*spdCorr3
                    spdLeft = min(1,spdLeft*(1+robotmap.driveLine.spdCompLarge))

        self.leftSpdCtrl.set(spdLeft)
        self.rightSpdCtrl.set(spdRight)
    
    def stop(self):
        if self.leftSpdCtrl:
            self.leftSpdCtrl.set(0.0)
        if self.rightSpdCtrl:
            self.rightSpdCtrl.set(0.0)
