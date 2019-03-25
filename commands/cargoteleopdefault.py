import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class CargoTeleopDefault(Command):

    def __init__(self):
            super().__init__('CargoTeleopDefault')
            self.requires(subsystems.cargograb)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)
            self.anglelInitRight = subsystems.cargograb.zeroAngleRight()
            self.anglelInitLeft = subsystems.cargograb.zeroAngleLeft()

    def execute(self):
        if subsystems.cargograb.cargoToggle == True:
            subsystems.cargograb.openCargoHold()
        else:
            subsystems.cargograb.closeCargoHold()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False