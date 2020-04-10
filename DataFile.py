from dataclasses import dataclass
from random import randint


@dataclass()
class EnumeratedFieldGenerator:
    values: []

    def getVal(self):
        numvalues = len(self.values)
        index = randint(0, numvalues - 1)
        return self.values[index]


@dataclass()
class RandomValueFieldGenerator:
    min: int
    max: int

    def getVal(self):
        return str(randint(self.min, self.max))


class DataLineGenerator:

    def __init__(self, generators=None, separator=" "):
        if generators is None:
            generators = []
        self.generators = generators
        self.separator = separator

    def generate(self):
        values = []

        for generator in self.generators:
            values.append(generator.getVal())

        return self.separator.join(values)
