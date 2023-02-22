def Fuel_required(mass):
    """Calculates and returns the amount of fuel required based on the mass"""
    fuel = mass // 3
    return fuel -2


def Total_fuel_required(mass):
    """Returns the sum of fuel required based on the given fuel mass"""
    return sum(Fuel_required(x) for x in mass)

if __name__ == '__main__':
    with open("input") as file:
        data = file.read()
        data = data.splitlines()
        data_list = list(map(int, data))
    print(Total_fuel_required(data_list))
