import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class HatchGrabTeleopDefault(Command):
    def __init__(self):
            super().__init__('HatchGrabTeleopDefault')
            self.requires(subsystems.hatchgrab)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        hatchToggle = False
        if (oi.btnHatchGrabTog.get() == True) and (hatchToggle == False):
            hatchToggle = True
        elif (oi.btnHatchGrabTog.get() == True) and (hatchToggle == True):
            hatchToggle = False
        
        if hatchToggle == True:
            subsystems.hatchgrab.HatchOpen()
        else:
            subsystems.hatchgrab.HatchClose()

    def isFinished(self):
        return True