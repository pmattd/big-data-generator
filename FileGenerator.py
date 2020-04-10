import os
import time


class FileGenerator:

    # todo pass the generator as a lambda
    # add a random number of lines as a possibility
    # use the max size

    def __init__(self, interval: int = 1, lines: int = 1, max_files: int = 1, path: str = "", generator=None,
                 file_name_generator=None):
        self.interval = interval
        self.path = path
        self.lines = lines
        self.max_files = max_files
        self.generator = generator
        self.file_name_generator = file_name_generator

    def schedule(self):
        os.makedirs(self.path, 0o777, True)
        for i in range(self.max_files):
            self.write()
            time.sleep(self.interval)

    def write(self):
        f = open(self.path + "/" + self.file_name_generator.get_name(), "w+")
        for i in range(self.lines):
            f.write(self.generator.generate() + "\n")
        f.close()


class SequentialFileName:

    def __init__(self, base_name=""):
        self.base_name = base_name
        self.sequence_number = 0

    def get_name(self):
        self.sequence_number = self.sequence_number + 1
        return self.base_name + str(++self.sequence_number)
