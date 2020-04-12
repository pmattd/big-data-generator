import json
from dataclasses import dataclass

from data_generator.data_generator import RandomValueFieldGenerator, EnumeratedFieldGenerator, IdentityFieldGenerator


@dataclass()
class GeneratorConfiguration:
    def __init__(self, file_write_interval_in_seconds=1, path="", max_lines=1, line_write_interval_in_seconds=0,
                 max_files=1, base_filename="filename", value_separator=",",
                 generators=None):
        self.file_write_interval_in_seconds = file_write_interval_in_seconds
        self.path = path
        self.max_lines = max_lines
        self.generators = generators
        self.max_files = max_files
        self.base_filename = base_filename
        self.line_write_interval_in_seconds = line_write_interval_in_seconds
        self.value_separator = value_separator


class ConfigReader:
    def read_json(self, json_data):

        generator_config: GeneratorConfiguration

        with open(json_data, 'r') as f:
            parsed_json = json.load(f)
            generators = []

            # todo change to switch

            for field in parsed_json["fields"]:
                if field["type"] == "random-value":
                    generators.append(self.create_random_value_generator(field))
                if field["type"] == "enumeration":
                    generators.append(self.create_enumerated_field_generator(field))
                if field["type"] == "identity":
                    generators.append(self.create_identity_field_generator())

            return GeneratorConfiguration(parsed_json["file-write-interval-in-seconds"],
                                          parsed_json["path"],
                                          parsed_json["max-lines"],
                                          parsed_json["line-write-interval-in-seconds"],
                                          parsed_json["max-files"],
                                          parsed_json["base-filename"],
                                          parsed_json["value-separator"],
                                          generators)

    @staticmethod
    def create_random_value_generator(json):
        return RandomValueFieldGenerator(json["min"], json["max"])

    @staticmethod
    def create_enumerated_field_generator(json):
        return EnumeratedFieldGenerator(json["values"])

    @staticmethod
    def create_identity_field_generator():
        return IdentityFieldGenerator()
