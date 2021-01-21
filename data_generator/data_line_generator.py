import time
import uuid
from dataclasses import dataclass
from datetime import datetime
from random import randint, seed


@dataclass()
class ValueGenerator:
    name: str

    def get_name(self):
        return self.name

    def get_val(self):
        raise NotImplementedError("this is an interface use a subclass")


@dataclass()
class EnumeratedFieldGenerator(ValueGenerator):
    values: []

    def get_val(self):
        numvalues = len(self.values)
        index = randint(0, numvalues - 1)
        return self.values[index]


@dataclass()
class RandomValueFieldGenerator(ValueGenerator):
    min: int
    max: int

    def get_val(self):
        return str(randint(self.min, self.max))


@dataclass()
class IdentityFieldGenerator(ValueGenerator):
    def get_val(self):
        return str(uuid.uuid4())


@dataclass()
class DateTimeGenerator(ValueGenerator):
    format: str
    randomize_lower: int
    randomize_upper: int

    def __init__(self, name, format="%Y-%m-%dT%H:%M:%SZ", randomize_lower=0, randomize_upper=0):
        self.format = format
        self.name = name
        self.randomize_upper = randomize_upper
        self.randomize_lower = randomize_lower

    def get_val(self):
        seed()
        random_range = randint(0, (self.randomize_upper - self.randomize_lower))
        mytime = time.time() + self.randomize_lower + random_range
        return datetime.fromtimestamp(mytime).strftime(self.format)


class DataLineGenerator:

    def __init__(self, generators: [ValueGenerator] = None, separator=";"):
        if generators is None:
            generators = []
        self.generators = generators
        self.separator = separator

    def generate(self):
        values = []

        for generator in self.generators:
            values.append(generator.get_val())

        return self.separator.join(values)

    def generateHeader(self):
        values = []
        for generator in self.generators:
            values.append(generator.get_name())

        return self.separator.join(values)
