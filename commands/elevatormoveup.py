import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorMoveUp(Command):

    def __init__(self):
            super().__init__('ElevatorMoveUp')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevator.elevatorMoveUp()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
