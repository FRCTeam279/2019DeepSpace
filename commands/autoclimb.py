from wpilib.command import CommandGroup, PrintCommand, WaitCommand
import subsystems
import commands
from commands.driveraw import DriveRaw
from commands.retractback import RetractBack
from commands.extendback import ExtendBack
from commands.extendfront import ExtendFront
from commands.retractfront import RetractFront

class AutoClimb(CommandGroup):

    def __init__(self):
            super().__init__('AutoClimb')
            self.setInterruptible(True)
            self.setRunWhenDisabled(True)

            self.addSequential(PrintCommand("Starting Climb"))

            self.addSequential(ExtendBack())    
            self.addSequential(WaitCommand(0.5))

            self.addSequential(DriveRaw(-.25,-.25, 1))  
            self.addSequential(WaitCommand(1))
            
            self.addSequential(ExtendFront())    
            self.addSequential(WaitCommand(0.5))
            
            self.addSequential(RetractBack())    
            self.addSequential(WaitCommand(1))

            self.addSequential(DriveRaw(-.25,-.25, 1))    
            self.addSequential(WaitCommand(1))

            self.addSequential(RetractFront())    
            self.addSequential(WaitCommand(1))

            self.addSequential(DriveRaw(-.25,-.25, 1))    
            self.addSequential(WaitCommand(1))

            self.addSequential(PrintCommand("Finished Test"))