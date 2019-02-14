from wpilib.command import CommandGroup, PrintCommand, WaitCommand
from subsystems

class AutoClimb(CommandGroup):

    def __init__(self):
            super().__init__('AutoClimb')
            self.setInterruptible(True)
            self.setRunWhenDisabled(True)

            self.addSequential(PrintCommand("Starting Climb"))

            self.addSequential(subsystems.drivelift.extendFront())    
            self.addSequential(WaitCommand(3))

            self.addSequential(subsystems.driveline.driveRaw())    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("3"))    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("4"))    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("Finished Test"))