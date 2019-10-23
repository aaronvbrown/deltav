
# GOAL:  Design Class to store rocket stages using engines


class Propulsion:
    # creates a member of the Propulsion family
    def __init__(self, name, type, thrust, mass, isp, fuel, oxydizer, cost):
        self._name = name
        self.type = type
        self.thrust = thrust                    # to do: units
        self.mass = mass                        # to do: units
        self.isp = isp                          # to do: units
        self.fuel = fuel
        self.oxydizer = oxydizer
        self.cost = cost

    def thrust_to_mass(self):
        return self.thrust / self.mass


merlin_1d = Propulsion("Merlin 1d", "Liquid", 981, 50, 320,"kerosene", "lox",1000000)


print(merlin_1d.thrust_to_mass())


class Body:
    # creates a member of the Body family
    def __init__(self, material, mass, diameter, length):
        self.material = material
        self.mass = mass
        self.diameter = diameter
        self.height = length


aluminum = Body("Aluminum", 100, 4, 60)


class VehicleStage:
    # creates a mamber of the vehicle family (for a single stage)
    # ToDo:  add stage number with zero being the top stage.  add methods to build entire vehicle up to zero.
    def __init__(self, name: str, body_type, propulsion_type, propulsion_count=0, fuel_cap=0, oxydizer_cap=0):
        self._name = name
        self.propulsion_type = propulsion_type
        self.propulsion_count = propulsion_count
        self.fuel_cap = fuel_cap                # to do: units
        self.oxydizer_cap = oxydizer_cap        # to do: units

    def thrust(self):
        return self.propulsion_type.thrust * self.propulsion_count    
        
    def mass_propulsion(self):
        return self.propulsion_type.mass * self.propulsion_count
        # ToDo:  teach this method to calculate dry mass of the stage
    
    def mass_dry(self):
        return self.body_type.mass + self.mass_propulsion

    def mass_wet(self, stage_mass_dry, fuel_cap, oxydizer_cap):
        # ToDo: teach this method to add the fuel and oxy mass to dry mass
        pass


falcon_9 = VehicleStage("Falcon 9", aluminum, merlin_1d, 9,300000,700000)
print(falcon_9.thrust())
print(falcon_9.mass_propulsion())
help(falcon_9)
print(falcon_9.mass_dry())


# Inheritance
class Reusable(VehicleStage):

    """
    Create a Vehicle that is a Reusable, meaning that it must be able to bring its dry weight back
    """
    def __init__(self, name: str, enginecountb, thrust, weight, isp, fuel_cap, oxy_cap, weight_dry, return_method):
        super().__init__(name, enginecountb, thrust, weight, isp, fuel_cap, oxy_cap)
        self.return_method = return_method

    def brag(self):
        return f"{self._name} says 'Hi!  I can return to earth after launching using {self.return_method}!"

