from wpilib.command import Command
import robotmap
import subsystems
import oi

class RampToggleTrigger(Command):

    def __init__(self):
            super().__init__('RampToggleTrigger')
            self.requires(subsystems.ramp)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.ramp.rampTogFunction()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True