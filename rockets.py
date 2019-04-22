#! python3

class Vehicle:
    #creates a mamber of the vehicle family
    def __init__(self, name: str, thrust, weight, isp, fuel_cap):
        self._name = name
        self.thrust = thrust
        self.weight = weight
        self.isp = isp
        self.fuel_cap = fuel_cap
        self.oxy_cap
