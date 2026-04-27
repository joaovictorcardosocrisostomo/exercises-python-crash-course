from car import Car

class Battery():
  def __init__(self, battery_size=70):
    """Modelando uma bateria de carro"""
    self.battery_size = battery_size

  def describe_battery(self):
        """Capacidade da bateria"""
        print(f"Capacidade da bateria: {self.battery_size}.")

  def get_range(self):
    """Exibe uma frase sobre a distância que o carro é capaz de
percorrer com essa bateria."""
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270
      
    message = "This car can go approximately " + str(range)
    message += " miles on a full charge."
    print(message)

  def upgrade_battery(self):
    if self.battery_size < 85:
      self.battery_size = 85
    else:
      print("A bateria já é de 85 ou maior.")


class ElectricCar(Car):
  """Representa aspectos específicos de veículos elétricos."""
  def __init__(self, make, model, year):
      """Inicializa atributos da classe pai
      Em seguida, inicializa os atributos
      específicos de um carro elétrico"""
      super().__init__(make, model, year)
      self.battery = Battery()
  
  def fill_gas_tank():
      """Carros elétricos não têm tanques de gasolina."""
      print("This car doesn't need a gas tank!")