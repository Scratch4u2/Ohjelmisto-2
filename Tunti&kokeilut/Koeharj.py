from flask import Flask, jsonify
import json

app = Flask(__name__)


class Engine():
    def __init__(self, model, type="Gasoline"):
        self.model = model
        self.type = type
    def print_info(self):
        print(self.model, self.type)


class Car(Engine):
    car_count = 0

    def __init__(self, price, make, year, engine):
        super().__init__(engine.model, engine.type)
        self.price = price
        self.make = make
        self.year = year
        self.engine = engine
        Car.car_count += 1

    def print_info(self):
        super().print_info()
        print("Car details:", self.price, self.make, self.year, "Engine details:", self.engine.model, self.engine.type)

engine1 = Engine("123", "Electric")
auto3 = Car(1000, "Ford", "2019",engine1)
auto3.print_info()


@app.route('/luokka/<car_name>')
def info_auto(car_name):
    if car_name == 'auto1':
        auto = Car("30000", "Toyota", 2019, Engine("123"))
    elif car_name == 'auto2':
        auto = Car("50000", "Lexus", 2024, Engine("456", "Electric"))
    else:
        return "Invalid car name"

    auto_data = {
        "price": auto.price,
        "make": auto.make,
        "year": auto.year,
        "engine": {
            "model": auto.engine.model,
            "type": auto.engine.type
        }
    }
    return jsonify(auto_data)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
