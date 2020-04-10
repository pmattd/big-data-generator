import json
from dataclasses import dataclass

from DataFile import RandomValueFieldGenerator, EnumeratedFieldGenerator


@dataclass()
class GeneratorConfiguration:
    def __init__(self, interval_in_seconds=1, path="", max_lines=1, max_files=1, base_filename="filename",
                 generators=None):
        self.interval_in_seconds = interval_in_seconds
        self.path = path
        self.max_lines = max_lines
        self.generators = generators
        self.max_files = max_files
        self.base_filename = base_filename


class ConfigReader:
    def read_json(self, json_data):

        generator_config: GeneratorConfiguration

        with open(json_data, 'r') as f:
            parsed_json = json.load(f)
            generators = []

            for field in parsed_json["fields"]:
                if field["type"] == "random-value":
                    generators.append(self.create_random_value_generator(field))
                if field["type"] == "enumeration":
                    generators.append(self.create_enumerated_field_generator(field))

            print(json.dumps(parsed_json, indent=4, sort_keys=True))

            return GeneratorConfiguration(parsed_json["intervalInSeconds"],
                                          parsed_json["path"],
                                          parsed_json["max-lines"],
                                          parsed_json["max-files"],
                                          parsed_json["base-filename"],
                                          generators)

    def create_random_value_generator(self, json):
        return RandomValueFieldGenerator(json["min"], json["max"])

    def create_enumerated_field_generator(self, json):
        return EnumeratedFieldGenerator(json["values"])
