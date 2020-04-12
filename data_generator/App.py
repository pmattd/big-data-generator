import argparse

from data_generator.DataFile import DataLineGenerator
from data_generator.FileGenerator import CsvWriter, SequentialFileName, FileGenerator
from data_generator.GeneratorConfiguration import GeneratorConfiguration, ConfigReader


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
                                   file_writer=file_writer)
    file_generator.schedule()

    print("generation completed")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="path to a config file")
    args = parser.parse_args()

    config_file_path = args.config if args.config else "config.json"

    schedule(config_file_path)

# write some tests
# checkout other projects on github to see structure (venv etc)
# avro writer/ parquet writer
# max size in bytes
# clean up files
# logging
