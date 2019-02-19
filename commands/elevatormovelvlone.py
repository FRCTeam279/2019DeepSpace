from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorMoveHatchHeight(Command):
    def __init__(self):
            super().__init__('ElevatorMoveHatchHeight')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevator.elevatorMoveHatchHeight()

    def isFinished(self):
        return True