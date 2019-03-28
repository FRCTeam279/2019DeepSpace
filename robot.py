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
        
        #Tanklift data
        SmartDashboard.putBoolean("Front IR", subsystems.drivelift.frontIR.state)
        SmartDashboard.putBoolean("Back IR", subsystems.drivelift.backIR.state)

        #Elevator Data
        SmartDashboard.putNumber("Elevator Ticks", subsystems.elevator.elevatorEncoder.get())
        SmartDashboard.putNumber("Elevator Height", subsystems.elevator.elevatorEncoder.getDistance())

        #Game Objective States
        SmartDashboard.putBoolean("Ramp Tog State", subsystems.ramp.rampToggle)
        SmartDashboard.putBoolean("Hatch Tog State", subsystems.hatchgrab.hatchToggle)
        SmartDashboard.putBoolean("Hatch Extend Tog", subsystems.hatchgrab.hatchExtendToggle)      
        SmartDashboard.putBoolean("Cargo Tog State", subsystems.cargograb.cargoToggle)
        SmartDashboard.putNumber("R Servo Angle", subsystems.cargograb.rightServo.getAngle())
        SmartDashboard.putNumber("L Servo Angle", subsystems.cargograb.leftServo.getAngle())

        #Driveline data
        SmartDashboard.putNumber("Left Speed", subsystems.driveline.leftSpdCtrl.get())
        SmartDashboard.putNumber("Right Speed", subsystems.driveline.rightSpdCtrl.get())
        SmartDashboard.putNumber("Speed Dif", subsystems.driveline.spdDif)

        SmartDashboard.putNumber("Right Sensors", subsystems.driveline.rSensor.getVoltage())
        SmartDashboard.putNumber("Left Sensors", subsystems.driveline.lSensor.getVoltage())
        SmartDashboard.putNumber("Sensor Dif", subsystems.driveline.lineSensorCompare)

    def teleopPeriodic(self):
        Scheduler.getInstance().run()

        #Tanklift data
        SmartDashboard.putBoolean("Front IR", subsystems.drivelift.frontIR.state)
        SmartDashboard.putBoolean("Back IR", subsystems.drivelift.backIR.state)

        #Elevator Data
        SmartDashboard.putNumber("Elevator Ticks", subsystems.elevator.elevatorEncoder.get())
        SmartDashboard.putNumber("Elevator Height", subsystems.elevator.elevatorEncoder.getDistance())

        #Game Objective States
        SmartDashboard.putBoolean("Ramp Tog State", subsystems.ramp.rampToggle)
        SmartDashboard.putBoolean("Hatch Tog State", subsystems.hatchgrab.hatchToggle)
        SmartDashboard.putBoolean("Hatch Extend Tog", subsystems.hatchgrab.hatchExtendToggle)
        SmartDashboard.putBoolean("Cargo Tog State", subsystems.cargograb.cargoToggle)
        SmartDashboard.putNumber("R Servo Angle", subsystems.cargograb.rightServo.getAngle())
        SmartDashboard.putNumber("L Servo Angle", subsystems.cargograb.leftServo.getAngle())

        #Driveline data
        SmartDashboard.putNumber("Left Speed", subsystems.driveline.leftSpdCtrl.get())
        SmartDashboard.putNumber("Right Speed", subsystems.driveline.rightSpdCtrl.get())
        SmartDashboard.putNumber("Speed Dif", subsystems.driveline.spdDif)

        SmartDashboard.putNumber("Right Sensors", subsystems.driveline.rSensor.getVoltage())
        SmartDashboard.putNumber("Left Sensors", subsystems.driveline.lSensor.getVoltage())
        SmartDashboard.putNumber("Sensor Dif", subsystems.driveline.lineSensorCompare)

    def disabledPeriodic(self):
        Scheduler.getInstance().run()

        #Tanklift data
        SmartDashboard.putBoolean("Front IR", subsystems.drivelift.frontIR.state)
        SmartDashboard.putBoolean("Back IR", subsystems.drivelift.backIR.state)

        #Elevator Data
        SmartDashboard.putNumber("Elevator Ticks", subsystems.elevator.elevatorEncoder.get())
        SmartDashboard.putNumber("Elevator Height", subsystems.elevator.elevatorEncoder.getDistance())

        #Game Objective States
        SmartDashboard.putBoolean("Ramp Tog State", subsystems.ramp.rampToggle)
        SmartDashboard.putBoolean("Hatch Tog State", subsystems.hatchgrab.hatchToggle)
        SmartDashboard.putBoolean("Hatch Extend Tog", subsystems.hatchgrab.hatchExtendToggle)
        SmartDashboard.putBoolean("Cargo Tog State", subsystems.cargograb.cargoToggle)
        SmartDashboard.putNumber("R Servo Angle", subsystems.cargograb.rightServo.getAngle())
        SmartDashboard.putNumber("L Servo Angle", subsystems.cargograb.leftServo.getAngle())

        #Driveline data
        SmartDashboard.putNumber("Left Speed", subsystems.driveline.leftSpdCtrl.get())
        SmartDashboard.putNumber("Right Speed", subsystems.driveline.rightSpdCtrl.get())
        SmartDashboard.putNumber("Speed Dif", subsystems.driveline.spdDif)

        SmartDashboard.putNumber("Right Sensors", subsystems.driveline.rSensor.getVoltage())
        SmartDashboard.putNumber("Left Sensors", subsystems.driveline.lSensor.getVoltage())
        SmartDashboard.putNumber("Sensor Dif", subsystems.driveline.lineSensorCompare)

    def testPeriodic(self):
        wpilib.LiveWindow.run()
        # optionally do stuff like display data to smart dashboard here while in test


if __name__ == '__main__':
    wpilib.run(MyRobot)

