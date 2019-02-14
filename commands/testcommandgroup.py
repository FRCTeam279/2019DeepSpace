from wpilib.command import CommandGroup, PrintCommand, WaitCommand

class TestCommandGroup(CommandGroup):

    def __init__(self):
            super().__init__('TestCommandGroup')
            self.setInterruptible(True)
            self.setRunWhenDisabled(True)

            self.addSequential(PrintCommand("Starting Test"))

            self.addSequential(PrintCommand("1"))    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("2"))    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("3"))    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("4"))    
            self.addSequential(WaitCommand(3))

            self.addSequential(PrintCommand("Finished Test"))