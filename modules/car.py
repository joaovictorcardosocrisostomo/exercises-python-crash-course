"""uma classe que representa um carro."""

class Car():
    """modelando um carro"""
    def __init__(self, make, model, year):
        """inicializa os atributos"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #recebendo um valor padrão
        #não precisa incluir parâmetro, é um atributo que deve começar com um
        #valor determinado e pode ser incrementado depois com outro método
    
    def get_descriptive_name(self):
        """apresenta o carro"""
        long_name = (f"{self.make} {self.model} {str(self.year)}")
        #fstrings não servem só pra função print.
        return(long_name.title())

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor
especificado. Rejeita a alteração se for tentativa de definir um valor menor
para o hodômetro"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode fazer isso.")

    def increment_odometer(self, increment):
        if increment >= 0:
            """Soma a quantidade especificada ao valor de leitura do
hodômetro."""
            self.odometer_reading += increment
        else:
            print("Não.")

    def read_odometer(self):
        """apresenta a kilometragem/milhagem do carro"""
        print(f"este carro já rodou {self.odometer_reading}")
    def fill_gas_tank(self):
        print("Tanque cheio.")