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
        if subsystems.hatchgrab.hatchToggle == True:
            subsystems.hatchgrab.HatchClose()
        else:
            subsystems.hatchgrab.HatchOpen()

    def isFinished(self):
        return True