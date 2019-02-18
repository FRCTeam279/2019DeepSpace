from wpilib.command import Command
import robotmap
import subsystems
import oi

class HatchToggleTrigger(Command):

    def __init__(self):
            super().__init__('HatchoggleTrigger')
            self.requires(subsystems.hatchgrab)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.hatchgrab.hatchTogFunction()
        
    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True