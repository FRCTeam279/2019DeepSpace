from wpilib.command import Command
import robotmap
import subsystems
import oi

class ExtendFront(Command):

    def __init__(self):
            super().__init__('ExtendFront')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.drivelift.extendFront()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
