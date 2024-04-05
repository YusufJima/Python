def CalculateMachNumber(Speedms):
    SpeedofSound = 343
    MachNumber = Speedms / SpeedofSound
    return MachNumber


def Clasificationofmachnumber(MachNumber):
    if MachNumber >= 10 and MachNumber <= 25:
        return "High Hypersonic"
    elif MachNumber >= 5 and MachNumber < 10:
        return "Hypersonic"
    elif MachNumber >= 1.2 and MachNumber < 5:
        return "Supersonic"
    elif MachNumber >= 0.8 and MachNumber < 1.2:
        return "Transonic"
    else:
        return "Subsonic"


Speedms = float(
    input("Enter the speed of the aircraft in meters per second (m/s): "))
MachNumber = CalculateMachNumber(Speedms)
Clasificacion = Clasificationofmachnumber(MachNumber)
message = f""" 
The Mach number is: {round(MachNumber,2)}
The Clasification is: {Clasificacion} """
print(message)
