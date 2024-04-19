from flask import Flask, Response, jsonify

app = Flask(__name__)


class Animal:  # Capitalized class name
    def __init__(self, species, size, latin_name):
        self.species = species
        self.size = size
        self.latin_name = latin_name

    def to_dict(self):
        return {
            "species": self.species,
            "size": self.size,
            "latin_name": self.latin_name
        }


class Otter(Animal):  # Inherits from Animal
    def __init__(self, species, size, latin_name):
        super().__init__(species, size, latin_name)


class Lynx(Animal):
    def __init__(self, species, size, latin_name, fur_type="dense"):
        super().__init__(species, size, latin_name)
        self.fur_type = fur_type

    def to_dict(self):
        lynx_dict = super().to_dict()
        lynx_dict["fur_type"] = self.fur_type
        return lynx_dict


# Routes
@app.route("/animal/<species>/<size>/<latin_name>")
def animal_info(species, size, latin_name):
    animal = Animal(species, size, latin_name)
    return jsonify(animal.to_dict())


@app.route("/otter/<species>/<size>/<latin_name>")
def otter_info(species, size, latin_name):
    otter = Otter(species, size, latin_name)
    return jsonify(otter.to_dict())


@app.route("/lynx/<species>/<size>/<latin_name>/<fur_type>")
def lynx_info(species, size, latin_name, fur_type):
    lynx = Lynx(species, size, latin_name, fur_type)
    return jsonify(lynx.to_dict())


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
