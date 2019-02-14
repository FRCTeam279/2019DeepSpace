import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class DriveRaw(Command):

    def __init__(self, left=0.0, right=0.0):
            super().__init__('DriveRaw')
            self.requires(subsystems.driveline)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)
            self.left = left
            self.right = right

    #def initialize():


    def execute(self):
        subsystems.driveline.driveRaw(self.left, self.right)

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
