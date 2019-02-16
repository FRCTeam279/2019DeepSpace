from wpilib.command import Command
import robotmap
import subsystems
import oi

class TankLiftTeleopDefault(Command):

    def __init__(self):
            super().__init__('TankLiftTeleopDefault')
            self.requires(subsystems.drivelift)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.drivelift.retractFront()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False