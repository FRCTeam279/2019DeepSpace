from wpilib.command import Command
import robotmap
import subsystems
import oi

class AllSolLiftSystem(Command):

    def __init__(self):
            super().__init__('AllSolLiftSystem')
            self.requires(subsystems.tanklift)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        if subsystems.tanklift.allSolToggle == True:
            subsystems.tanklift.extendAll()
        else:
            subsystems.ramp.retractAll()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True