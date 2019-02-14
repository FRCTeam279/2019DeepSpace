import math

from wpilib.command import CommandGroup, PrintCommand
import robotmap
import subsystems
import oi
from commands.extendfront import ExtendFront
from commands.extendback import ExtendBack
from commands.retractfront import RetractFront
from commands.retractback import RetractBack
from commands.driveraw import DriveRaw

"""
class ClimbAutomatic(CommandGroup):


    def __init__(self):
            super().__init__('ClimbAutomatic')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)
            #if oi.joystick.button.get() #we dont have a button configured yet
                self.addSequential(PrintCommand("CMD Group ClimbAutomatic: Extending Front Cylinders")
                self.addSequential(ExtendFront(), timeout = 2.5) #dont drive forward until fully extended
                
                self.addSequential(PrintCom(mand("CMD Group ClimbAutomatic: Drive Forward")
                self.addSequential(DriveRaw(0.5, 0.5), timeout = 1.5)
                #needs to stop when front sensor is triggered

                self.addSequential(PrintCommand("CMD Group ClimbAutomatic: Extend Back"))
                self.addSequential(ExtendBack(), timeout = 2.5)

                self.addSequential(PrintCommand("CMD Group ClimbAutomatic: Retract Front and drive forward"))
                self.addParallel(RetractFront(), timeout = 1.5)
                self.addParallel(DriveRaw(0.2, 0.2), timeout = 1.5) #this may be bad if its still retracting
"""



