from wpilib.command import Command
import robotmap
import subsystems
import oi

class RampTeleopDefault(Command):

    def __init__(self):
            super().__init__('RampTeleopDefault')
            self.requires(subsystems.ramp)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        if subsystems.ramp.rampToggle == True:
            subsystems.ramp.extendRamp()
        else:
            subsystems.ramp.retractRamp()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True