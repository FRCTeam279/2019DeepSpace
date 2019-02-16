import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class HatchOpen(Command):
    def __init__(self):
            super().__init__('HatchOpen')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.hatchgrab.HatchOpen()

    def isFinished(self):
        return True