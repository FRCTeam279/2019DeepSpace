import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorMoveDown(Command):

    def __init__(self):
            super().__init__('ElevatorMoveDown')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevator.elevatorMoveDown()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
