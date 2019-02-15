from wpilib.command import CommandGroup, PrintCommand, WaitCommand
import subsystems

class AutoClimb(CommandGroup):

    def __init__(self):
            super().__init__('AutoClimb')
            self.setInterruptible(True)
            self.setRunWhenDisabled(True)

            self.addSequential(PrintCommand("Starting Climb"))

            self.addSequential(subsystems.drivelift.extendBack())    
            self.addSequential(WaitCommand(6))

            self.addSequential(subsystems.driveline.driveRaw(-.1,-.1))    
            self.addSequential(WaitCommand(2))
            
            self.addSequential(subsystems.drivelift.extendFront())    
            self.addSequential(WaitCommand(6))
            
            self.addSequential(subsystems.drivelift.retractBack())    
            self.addSequential(WaitCommand(2))

            self.addSequential(subsystems.driveline.driveRaw(-.1,-.1))    
            self.addSequential(WaitCommand(2))

            self.addSequential(subsystems.drivelift.retractFront())    
            self.addSequential(WaitCommand(2))

            self.addSequential(subsystems.driveline.driveRaw(-.1,-.1))    
            self.addSequential(WaitCommand(2))

            self.addSequential(PrintCommand("Finished Test"))