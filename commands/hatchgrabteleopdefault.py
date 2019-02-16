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

        #self.hatchBtnState = oi.goGamePad.getRawButton(oi.config.btnHatchGrabTogIndex)


        def execute(self):
        #    hatchToggle = False
        #    if (self.hatchBtnState == True) and (hatchToggle == False):
        #        hatchToggle = True
        #    elif (self.hatchBtnState == True) and (hatchToggle == True):
        #        hatchToggle = False

            if subsystems.hatchgrab.hatchToggle == True:
                subsystems.hatchgrab.HatchClose()
            else:
                subsystems.hatchgrab.HatchOpen()

    def isFinished(self):
        return True