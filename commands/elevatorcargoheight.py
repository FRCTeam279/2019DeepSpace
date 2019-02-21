from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorCargoHeight(Command):
    def __init__(self):
            super().__init__('ElevatorCargoHeight')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevator.elevatorCargoHeight()

    def isFinished(self):
        return True