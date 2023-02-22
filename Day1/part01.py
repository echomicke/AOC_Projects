def Fuel_required(mass):
    """Calculates and returns the amount of fuel required based on the mass"""
    fuel = mass // 3
    return fuel -2


def Total_fuel_required(mass):
    """Returns the sum of fuel required based on the given fuel mass"""
    return sum(Fuel_required(x) for x in mass)
