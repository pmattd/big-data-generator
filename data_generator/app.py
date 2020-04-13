import argparse
import logging

from data_generator.config_reader import GeneratorConfiguration, ConfigReader
from data_generator.data_line_generator import DataLineGenerator
from data_generator.file_generator import CsvWriter, SequentialFileName, FileGenerator, WriteState
from data_generator.log import configure_logging


def schedule(config_path):
    config: GeneratorConfiguration = ConfigReader().read_json(config_path)

    data_line_generator = DataLineGenerator(config.generators, config.value_separator)

    file_writer = CsvWriter(lines=config.max_lines,
                            line_write_interval=config.line_write_interval_in_seconds,
                            file_name_generator=SequentialFileName(config.base_filename),
                            data_generator=data_line_generator)

    file_generator = FileGenerator(file_write_interval=config.file_write_interval_in_seconds,
                                   file_path=config.path,
                                   max_files=config.max_files,
                                   file_writer=file_writer,
                                   write_state=WriteState(config.max_data_size))
    file_generator.schedule()

    print("generation completed")


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="path to a config file")
    parser.add_argument("-v", "--verbose", help="turn on verbose logging", action="store_true")
    args = parser.parse_args()

    configure_logging(args.verbose)

    config_file_path = args.config if args.config is not None else "config.json"

    logger.debug('config file is {}'.format(config_file_path))

    schedule(config_file_path)

# todo avro writer/ parquet writer
# todo pass the generator as a lambda
# todo add a random number of lines as a possibility
