import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation

# import items in the order they should be initialized to avoid any surprises
import robotmap
import subsystems
import oi

#autoManager = None


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        print('Robot Base - robotInit called')

        # subsystems must be initialized before things that use them
        # ensure order of operations is correct, just like importing to avoid issues with dependencies
        subsystems.init()
        oi.init()

        #if robotmap.sensors.hasAHRS:
        #    try:
        #        robotmap.sensors.ahrs = navx.AHRS.create_spi()
        #        # use via robotmap.sensors.ahrs.getAngle() or getYaw()
        #        print('robotInit: NavX Setup')
        #    except:
        #        if not DriverStation.getInstance().isFmsAttached():
        #            raise

        print('robotInit: Starting Camera Server')
        try:
            wpilib.CameraServer.launch()
            print('robotInit: Camera Rolling')
        except Exception as e:
            print('robotInit: Error! Exception caught starting cameraServer: {}'.format(e))

    def autonomousInit(self):
        super().autonomousInit()

    def autonomousPeriodic(self):
        super().autonomousPeriodic()
        SmartDashboard.putNumber("Front IR", subsystems.drivelift.frontIR.getVoltage())
        SmartDashboard.putNumber("Back IR", subsystems.drivelift.backIR.getVoltage())
        SmartDashboard.putNumber("Elevator Height", subsystems.elevator.elevatorHeight)
        # optionally do stuff like display data to smart dashboard here while in autonomous

    def teleopPeriodic(self):
        Scheduler.getInstance().run()
        SmartDashboard.putNumber("Front IR", subsystems.drivelift.frontIR.getVoltage())
        SmartDashboard.putNumber("Back IR", subsystems.drivelift.backIR.getVoltage())
        SmartDashboard.putNumber("Elevator Height", subsystems.elevator.elevatorHeight)
        #optionally do stuff like display data to smart dashboard here while in teleop

    def disabledPeriodic(self):
        Scheduler.getInstance().run()
        SmartDashboard.putNumber("Front IR", subsystems.drivelift.frontIR.getVoltage())
        SmartDashboard.putNumber("Back IR", subsystems.drivelift.backIR.getVoltage())
        SmartDashboard.putNumber("Elevator Height", subsystems.elevator.elevatorHeight)
        # optionally do stuff like display data to smart dashboard here while in disabled

    def testPeriodic(self):
        wpilib.LiveWindow.run()
        # optionally do stuff like display data to smart dashboard here while in test


if __name__ == '__main__':
    wpilib.run(MyRobot)

