import math

from wpilib.command import Command
import robotmap
import subsystems

import oi

class CloseCargoHold(Command):
    def __init__(self):
            super().__init__('CloseCargoHold')
            self.requires(subsystems.cargograb)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.cargograb.closeCargoHold(-1)

    def isFinished(self):
        return True