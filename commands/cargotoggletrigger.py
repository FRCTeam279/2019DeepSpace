from wpilib.command import Command
import robotmap
import subsystems
import oi

class CargoToggleTrigger(Command):

    def __init__(self):
            super().__init__('CargoToggleTrigger')
            self.requires(subsystems.cargograb)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        #subsystems.cargograb.cargoTogFunction()
        pass
        
    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True