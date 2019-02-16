from wpilib.command import Command
import robotmap
import subsystems
import oi

class ExtendAll(Command):

    def __init__(self):
            super().__init__('ExtendAll')
            self.requires(subsystems.drivelift)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.drivelift.extendAll()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
