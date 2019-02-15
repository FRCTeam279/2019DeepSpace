import math

from wpilib.command import Command
import robotmap
import subsystems
import oi
import time

class DriveRaw(Command):

    def __init__(self, left=0.0, right=0.0, duration=0.0):
            super().__init__('DriveRaw')
            self.requires(subsystems.driveline)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)
            self.left = left
            self.right = right
            self.duration = duration
            self.endTime = 0

    def initialize(self):
        self.endTime = time.time() + self.duration


    def execute(self):
        subsystems.driveline.driveRaw(self.left, self.right)
   
    def isFinished(self):
        if time.time() > self.endTime:
            return True
        return False

    def end(self):
        self.endTime = 0
        subsystems.driveline.driveRaw(0, 0)

    def interrupted(self):
        self.endTime = 0