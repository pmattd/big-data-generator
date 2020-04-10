import os
import time


class FileGenerator:

    # todo pass the generator as a lambda
    # todo add a random number of lines as a possibility
    # todo use the max size

    def __init__(self, interval: int = 1, path: str = "", max_files: int = 1, file_writer=None):
        self.interval = interval
        self.max_files = max_files
        self.file_writer = file_writer
        self.path = path

    def schedule(self):
        os.makedirs(self.path, 0o777, True)
        for i in range(self.max_files):
            self.write()
            time.sleep(self.interval)

    def write(self):
        self.file_writer.write(self.path)


class CsvWriter:
    def __init__(self, lines: int = 1,
                 file_name_generator=None,
                 data_generator=None):
        self.lines = lines
        self.file_name_generator = file_name_generator
        self.data_generator = data_generator

    def write(self, base_path):
        f = open(base_path + "/" + self.file_name_generator.get_name() + ".csv", "w+")
        for i in range(self.lines):
            f.write(self.data_generator.generate() + "\n")
        f.close()


class SequentialFileName:

    def __init__(self, base_name=""):
        self.base_name = base_name
        self.sequence_number = 0

    def get_name(self):
        self.sequence_number = self.sequence_number + 1
        return self.base_name + str(++self.sequence_number)
