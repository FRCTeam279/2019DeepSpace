from wpilib.command import Command
import robotmap
import subsystems
import oi

class ExtendBack(Command):

    def __init__(self):
            super().__init__('ExtendBack')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.drivelift.extendBack()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
