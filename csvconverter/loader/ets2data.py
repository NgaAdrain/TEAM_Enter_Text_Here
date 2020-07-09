class Ets2Data:
    def __init__(self, info):
        self.timestamp = info.timestamp + '_' + str(info.inGameTime)
        self.drivetrain = Drivetrain(info.drivetrain)
        self.physics = Physics(info.physics)
        self.controls = Controls(info.controls)
        self.lights = Lights(info.lights)

    def __str__(self):
        substr = self.timestamp + ', '
        substr += str(self.drivetrain) + ', '
        substr += str(self.physics) + ', '
        substr += str(self.controls) + ', '
        substr += str(self.lights) + ', '
        return substr

    def print(self):
        substr = 'Timestamp : ' + str(self.timestamp) + '\n'
        # substr += 'Ingame time : ' + str(self.inGameTime) + '\n'
        print(substr)
        self.drivetrain.print()
        self.physics.print()
        self.controls.print()
        self.lights.print()


class Drivetrain:
    def __init__(self, drt):
        self.truckOdometer = drt.TruckOdometer
        self.gearDashboard = drt.GearDashboard
        self.engineRpm = drt.EngineRpm
        self.fuel = drt.Fuel
        self.fuelAvgConsumption = drt.FuelAvgConsumption

    def __str__(self):
        substr = str(self.truckOdometer) + ', '
        substr += str(self.gearDashboard) + ', '
        substr += str(self.engineRpm) + ', '
        substr += str(self.fuel) + ', '
        substr += str(self.fuelAvgConsumption)
        return substr

    def print(self):
        substr = '\t + Drivetrain information' + '\n'
        substr += '\t\t- Drivetrain.TruckOdometer : ' + str(self.truckOdometer) + '\n'
        substr += '\t\t- Drivetrain.GearDashboard : ' + str(self.gearDashboard) + '\n'
        substr += '\t\t- Drivetrain.EngineRpm : ' + str(self.engineRpm) + '\n'
        substr += '\t\t- Drivetrain.Fuel : ' + str(self.fuel) + '\n'
        substr += '\t\t- Drivetrain.FuelAvgConsumption : ' + str(self.fuelAvgConsumption) + '\n'
        print(substr)

class Physics:
    def __init__(self, phy):
        self.speedKmh = phy.SpeedKmh
        self.acceleration = [phy.AccelerationX, phy.AccelerationY, phy.AccelerationZ]
        self.coordinate = [phy.CoordinateX, phy.CoordinateY, phy.CoordinateZ]
        self.rotation = [phy.RotationX, phy.RotationY, phy.RotationZ]

    def __str__(self):
        substr = str(self.speedKmh) + ', '
        substr += str(self.acceleration[0]) + ', '
        substr += str(self.acceleration[1]) + ', '
        substr += str(self.acceleration[2]) + ', '
        substr += str(self.coordinate[0]) + ', '
        substr += str(self.coordinate[1]) + ', '
        substr += str(self.coordinate[2]) + ', '
        substr += str(self.rotation[0]) + ', '
        substr += str(self.rotation[1]) + ', '
        substr += str(self.rotation[2])
        return substr

    def print(self):
        substr = '\t + Physics information' + '\n'
        substr += '\t\t- Physics.SpeedKmh : ' + str(self.speedKmh) + '\n'
        substr += '\t\t- Physics.Acceleration : ' + str(self.acceleration) + '\n'
        substr += '\t\t- Physics.Coordinate : ' + str(self.coordinate) + '\n'
        substr += '\t\t- Physics.Rotation : ' + str(self.rotation) + '\n'
        print(substr)

class Controls:
    def __init__(self, ctrl):
        self.userSteer = ctrl.UserSteer
        self.userThrottle = ctrl.UserThrottle
        self.userBrake = ctrl.UserBrake
        self.userClutch = ctrl.UserClutch

    def __str__(self):
        substr = str(self.userSteer) + ', '
        substr += str(self.userThrottle) + ', '
        substr += str(self.userBrake)
        substr += str(self.userBrake) + ', '
        substr += str(self.userClutch)
        return substr

    def print(self):
        substr = '\t + Controls information' + '\n'
        substr += '\t\t- Controls.UserSteer : ' + str(self.userSteer) + '\n'
        substr += '\t\t- Controls.UserThrottle : ' + str(self.userThrottle) + '\n'
        substr += '\t\t- Controls.UserBrake : ' + str(self.userBrake) + '\n'
        substr += '\t\t- Controls.UserClutch : ' + self.userClutch + '\n'
        print(substr)

class Lights:
    def __init__(self, lig):
        self.left = lig.BlinkerLeftOn
        self.right = lig.BlinkerRightOn

    def __str__(self):
        substr = str(self.left) + ', '
        substr += str(self.right)
        return substr

    def print(self):
        substr = '\t + Lights information..' + '\n'
        substr += '\t\t- Lights.BlinkerLeftOn : ' + str(self.left) + '\n'
        substr += '\t\t- Lights.BlinkerRightOn : ' + str(self.right) + '\n'
        print(substr)