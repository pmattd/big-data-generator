import uuid
from dataclasses import dataclass
from random import randint


@dataclass()
class EnumeratedFieldGenerator:
    values: []

    def get_val(self):
        numvalues = len(self.values)
        index = randint(0, numvalues - 1)
        return self.values[index]


@dataclass()
class RandomValueFieldGenerator:
    min: int
    max: int

    def get_val(self):
        return str(randint(self.min, self.max))


@dataclass()
class IdentityFieldGenerator:
    def get_val(self):
        return str(uuid.uuid4())


class DataLineGenerator:

    def __init__(self, generators=None, separator=" "):
        if generators is None:
            generators = []
        self.generators = generators
        self.separator = separator

    def generate(self):
        values = []

        for generator in self.generators:
            values.append(generator.get_val())

        return self.separator.join(values)
