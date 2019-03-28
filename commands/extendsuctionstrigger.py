from wpilib.command import Command
import robotmap
import subsystems
import oi

class ExtendSuctionsTrigger(Command):

    def __init__(self):
            super().__init__('ExtendSuctionsTrigger')
            self.requires(subsystems.hatchgrab)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.hatchgrab.hatchExtendTogFunction()
        
    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True