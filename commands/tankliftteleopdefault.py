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
        #if subsystems.drivelift.allLiftToggle == True:
        #    subsystems.drivelift.extendAll()
        #else:
        #    subsystems.drivelift.retractAll()

        #^We never want to extend all, so this needs to cahnge^

        #if subsystems.drivelift.frontLiftToggle == True:
        #    subsystems.drivelift.extendFront()
        #else:
        #    subsystems.drivelift.retractFront()

        #if subsystems.drivelift.cackLiftToggle == True:
        #    subsystems.drivelift.extendBack()
        #else:
        #    subsystems.drivelift.retractBack()
        
        subsystems.drivelift.retractAll()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False