import math

from wpilib.command import Command
import robotmap 
import subsystems
import oi
import utility.navhelper as navhelper


class MecDriveTeleopDefaultFPS(Command):
    '''
    One joystick controls rotation, and the other translation
    '''


    def __init__(self):
        super().__init__('MecDriveTeleopDefaultFPS')
        self.requires(subsystems.driveline)
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)


    def execute(self):
        if oi.leftDriverStick is None or oi.rightDriverStick is None:
            return
            
        y = oi.leftDriverStick.getY()
        x = oi.leftDriverStick.getX()
        z = oi.rightDriverStick.getX()

        if oi.btnDriveSlow.get():
            y = y/2
            x = x/2
        
        x = oi.filterInput(x, oi.config.leftDriverStickNullZone, 1)
        y = oi.filterInput(y, oi.config.leftDriverStickNullZone, 1)
        z = oi.filterInput(z, oi.config.rightDriverStickNullZone, 1)

        magnitude = math.sqrt((x * x) + (y * y))

        #Robot oriented
        #roboDrive.mecanumDrive_Polar(magnitude, oi.leftDriverStick.getDirectionDegrees(), z);

        #Field Oriented
        subsystems.driveline.mecanumDrive.drivePolar(magnitude, navhelper.addDegrees(oi.leftDriverStick.getDirectionDegrees(), -1 * robotmap.sensors.ahrs.getAngle()), z)


    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False
