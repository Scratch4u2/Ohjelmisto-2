class Engine():
    def __init__(self, model, type="Gasoline"):
        # Initialize the Engine object with a model and type (defaulting to "Gasoline")
        self.model = model
        self.type = type

    def print_info(self):
        # Print the model and type of the Engine
        print(self.model, self.type)


class Car(Engine):
    car_count = 0

    def __init__(self, price, make, year, engine):
        # Call the __init__ method of the parent class (Engine) to initialize the engine's model and type
        super().__init__(engine.model, engine.type)

        # Initialize Car-specific attributes: price, make, year, and engine
        self.price = price
        self.make = make
        self.year = year
        self.engine = engine  # Store the Engine object associated with the Car
        Car.car_count += 1

    def print_info(self):
        # Call the print_info method of the parent class (Engine) to print engine details
        super().print_info()

        # Print Car-specific attributes: price, make, and year
        print("Car details:", self.price, self.make, self.year, "Engine details:", self.engine.model, self.engine.type)

        # Print engine details
        # print("Engine details:", self.engine.model, self.engine.type)


# Create an Engine object
bensiini1 = Engine("123")
# Print information about the Engine
#bensiini1.print_info()

# Create another Engine object
sahko = Engine("456", "Electric")
#sahko.print_info()

# Create a Car object and associate it with the first Engine object
auto1 = Car("30000", "Toyota", 2019, bensiini1)
# Print information about the Car, including Engine details
auto1.print_info()

auto2 = Car("50000", "Lexus", 2024, sahko)
auto2.print_info()

print(Car.car_count)
