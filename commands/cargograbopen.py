import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class OpenCargoHold(Command):
    def __init__(self):
            super().__init__('OpenCargoHold')
            self.requires(subsystems.cargograb)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.cargograb.openCargoHold(1)

    def isFinished(self):
        return True