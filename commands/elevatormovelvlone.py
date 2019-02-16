from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorMoveLvlOne(Command):
    def __init__(self):
            super().__init__('ElevatorMoveLvlOne')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevator.elevatorMoveLvlOne()

    def isFinished(self):
        return True