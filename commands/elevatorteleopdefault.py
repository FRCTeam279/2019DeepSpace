import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorTeleopDefault(Command):

    def __init__(self):
            super().__init__('ElevatorTeleopDefault')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        speed = -(oi.goGamePad.getRawAxis(oi.config.axisElevatorIndex))
        speed = oi.filterInput(speed, robotmap.elevator.elevatorDeadZone)
        subsystems.elevator.move(speed)

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False

    def interrupted(self):
        subsystems.elevator.stopElevator()
