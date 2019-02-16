from wpilib.command import Command
import robotmap
import subsystems
import oi

class RampExtend(Command):

    def __init__(self):
            super().__init__('RampExtend')
            self.requires(subsystems.ramp)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.ramp.extendRamp()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
