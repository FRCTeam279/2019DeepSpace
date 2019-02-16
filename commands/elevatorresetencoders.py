import time
import math

from wpilib import SmartDashboard
from wpilib.command import Command

import robotmap
import subsystems


class ElevatorResetEncoders(Command):

    def __init__(self):
        super().__init__('ElevatorResetEncoders')
        self.requires(subsystems.elevator)
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevator.resetEncoders(self)
        print("CMD ElevatorResetEncoders: Reset Completed")

    def isFinished(self):
       return True

