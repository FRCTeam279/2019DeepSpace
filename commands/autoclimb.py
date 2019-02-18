from wpilib.command import CommandGroup, PrintCommand, WaitCommand
import subsystems
import commands
from commands.driveraw import DriveRaw
from commands.retractback import RetractBack
from commands.extendback import ExtendBack
from commands.extendfront import ExtendFront
from commands.retractall import RetractAll   # used to be retractfront

class AutoClimb(CommandGroup):
    climbSpd = .4
    def __init__(self):
            super().__init__('AutoClimb')
            self.setInterruptible(True)
            self.setRunWhenDisabled(True)
            
            self.addSequential(PrintCommand("Starting Climb"))

            self.addSequential(ExtendBack())    
            self.addSequential(WaitCommand(0.5))  # time-to-run = .5 sec

            self.addSequential(DriveRaw(-self.climbSpd,-self.climbSpd, 1))  
            self.addSequential(WaitCommand(1))    # time-to-run = 1.0 sec
                
            self.addSequential(ExtendFront())    
            self.addSequential(WaitCommand(0.5))  # time-to-run = .5 sec
            
            self.addSequential(RetractBack())    
            self.addSequential(WaitCommand(2))   

            self.addSequential(DriveRaw(-self.climbSpd,-self.climbSpd, 1))    
            self.addSequential(WaitCommand(1.2))

            self.addSequential(RetractAll())    
            self.addSequential(WaitCommand(1.5))

            self.addSequential(DriveRaw(-self.climbSpd,-self.climbSpd, 2))    
            self.addSequential(WaitCommand(1))

            self.addSequential(PrintCommand("Finished Test"))
            