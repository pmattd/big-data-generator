import uuid
from dataclasses import dataclass
from random import randint


class ValueGenerator:
    def getVal(self):
        raise NotImplementedError("this is an interface use a subclass")


@dataclass()
class EnumeratedFieldGenerator(ValueGenerator):
    values: []

    def getVal(self):
        numvalues = len(self.values)
        index = randint(0, numvalues - 1)
        return self.values[index]


@dataclass()
class RandomValueFieldGenerator(ValueGenerator):
    min: int
    max: int

    def getVal(self):
        return str(randint(self.min, self.max))


@dataclass()
class IdentityFieldGenerator(ValueGenerator):
    def getVal(self):
        return str(uuid.uuid4())


class DataLineGenerator:

    def __init__(self, generators: [ValueGenerator] = None, separator=" "):
        if generators is None:
            generators = []
        self.generators = generators
        self.separator = separator

    def generate(self):
        values = []

        for generator in self.generators:
            values.append(generator.getVal())

        return self.separator.join(values)
