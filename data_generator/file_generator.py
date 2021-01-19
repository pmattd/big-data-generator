import logging
import os
import time

logger = logging.getLogger(__name__)


# todo make immutable?
class WriteState:
    def __init__(self,
                 max_data_size: int = 10000000):
        self.max_data_size = max_data_size
        self.current_data_size = 0
        self.num_files = 0

    def add_string(self, s):
        self.add_data(len(s.encode('utf-8')))

    def add_data(self, data_size):
        self.current_data_size += data_size

    def stop_writing(self):
        return (self.max_data_size >= 0) and (self.current_data_size > self.max_data_size)

    def __str__(self):
        return "current data size: [{}] max data size : [{}]".format(self.current_data_size, self.max_data_size)

class FileGenerator:

    def __init__(self,
                 file_write_interval: int = 1,
                 file_path: str = "",
                 max_files: int = 1,
                 file_writer=None,
                 write_state: WriteState = None):
        self.interval = file_write_interval
        self.max_files = max_files
        self.file_writer = file_writer
        self.path = file_path
        self.write_state = write_state

    def schedule(self):
        os.makedirs(self.path, 0o777, True)

        for i in range(self.max_files):
            self.write()
            time.sleep(self.interval)
            if self.write_state.stop_writing():
                logger.info("stopping writing {}".format(str(self.write_state)))
                break

    def write(self):
        self.write_state = self.file_writer.write(self.path, self.write_state)


class CsvWriter:
    def __init__(self,
                 lines: int = 1,
                 line_write_interval: int = 0,
                 file_name_generator=None,
                 data_generator=None,
                 header=False):
        self.lines = lines
        self.line_interval = line_write_interval
        self.file_name_generator = file_name_generator
        self.data_generator = data_generator
        self.header = header

    def write(self, base_path, write_state):

        f = open(base_path + "/" + self.file_name_generator.get_name() + ".csv", "w+")

        if self.header:
            header = self.data_generator.generateHeader()
            write_state.add_string(header)
            f.write(header + "\n")

        for i in range(self.lines):
            line = self.data_generator.generate()

            write_state.add_string(line)
            if write_state.stop_writing():
                break

            f.write(line + "\n")

            if self.line_interval != 0:
                self.flush_and_wait(f)

        f.close()

        return write_state

    def flush_and_wait(self, f):
        f.flush()
        time.sleep(self.line_interval)

    def utf8len(self, s):
        return len(s.encode('utf-8'))


class SequentialFileName:

    def __init__(self, base_name=""):
        self.base_name = base_name
        self.sequence_number = 0

    def get_name(self):
        self.sequence_number = self.sequence_number + 1
        return self.base_name + str(++self.sequence_number)
