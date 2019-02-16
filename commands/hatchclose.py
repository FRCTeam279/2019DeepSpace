import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class HatchClose(Command):
    def __init__(self):
            super().__init__('HatchClose')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.hatchgrab.HatchClose()

    def isFinished(self):
       return True 