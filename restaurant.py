class Restaurant():
    """mantendo boas práticas: modela um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        """define dados do restaurante"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """descreve o restaurante"""
        message = (f"The restaurant name is {self.restaurant_name.title()}. "
        f"It's cuisine type is {self.cuisine_type}.")
        print(message)

    def open_restaurant(self):
        """simula abertura do restaurante"""
        print(f"{self.restaurant_name.title()} is now open.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print("Não.")