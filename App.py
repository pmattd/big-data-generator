from DataFile import DataLineGenerator
from FileGenerator import FileGenerator, SequentialFileName, CsvWriter
from GeneratorConfiguration import ConfigReader, GeneratorConfiguration

if __name__ == '__main__':
    config: GeneratorConfiguration = ConfigReader().read_json("config.json")

    data_line_generator = DataLineGenerator(config.generators, ",")

    file_writer = CsvWriter(lines=config.max_lines,
                            file_name_generator=SequentialFileName(config.base_filename),
                            data_generator=data_line_generator)

    file_generator = FileGenerator(interval=config.interval_in_seconds,
                                   path=config.path,
                                   max_files=config.max_files,
                                   file_writer=file_writer)
    file_generator.schedule()

    print("generation completed")

# make the configuration an optional command line parameter
# make the script run in a process
# checkout other projects on github to see structure

# avro writer/ parquet writer
# max size in bytes
# clean up files
# logging
